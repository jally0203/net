<#--
/*******************************************************************************
  TCPIP MAC Freemarker Template File

  Company:
    Microchip Technology Inc.

  File Name:
    tcpip_mac_pic32c.h.ftl

  Summary:
    TCPIP MAC Freemarker Template File

  Description:

*******************************************************************************/
-->

<#----------------------------------------------------------------------------
 Copyright (C) 2014-2018 Microchip Technology Inc. and its subsidiaries.

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
----------------------------------------------------------------------------->
<#if TCPIP_USE_ETH_MAC == true>
/*** TCPIP MAC Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY}
#define TCPIP_GMAC_RX_BUFF_SIZE_DUMMY				    	${TCPIP_GMAC_RX_BUFF_SIZE_DUMMY}
#define TCPIP_GMAC_TX_BUFF_SIZE_DUMMY				    	${TCPIP_GMAC_TX_BUFF_SIZE_DUMMY}

<#if TCPIP_GMAC_QUEUE_0 == true>
/*** QUEUE 0 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE0				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE0}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE0				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE0}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE0				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE0}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE0				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE0 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE0				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE0}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE0					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE0}
<#else>
/*** QUEUE 0 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE0				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE0				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE0				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE0				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE0				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE0					0
</#if>

<#if (TCPIP_GMAC_QUEUE_1)?has_content>
<#if TCPIP_GMAC_QUEUE_1 == true>
/*** QUEUE 1 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE1				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE1}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE1				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE1}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE1				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE1}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE1				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE1 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE1				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE1}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE1					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE1}
<#else>
/*** QUEUE 1 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE1				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE1				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE1				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE1				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE1				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE1					0
</#if>
</#if>

<#if (TCPIP_GMAC_QUEUE_2)?has_content>
<#if TCPIP_GMAC_QUEUE_2 == true>
/*** QUEUE 2 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE2				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE2}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE2				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE2}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE2				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE2}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE2				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE2 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE2				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE2}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE2					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE2}
<#else>
/*** QUEUE 2 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE2				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE2				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE2				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE2				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE2				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE2					0
</#if>
</#if>

<#if (TCPIP_GMAC_QUEUE_3)?has_content>
<#if TCPIP_GMAC_QUEUE_3 == true>
/*** QUEUE 3 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE3				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE3}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE3				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE3}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE3				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE3}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE3				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE3 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE3				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE3}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE3					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE3}
<#else>
/*** QUEUE 3 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE3				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE3				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE3				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE3				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE3				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE3					0
</#if>
</#if>

<#if (TCPIP_GMAC_QUEUE_4)?has_content>
<#if TCPIP_GMAC_QUEUE_4 == true>
/*** QUEUE 4 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE4				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE4}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE4				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE4}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE4				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE4}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE4				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE4 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE4				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE4}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE4					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE4}
<#else>
/*** QUEUE 4 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE4				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE4				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE4				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE4				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE4				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE4					0
</#if>
</#if>

<#if (TCPIP_GMAC_QUEUE_5)?has_content>
<#if TCPIP_GMAC_QUEUE_5 == true>
/*** QUEUE 5 Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE5				${TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE5}
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5				${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5}
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE5				    	${TCPIP_GMAC_RX_BUFF_SIZE_QUE5}
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE5				    	${TCPIP_GMAC_TX_BUFF_SIZE_QUE5}
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE5				   		${TCPIP_GMAC_RX_ADDL_BUFF_COUNT_QUE5 + TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE5				${TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE5}
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE5					${TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE5}
<#else>
/*** QUEUE 5 Disabled; Dummy Configuration ***/
#define TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE5				TCPIP_GMAC_TX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5				TCPIP_GMAC_RX_DESCRIPTORS_COUNT_DUMMY
#define TCPIP_GMAC_RX_BUFF_SIZE_QUE5				    	TCPIP_GMAC_RX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_TX_BUFF_SIZE_QUE5				    	TCPIP_GMAC_TX_BUFF_SIZE_DUMMY
#define TCPIP_GMAC_RX_BUFF_COUNT_QUE5				   		${TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5}
#define TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE5				0
#define TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE5					0
</#if>
</#if>

