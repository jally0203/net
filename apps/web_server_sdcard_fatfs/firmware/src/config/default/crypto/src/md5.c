/**************************************************************************
  Crypto Framework Library Source

  Company:
    Microchip Technology Inc.

  File Name:
    md5.c
  
  Summary:
    Crypto Framework Libarary source for cryptographic functions.

  Description:
    This source file contains functions that make up the Cryptographic 
	Framework Library for PIC32 families of Microchip microcontrollers.
**************************************************************************/

//DOM-IGNORE-BEGIN
/******************************************************************************
File Name:  md5.c
Copyright � 2013-2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED �AS IS� WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END




#ifdef HAVE_CONFIG_H
    #include "config.h"
#endif
#include "system_config.h"

#include "crypto/src/settings.h"
#if !defined(NO_MD5)

#if defined(WOLFSSL_TI_HASH)
    /* #include <wolfcrypt/src/port/ti/ti-hash.c> included by wc_port.c */

#else

#include "crypto/src/md5.h"
#include "crypto/src/error-crypt.h"
#include "crypto/src/logging.h"

#ifdef NO_INLINE
    #include "crypto/src/misc.h"
#else
    #define WOLFSSL_MISC_INCLUDED
    #include "crypto/src/misc.c"
#endif


/* Hardware Acceleration */
#if defined(STM32F2_HASH) || defined(STM32F4_HASH)
    /*
     * STM32F2/F4 hardware MD5 support through the standard peripheral
     * library. (See note in README).
     */

    #define HAVE_MD5_CUST_API

    int wc_InitMd5_ex(Md5* md5, void* heap, int devId)
    {
        (void)heap;
        (void)devId;

        /* STM32 struct notes:
         * md5->buffer  = first 4 bytes used to hold partial block if needed
         * md5->buffLen = num bytes currently stored in md5->buffer
         * md5->loLen   = num bytes that have been written to STM32 FIFO
         */
        XMEMSET(md5->buffer, 0, MD5_REG_SIZE);

        md5->buffLen = 0;
        md5->loLen = 0;

        /* initialize HASH peripheral */
        HASH_DeInit();

        /* configure algo used, algo mode, datatype */
        HASH->CR &= ~ (HASH_CR_ALGO | HASH_CR_DATATYPE | HASH_CR_MODE);
        HASH->CR |= (HASH_AlgoSelection_MD5 | HASH_AlgoMode_HASH
                 | HASH_DataType_8b);

        /* reset HASH processor */
        HASH->CR |= HASH_CR_INIT;

        return 0;
    }

    int wc_Md5Update(Md5* md5, const byte* data, word32 len)
    {
        word32 i = 0;
        word32 fill = 0;
        word32 diff = 0;

        /* if saved partial block is available */
        if (md5->buffLen > 0) {
            fill = 4 - md5->buffLen;

            /* if enough data to fill, fill and push to FIFO */
            if (fill <= len) {
                XMEMCPY((byte*)md5->buffer + md5->buffLen, data, fill);
                HASH_DataIn(*(uint32_t*)md5->buffer);

                data += fill;
                len -= fill;
                md5->loLen += 4;
                md5->buffLen = 0;
            } else {
                /* append partial to existing stored block */
                XMEMCPY((byte*)md5->buffer + md5->buffLen, data, len);
                md5->buffLen += len;
                return 0;
            }
        }

        /* write input block in the IN FIFO */
        for (i = 0; i < len; i += 4)
        {
            diff = len - i;
            if (diff < 4) {
                /* store incomplete last block, not yet in FIFO */
                XMEMSET(md5->buffer, 0, MD5_REG_SIZE);
                XMEMCPY((byte*)md5->buffer, data, diff);
                md5->buffLen = diff;
            } else {
                HASH_DataIn(*(uint32_t*)data);
                data+=4;
            }
        }

        /* keep track of total data length thus far */
        md5->loLen += (len - md5->buffLen);

        return 0;
    }

    int wc_Md5Final(Md5* md5, byte* hash)
    {
        __IO uint16_t nbvalidbitsdata = 0;

        /* finish reading any trailing bytes into FIFO */
        if (md5->buffLen > 0) {
            HASH_DataIn(*(uint32_t*)md5->buffer);
            md5->loLen += md5->buffLen;
        }

        /* calculate number of valid bits in last word of input data */
        nbvalidbitsdata = 8 * (md5->loLen % MD5_REG_SIZE);

        /* configure number of valid bits in last word of the data */
        HASH_SetLastWordValidBitsNbr(nbvalidbitsdata);

        /* start HASH processor */
        HASH_StartDigest();

        /* wait until Busy flag == RESET */
        while (HASH_GetFlagStatus(HASH_FLAG_BUSY) != RESET) {}

        /* read message digest */
        md5->digest[0] = HASH->HR[0];
        md5->digest[1] = HASH->HR[1];
        md5->digest[2] = HASH->HR[2];
        md5->digest[3] = HASH->HR[3];

        ByteReverseWords(md5->digest, md5->digest, MD5_DIGEST_SIZE);

        XMEMCPY(hash, md5->digest, MD5_DIGEST_SIZE);

        return wc_InitMd5(md5);  /* reset state */
    }

