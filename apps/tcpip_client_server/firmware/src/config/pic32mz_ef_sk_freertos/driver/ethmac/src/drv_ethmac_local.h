/*******************************************************************************
  Ethernet MAC Driver Local Data Structures

  Company:
    Microchip Technology Inc.

  File Name:
    drv_ethmac_local.h

  Summary:
    Ethernet MAC driver local declarations and definitions.

  Description:
    This file contains the Ethernet MAC driver's local declarations and definitions.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*****************************************************************************
 Copyright (C) 2013-2018 Microchip Technology Inc. and its subsidiaries.

Microchip Technology Inc. and its subsidiaries.

Subject to your compliance with these terms, you may use Microchip software 
and any derivatives exclusively with Microchip products. It is your 
responsibility to comply with third party license terms applicable to your 
use of third party software (including open source software) that may 
accompany Microchip software.

THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED 
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR 
PURPOSE.

IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS 
BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE 
FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN 
ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, 
THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************/

//DOM-IGNORE-END

#ifndef _DRV_ETHMAC_LOCAL_H
#define _DRV_ETHMAC_LOCAL_H

// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>

#include "system_config.h"
#include "system/system.h"

#include "system/int/sys_int.h"
#include "system/time/sys_time.h"

#include "tcpip/tcpip_mac_object.h"


#include "driver/ethphy/drv_ethphy.h"
#include "driver/ethmac/drv_ethmac.h"


// *****************************************************************************
// *****************************************************************************
// Section: Data Type Definitions
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* TCPIP Stack Event Descriptor

  Summary:

  Description:

  Remarks:
    None
*/
typedef struct
{
    TCPIP_MAC_EVENT             _TcpEnabledEvents;          // group enabled notification events
    volatile TCPIP_MAC_EVENT    _TcpPendingEvents;          // group notification events that are set, waiting to be re-acknowledged
    DRV_ETH_EVENTS             _EthEnabledEvents;          // copy in DRV_ETH_EVENTS space
    volatile DRV_ETH_EVENTS    _EthPendingEvents;          // copy in DRV_ETH_EVENTS space
    TCPIP_MAC_EventF            _TcpNotifyFnc;              // group notification handler
    const void*                 _TcpNotifyParam;            // notification parameter
}DRV_ETHMAC_EVENT_DCPT;   // event descriptor per group

// transmit directly from within ISR
// provides a faster response when running out of
// TX descriptors
//
//#define ETH_PIC32_INT_MAC_ISR_TX


// synchronization for the RX flow
// The RX packets are allocated by the MAC and
// passed to the stack in manager context but
// acknowledged by the stack (user threads)
// when contents is processed
// Synchronization is needed
// If a semaphore is used then the packet RX flow (manager)
// could be blocked waiting for user threads.
// For better performance this should be avoided.
// When not using a semaphore lock, a critical section
// will be used.
//#define   DRV_ETHMAC_USE_RX_SEMAPHORE_LOCK
#define   DRV_ETHMAC_USE_TX_SEMAPHORE_LOCK


#define ETH_PIC32_INT_MAC_MIN_RX_SIZE           128     // minimum RX buffer size
                                                        // less than this creates excessive fragmentation
                                                        // Keep it always multiple of 16!

#define ETH_PIC32_INT_MAC_MIN_TX_DESCRIPTORS    4       // minimum number of TX descriptors
                                                        // needed to accomodate zero copy and TCP traffic
                                                        //
// *****************************************************************************
/* Ethernet Driver Module Link check states

  Summary:
    List of the states to read the current link status

  Description:
    List of the states to read the current link status

  Remarks:
    None
*/

typedef enum
{
    DRV_ETHMAC_LINK_CHECK_START_LINK  = 0,
    DRV_ETHMAC_LINK_CHECK_GET_LINK,
    DRV_ETHMAC_LINK_CHECK_WAIT_LINK_UP,
    DRV_ETHMAC_LINK_CHECK_NEG_COMPLETE,
    DRV_ETHMAC_LINK_CHECK_NEG_RESULT,
}DRV_ETHMAC_LINK_CHECK_STATE;


// *****************************************************************************
/* PIC32 Embedded MAC Data Structure

  Summary:

  Description:

  Remarks:
    Dynamic data needed for the embedded PIC32 MAC
*/