#define TCPIP_GMAC_RX_MAX_FRAME		    			${TCPIP_GMAC_RX_MAX_FRAME}
#define TCPIP_GMAC_RX_FILTERS                       \
<#if TCPIP_GMAC_ETH_FILTER_BCAST_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_BCAST_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_MCAST_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_MCAST_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_UCAST_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_UCAST_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_MCAST_HASH_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_MCAST_HASH_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_UCAST_HASH_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_UCAST_HASH_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_CRC_ERROR_REJECT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_CRC_ERROR_REJECT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_CRC_ERROR_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_CRC_ERROR_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_MAX_FRAME_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_MAXFRAME_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_ALL_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_ALL_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_FRAME_ERROR_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_FRAMEERROR_ACCEPT |\
</#if>
<#if TCPIP_GMAC_ETH_FILTER_JUMBO_FRAME_ACCEPT>
                                                    TCPIP_MAC_RX_FILTER_TYPE_JUMBOFRAME_ACCEPT |\
</#if>
                                                    0
#define TCPIP_GMAC_ETH_OPEN_FLAGS       			\
<#if TCPIP_GMAC_ETH_OF_AUTO_NEGOTIATION>
                                                    TCPIP_ETH_OPEN_AUTO |\
</#if>
<#if TCPIP_GMAC_ETH_OF_FULL_DUPLEX>
                                                    TCPIP_ETH_OPEN_FDUPLEX |\
</#if>
<#if TCPIP_GMAC_ETH_OF_HALF_DUPLEX>
                                                    TCPIP_ETH_OPEN_HDUPLEX |\
</#if>
<#if TCPIP_GMAC_ETH_OF_100>
                                                    TCPIP_ETH_OPEN_100 |\
</#if>
<#if TCPIP_GMAC_ETH_OF_10>
                                                    TCPIP_ETH_OPEN_10 |\
</#if>
<#if TCPIP_GMAC_ETH_OF_HUGE_PKTS>
                                                    TCPIP_ETH_OPEN_HUGE_PKTS |\
</#if>
<#if TCPIP_GMAC_ETH_OF_MAC_LOOPBACK>
                                                    TCPIP_ETH_OPEN_MAC_LOOPBACK |\
</#if>
<#if TCPIP_GMAC_ETH_OF_PHY_LOOPBACK>
                                                    TCPIP_ETH_OPEN_PHY_LOOPBACK |\
</#if>
<#if TCPIP_GMAC_ETH_OF_MDIX_AUTO>
                                                    TCPIP_ETH_OPEN_MDIX_AUTO |\
</#if>
<#if TCPIP_GMAC_ETH_OF_MDIX_SWAP>
                                                    TCPIP_ETH_OPEN_MDIX_SWAP |\
</#if>
<#if TCPIP_GMAC_ETH_OF_RMII>
                                                    TCPIP_ETH_OPEN_RMII |\
</#if>
                                                    0

#define TCPIP_INTMAC_MODULE_ID		    			${TCPIP_INTMAC_MODULE_ID}
<#if (TCPIP_INTMAC_DEVICE)?has_content>
<#if TCPIP_INTMAC_DEVICE == "SAME7x_V7x">
#define TCPIP_INTMAC_PERIPHERAL_CLK  				${core.MASTER_CLOCK_FREQUENCY}
<#elseif TCPIP_INTMAC_DEVICE == "SAME5x">
#define TCPIP_INTMAC_PERIPHERAL_CLK  				${core.MAIN_CLOCK_FREQUENCY}
<#elseif TCPIP_INTMAC_DEVICE == "SAMA5D2">
#define TCPIP_INTMAC_PERIPHERAL_CLK  				${core.MCK_CLK_FREQUENCY}
</#if>
</#if>

#define DRV_GMAC_INSTANCES_NUMBER				${DRV_GMAC_INSTANCES_NUMBER}
#define DRV_GMAC_NUMBER_OF_QUEUES				${DRV_GMAC_NUMBER_OF_QUEUES}
#define DRV_GMAC_CLIENTS_NUMBER					${DRV_GMAC_CLIENTS_NUMBER}
#define DRV_GMAC_INDEX	    	    				${DRV_GMAC_INDEX}
#define DRV_GMAC_PERIPHERAL_ID					${DRV_GMAC_PERIPHERAL_ID}
#define DRV_GMAC_INTERRUPT_SOURCE				${DRV_GMAC_INTERRUPT_SOURCE}

<#if DRV_GMAC_INTERRUPT_MODE == true>
#define DRV_GMAC_INTERRUPT_MODE        				true
<#else>
#define DRV_GMAC_INTERRUPT_MODE        				true
</#if>
#define DRV_GMAC_RMII_MODE					${DRV_GMAC_RMII_VALUE}
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->