#elif defined(FREESCALE_MMCAU_SHA)
    #include "cau_api.h"
    #define XTRANSFORM(S,B)  Transform((S), (B))

    static int Transform(Md5* md5, byte* data)
    {
        int ret = wolfSSL_CryptHwMutexLock();
        if(ret == 0) {
        #ifdef FREESCALE_MMCAU_CLASSIC_SHA
            cau_md5_hash_n(data, 1, (unsigned char*)md5->digest);
        #else
            MMCAU_MD5_HashN(data, 1, (uint32_t*)md5->digest);
        #endif
            wolfSSL_CryptHwMutexUnLock();
        }
        return ret;
    }

#elif defined(WOLFSSL_PIC32MZ_HASH)
    #include "crypto/src/pic32mz-crypt.h"
    #define HAVE_MD5_CUST_API

#else
    #define NEED_SOFT_MD5

#endif /* End Hardware Acceleration */


#ifdef NEED_SOFT_MD5

    #define XTRANSFORM(S,B)  Transform((S))

    #define F1(x, y, z) (z ^ (x & (y ^ z)))
    #define F2(x, y, z) F1(z, x, y)
    #define F3(x, y, z) (x ^ y ^ z)
    #define F4(x, y, z) (y ^ (x | ~z))

    #define MD5STEP(f, w, x, y, z, data, s) \
        w = rotlFixed(w + f(x, y, z) + data, s) + x

    static int Transform(Md5* md5)
    {
        /* Copy context->state[] to working vars  */
        word32 a = md5->digest[0];
        word32 b = md5->digest[1];
        word32 c = md5->digest[2];
        word32 d = md5->digest[3];

        MD5STEP(F1, a, b, c, d, md5->buffer[0]  + 0xd76aa478,  7);
        MD5STEP(F1, d, a, b, c, md5->buffer[1]  + 0xe8c7b756, 12);
        MD5STEP(F1, c, d, a, b, md5->buffer[2]  + 0x242070db, 17);
        MD5STEP(F1, b, c, d, a, md5->buffer[3]  + 0xc1bdceee, 22);
        MD5STEP(F1, a, b, c, d, md5->buffer[4]  + 0xf57c0faf,  7);
        MD5STEP(F1, d, a, b, c, md5->buffer[5]  + 0x4787c62a, 12);
        MD5STEP(F1, c, d, a, b, md5->buffer[6]  + 0xa8304613, 17);
        MD5STEP(F1, b, c, d, a, md5->buffer[7]  + 0xfd469501, 22);
        MD5STEP(F1, a, b, c, d, md5->buffer[8]  + 0x698098d8,  7);
        MD5STEP(F1, d, a, b, c, md5->buffer[9]  + 0x8b44f7af, 12);
        MD5STEP(F1, c, d, a, b, md5->buffer[10] + 0xffff5bb1, 17);
        MD5STEP(F1, b, c, d, a, md5->buffer[11] + 0x895cd7be, 22);
        MD5STEP(F1, a, b, c, d, md5->buffer[12] + 0x6b901122,  7);
        MD5STEP(F1, d, a, b, c, md5->buffer[13] + 0xfd987193, 12);
        MD5STEP(F1, c, d, a, b, md5->buffer[14] + 0xa679438e, 17);
        MD5STEP(F1, b, c, d, a, md5->buffer[15] + 0x49b40821, 22);

        MD5STEP(F2, a, b, c, d, md5->buffer[1]  + 0xf61e2562,  5);
        MD5STEP(F2, d, a, b, c, md5->buffer[6]  + 0xc040b340,  9);
        MD5STEP(F2, c, d, a, b, md5->buffer[11] + 0x265e5a51, 14);
        MD5STEP(F2, b, c, d, a, md5->buffer[0]  + 0xe9b6c7aa, 20);
        MD5STEP(F2, a, b, c, d, md5->buffer[5]  + 0xd62f105d,  5);
        MD5STEP(F2, d, a, b, c, md5->buffer[10] + 0x02441453,  9);
        MD5STEP(F2, c, d, a, b, md5->buffer[15] + 0xd8a1e681, 14);
        MD5STEP(F2, b, c, d, a, md5->buffer[4]  + 0xe7d3fbc8, 20);
        MD5STEP(F2, a, b, c, d, md5->buffer[9]  + 0x21e1cde6,  5);
        MD5STEP(F2, d, a, b, c, md5->buffer[14] + 0xc33707d6,  9);
        MD5STEP(F2, c, d, a, b, md5->buffer[3]  + 0xf4d50d87, 14);
        MD5STEP(F2, b, c, d, a, md5->buffer[8]  + 0x455a14ed, 20);
        MD5STEP(F2, a, b, c, d, md5->buffer[13] + 0xa9e3e905,  5);
        MD5STEP(F2, d, a, b, c, md5->buffer[2]  + 0xfcefa3f8,  9);
        MD5STEP(F2, c, d, a, b, md5->buffer[7]  + 0x676f02d9, 14);
        MD5STEP(F2, b, c, d, a, md5->buffer[12] + 0x8d2a4c8a, 20);

        MD5STEP(F3, a, b, c, d, md5->buffer[5]  + 0xfffa3942,  4);
        MD5STEP(F3, d, a, b, c, md5->buffer[8]  + 0x8771f681, 11);
        MD5STEP(F3, c, d, a, b, md5->buffer[11] + 0x6d9d6122, 16);
        MD5STEP(F3, b, c, d, a, md5->buffer[14] + 0xfde5380c, 23);
        MD5STEP(F3, a, b, c, d, md5->buffer[1]  + 0xa4beea44,  4);
        MD5STEP(F3, d, a, b, c, md5->buffer[4]  + 0x4bdecfa9, 11);
        MD5STEP(F3, c, d, a, b, md5->buffer[7]  + 0xf6bb4b60, 16);
        MD5STEP(F3, b, c, d, a, md5->buffer[10] + 0xbebfbc70, 23);
        MD5STEP(F3, a, b, c, d, md5->buffer[13] + 0x289b7ec6,  4);
        MD5STEP(F3, d, a, b, c, md5->buffer[0]  + 0xeaa127fa, 11);
        MD5STEP(F3, c, d, a, b, md5->buffer[3]  + 0xd4ef3085, 16);
        MD5STEP(F3, b, c, d, a, md5->buffer[6]  + 0x04881d05, 23);
        MD5STEP(F3, a, b, c, d, md5->buffer[9]  + 0xd9d4d039,  4);
        MD5STEP(F3, d, a, b, c, md5->buffer[12] + 0xe6db99e5, 11);
        MD5STEP(F3, c, d, a, b, md5->buffer[15] + 0x1fa27cf8, 16);
        MD5STEP(F3, b, c, d, a, md5->buffer[2]  + 0xc4ac5665, 23);

        MD5STEP(F4, a, b, c, d, md5->buffer[0]  + 0xf4292244,  6);
        MD5STEP(F4, d, a, b, c, md5->buffer[7]  + 0x432aff97, 10);
        MD5STEP(F4, c, d, a, b, md5->buffer[14] + 0xab9423a7, 15);
        MD5STEP(F4, b, c, d, a, md5->buffer[5]  + 0xfc93a039, 21);
        MD5STEP(F4, a, b, c, d, md5->buffer[12] + 0x655b59c3,  6);
        MD5STEP(F4, d, a, b, c, md5->buffer[3]  + 0x8f0ccc92, 10);
        MD5STEP(F4, c, d, a, b, md5->buffer[10] + 0xffeff47d, 15);
        MD5STEP(F4, b, c, d, a, md5->buffer[1]  + 0x85845dd1, 21);
        MD5STEP(F4, a, b, c, d, md5->buffer[8]  + 0x6fa87e4f,  6);
        MD5STEP(F4, d, a, b, c, md5->buffer[15] + 0xfe2ce6e0, 10);
        MD5STEP(F4, c, d, a, b, md5->buffer[6]  + 0xa3014314, 15);
        MD5STEP(F4, b, c, d, a, md5->buffer[13] + 0x4e0811a1, 21);
        MD5STEP(F4, a, b, c, d, md5->buffer[4]  + 0xf7537e82,  6);
        MD5STEP(F4, d, a, b, c, md5->buffer[11] + 0xbd3af235, 10);
        MD5STEP(F4, c, d, a, b, md5->buffer[2]  + 0x2ad7d2bb, 15);
        MD5STEP(F4, b, c, d, a, md5->buffer[9]  + 0xeb86d391, 21);

        /* Add the working vars back into digest state[]  */
        md5->digest[0] += a;
        md5->digest[1] += b;
        md5->digest[2] += c;
        md5->digest[3] += d;

        return 0;
    }