typedef struct
{
    unsigned int        _macIx;             // index of the MAC, for multiple MAC's support
    unsigned int        _phyIx;             // index of the associated PHY
    SYS_MODULE_OBJ      hPhySysObject;      // PHY object handle
    SYS_MODULE_OBJ      hPhyClient;         // PHY handle
    SYS_STATUS          sysStat;            // driver status
    union
    {
        uint16_t        val;
        struct
        {
            uint16_t    _init               : 1;    // the corresponding MAC is initialized
            uint16_t    _open               : 1;    // the corresponding MAC is opened
            uint16_t    _linkPresent        : 1;    // lif connection to the PHY properly detected : on/off
            uint16_t    _linkNegotiation    : 1;    // if an auto-negotiation is in effect : on/off
            uint16_t	_linkPrev           : 1;    // last value of the link status: on/off
            uint16_t	_linkUpDone       : 1;      // the link up sequence done
            // add another flags here
        };
    }                   _macFlags;          // corresponding MAC flags

    TCPIP_MODULE_MAC_PIC32INT_CONFIG    macConfig;  // configuration parameters
    DRV_ETHERNET_REGISTERS*             pEthReg;    // pointer to Ethernet registers describing the peripheral

    DRV_ETHMAC_SGL_LIST _TxQueue;           // current TX queue; stores TX queued packets 

    // general stuff
    const void*            _AllocH ;        // allocation handle  
    TCPIP_MAC_HEAP_CallocF _callocF;        // allocation functions
    TCPIP_MAC_HEAP_FreeF   _freeF;

    // packet allocation functions
    TCPIP_MAC_PKT_AllocF    pktAllocF;
    TCPIP_MAC_PKT_FreeF     pktFreeF;
    TCPIP_MAC_PKT_AckF      pktAckF;
    
    // synhchronization
    TCPIP_MAC_SynchReqF     _synchF;

    // timing and link status maintenance
    TCPIP_ETH_OPEN_FLAGS      _linkResFlags;        // resulted link flags
    uint32_t            _linkUpTick;          // tick value when the link up sequence was started
    uint32_t            _linkWaitTick;        // tick value to wait for
    DRV_ETHPHY_NEGOTIATION_RESULT   _negResult;  // negotiation result storage
    DRV_ETHMAC_LINK_CHECK_STATE _linkCheckState;    // link state machine current status

    INT_SOURCE     _macIntSrc;             // this MAC interrupt source

    DRV_ETHMAC_EVENT_DCPT _pic32_ev_group_dcpt;
#if defined(ETH_PIC32_INT_MAC_ISR_TX)
    DRV_ETHMAC_SGL_LIST _TxAckQueue;        // TX acknowledgement queue; stores TX packets that need to be acknowledged 
#endif  // defined(ETH_PIC32_INT_MAC_ISR_TX)

    // rx descriptor; supports maximum fragmentation
    DRV_ETHMAC_PKT_DCPT         rxPktDcpt[TCPIP_EMAC_RX_FRAGMENTS];

    // descriptor lists
    // for PIC32MZ these need to be 16 bytes aligned!
    // Aligning them will conserve some space
    DRV_ETHMAC_DCPT_LIST _EnetTxFreeList;    // transmit list of free descriptors
    DRV_ETHMAC_DCPT_LIST _EnetTxBusyList;    // transmit list of descriptors passed to the Tx Engine
                                     // the _EnetTxBusyList always ends with an sw owned descriptor (hdr.EOWN=0);

    DRV_ETHMAC_DCPT_LIST _EnetRxFreeList;    // receive list of free descriptors
    DRV_ETHMAC_DCPT_LIST _EnetRxBusyList;    // receive list of descriptors passed to the Rx Engine

    DRV_ETHMAC_DCPT_LIST* _EnetTxFreePtr;    // pointer to the transmit list of free descriptors
    DRV_ETHMAC_DCPT_LIST* _EnetTxBusyPtr;    // pointer to the transmit list of descriptors passed to the Tx Engine

    DRV_ETHMAC_DCPT_LIST* _EnetRxFreePtr;    // pointer to the receive list of free descriptors
    DRV_ETHMAC_DCPT_LIST* _EnetRxBusyPtr;    // pointer to the receive list of descriptors passed to the Rx Engine

    uintptr_t             _syncRxH;          // synch object handle for RX operations
    uintptr_t             _syncTxH;          // synch object handle for TX operations

    // debug: run time statistics
    TCPIP_MAC_RX_STATISTICS _rxStat;
    TCPIP_MAC_TX_STATISTICS _txStat;


} DRV_ETHMAC_INSTANCE_DATA;


// *****************************************************************************
/* PIC32 Embedded MAC Descriptor

  Summary:

  Description:

  Remarks:
    the embedded PIC32 MAC descriptor
    support for multiple instances
*/

typedef struct
{
    const TCPIP_MAC_OBJECT* pObj;  // safe cast to TCPIP_MAC_DCPT
    DRV_ETHMAC_INSTANCE_DATA     mData;  // specific PIC32 MAC data

} DRV_ETHMAC_INSTANCE_DCPT;



typedef uint16_t (*DRV_ETHMAC_HW_REG_FUNC)(DRV_ETHERNET_REGISTERS* ethId);

// *****************************************************************************
/* PIC32 MAC Hardware statistics register access structure

  Summary:

  Description:
    Abstraction of the HW statistics registers

  Remarks:
*/

typedef struct
{
    char                    regName[8 + 1]; // hardware name + \0
    DRV_ETHMAC_HW_REG_FUNC  regFunc;        // register access function
} DRV_ETHMAC_HW_REG_DCPT;




#endif //#ifndef _DRV_ETHMAC_LOCAL_H

/*******************************************************************************
 End of File
*/