#endif /* NEED_SOFT_MD5 */


#ifndef HAVE_MD5_CUST_API
static INLINE void AddMd5Length(Md5* md5, word32 len)
{
    word32 tmp = md5->loLen;
    if ((md5->loLen += len) < tmp) {
        md5->hiLen++;                       /* carry low to high */
    }
}

static int _InitMd5(Md5* md5)
{
    int ret = 0;

    md5->digest[0] = 0x67452301L;
    md5->digest[1] = 0xefcdab89L;
    md5->digest[2] = 0x98badcfeL;
    md5->digest[3] = 0x10325476L;

    md5->buffLen = 0;
    md5->loLen   = 0;
    md5->hiLen   = 0;

    return ret;
}

int wc_InitMd5_ex(Md5* md5, void* heap, int devId)
{
    int ret = 0;

    if (md5 == NULL)
        return BAD_FUNC_ARG;

    md5->heap = heap;

    ret = _InitMd5(md5);
    if (ret != 0)
        return ret;

#if defined(WOLFSSL_ASYNC_CRYPT) && defined(WC_ASYNC_ENABLE_MD5)
    ret = wolfAsync_DevCtxInit(&md5->asyncDev, WOLFSSL_ASYNC_MARKER_MD5,
                                                            md5->heap, devId);
#else
    (void)devId;
#endif
    return ret;
}

int wc_Md5Update(Md5* md5, const byte* data, word32 len)
{
    int ret = 0;
    byte* local;

    if (md5 == NULL || (data == NULL && len > 0)) {
        return BAD_FUNC_ARG;
    }

#if defined(WOLFSSL_ASYNC_CRYPT) && defined(WC_ASYNC_ENABLE_MD5)
    if (md5->asyncDev.marker == WOLFSSL_ASYNC_MARKER_MD5) {
    #if defined(HAVE_INTEL_QA)
        return IntelQaSymMd5(&md5->asyncDev, NULL, data, len);
    #endif
    }
#endif /* WOLFSSL_ASYNC_CRYPT */

    /* do block size increments */
    local = (byte*)md5->buffer;

    /* check that internal buffLen is valid */
    if (md5->buffLen >= MD5_BLOCK_SIZE)
        return BUFFER_E;

    while (len) {
        word32 add = min(len, MD5_BLOCK_SIZE - md5->buffLen);
        XMEMCPY(&local[md5->buffLen], data, add);

        md5->buffLen += add;
        data         += add;
        len          -= add;

        if (md5->buffLen == MD5_BLOCK_SIZE) {
        #if defined(BIG_ENDIAN_ORDER) && !defined(FREESCALE_MMCAU_SHA)
            ByteReverseWords(md5->buffer, md5->buffer, MD5_BLOCK_SIZE);
        #endif
            XTRANSFORM(md5, local);
            AddMd5Length(md5, MD5_BLOCK_SIZE);
            md5->buffLen = 0;
        }
    }
    return ret;
}

int wc_Md5Final(Md5* md5, byte* hash)
{
    byte* local;

    if (md5 == NULL || hash == NULL) {
        return BAD_FUNC_ARG;
    }

#if defined(WOLFSSL_ASYNC_CRYPT) && defined(WC_ASYNC_ENABLE_MD5)
    if (md5->asyncDev.marker == WOLFSSL_ASYNC_MARKER_MD5) {
    #if defined(HAVE_INTEL_QA)
        return IntelQaSymMd5(&md5->asyncDev, hash, NULL, MD5_DIGEST_SIZE);
    #endif
    }
#endif /* WOLFSSL_ASYNC_CRYPT */

    local = (byte*)md5->buffer;

    AddMd5Length(md5, md5->buffLen);  /* before adding pads */
    local[md5->buffLen++] = 0x80;  /* add 1 */

    /* pad with zeros */
    if (md5->buffLen > MD5_PAD_SIZE) {
        XMEMSET(&local[md5->buffLen], 0, MD5_BLOCK_SIZE - md5->buffLen);
        md5->buffLen += MD5_BLOCK_SIZE - md5->buffLen;

    #if defined(BIG_ENDIAN_ORDER) && !defined(FREESCALE_MMCAU_SHA)
        ByteReverseWords(md5->buffer, md5->buffer, MD5_BLOCK_SIZE);
    #endif
        XTRANSFORM(md5, local);
        md5->buffLen = 0;
    }
    XMEMSET(&local[md5->buffLen], 0, MD5_PAD_SIZE - md5->buffLen);

#if defined(BIG_ENDIAN_ORDER) && !defined(FREESCALE_MMCAU_SHA)
    ByteReverseWords(md5->buffer, md5->buffer, MD5_BLOCK_SIZE);
#endif

    /* put lengths in bits */
    md5->hiLen = (md5->loLen >> (8*sizeof(md5->loLen) - 3)) +
                 (md5->hiLen << 3);
    md5->loLen = md5->loLen << 3;

    /* store lengths */
    /* ! length ordering dependent on digest endian type ! */
    XMEMCPY(&local[MD5_PAD_SIZE], &md5->loLen, sizeof(word32));
    XMEMCPY(&local[MD5_PAD_SIZE + sizeof(word32)], &md5->hiLen, sizeof(word32));

    /* final transform and result to hash */
    XTRANSFORM(md5, local);
#ifdef BIG_ENDIAN_ORDER
    ByteReverseWords(md5->digest, md5->digest, MD5_DIGEST_SIZE);
#endif
    XMEMCPY(hash, md5->digest, MD5_DIGEST_SIZE);

    return _InitMd5(md5); /* reset state */
}
#endif /* !HAVE_MD5_CUST_API */


int wc_InitMd5(Md5* md5)
{
    if (md5 == NULL) {
        return BAD_FUNC_ARG;
    }
    return wc_InitMd5_ex(md5, NULL, INVALID_DEVID);
}

void wc_Md5Free(Md5* md5)
{
    if (md5 == NULL)
        return;
#if defined(WOLFSSL_ASYNC_CRYPT) && defined(WC_ASYNC_ENABLE_MD5)
    wolfAsync_DevCtxFree(&md5->asyncDev, WOLFSSL_ASYNC_MARKER_MD5);
#endif /* WOLFSSL_ASYNC_CRYPT */
}

int wc_Md5GetHash(Md5* md5, byte* hash)
{
    int ret;
    Md5 tmpMd5;

    if (md5 == NULL || hash == NULL)
        return BAD_FUNC_ARG;

    ret = wc_Md5Copy(md5, &tmpMd5);
    if (ret == 0) {
        ret = wc_Md5Final(&tmpMd5, hash);
    }

    return ret;
}

int wc_Md5Copy(Md5* src, Md5* dst)
{
    int ret = 0;

    if (src == NULL || dst == NULL)
        return BAD_FUNC_ARG;

    XMEMCPY(dst, src, sizeof(Md5));

#ifdef WOLFSSL_ASYNC_CRYPT
    ret = wolfAsync_DevCopy(&src->asyncDev, &dst->asyncDev);
#endif
#ifdef WOLFSSL_PIC32MZ_HASH
    ret = wc_Pic32HashCopy(&src->cache, &dst->cache);
#endif

    return ret;
}

#endif /* WOLFSSL_TI_HASH */
#endif /* NO_MD5 */