/*******************************************************************************
  System Initialization File

  File Name:
    initialization.c

  Summary:
    This file contains source code necessary to initialize the system.

  Description:
    This file contains source code necessary to initialize the system.  It
    implements the "SYS_Initialize" function, defines the configuration bits,
    and allocates any necessary global system resources,
 *******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "configuration.h"
#include "definitions.h"
#include "device.h"



// ****************************************************************************
// ****************************************************************************
// Section: Configuration Bits
// ****************************************************************************
// ****************************************************************************



// *****************************************************************************
// *****************************************************************************
// Section: Driver Initialization Data
// *****************************************************************************
// *****************************************************************************


/* MIIM Driver Configuration */
static const DRV_MIIM_INIT drvMiimInitData =
{
    .ethphyId = DRV_MIIM_ETH_MODULE_ID,
};



// *****************************************************************************
// *****************************************************************************
// Section: System Data
// *****************************************************************************
// *****************************************************************************
/* Structure to hold the object handles for the modules in the system. */
SYSTEM_OBJECTS sysObj;

// *****************************************************************************
// *****************************************************************************
// Section: Library/Stack Initialization Data
// *****************************************************************************
// *****************************************************************************

// <editor-fold defaultstate="collapsed" desc="TCP/IP Stack Initialization Data">
// *****************************************************************************
// *****************************************************************************
// Section: TCPIP Data
// *****************************************************************************
// *****************************************************************************
/*** ARP Service Initialization Data ***/
const TCPIP_ARP_MODULE_CONFIG tcpipARPInitData =
{ 
    .cacheEntries       = TCPIP_ARP_CACHE_ENTRIES,     
    .deleteOld          = TCPIP_ARP_CACHE_DELETE_OLD,    
    .entrySolvedTmo     = TCPIP_ARP_CACHE_SOLVED_ENTRY_TMO, 
    .entryPendingTmo    = TCPIP_ARP_CACHE_PENDING_ENTRY_TMO, 
    .entryRetryTmo      = TCPIP_ARP_CACHE_PENDING_RETRY_TMO, 
    .permQuota          = TCPIP_ARP_CACHE_PERMANENT_QUOTA, 
    .purgeThres         = TCPIP_ARP_CACHE_PURGE_THRESHOLD, 
    .purgeQuanta        = TCPIP_ARP_CACHE_PURGE_QUANTA, 
    .retries            = TCPIP_ARP_CACHE_ENTRY_RETRIES, 
    .gratProbeCount     = TCPIP_ARP_GRATUITOUS_PROBE_COUNT,
};

/*** Announce Discovery Initialization Data ***/
const TCPIP_ANNOUNCE_MODULE_CONFIG tcpipAnnounceInitData =
{ 
    0
};

/*** UDP Sockets Initialization Data ***/
const TCPIP_UDP_MODULE_CONFIG tcpipUDPInitData =
{
    .nSockets       = TCPIP_UDP_MAX_SOCKETS,
    .sktTxBuffSize  = TCPIP_UDP_SOCKET_DEFAULT_TX_SIZE, 
};

/*** TCP Sockets Initialization Data ***/
const TCPIP_TCP_MODULE_CONFIG tcpipTCPInitData =
{
    .nSockets       = TCPIP_TCP_MAX_SOCKETS,
    .sktTxBuffSize  = TCPIP_TCP_SOCKET_DEFAULT_TX_SIZE, 
    .sktRxBuffSize  = TCPIP_TCP_SOCKET_DEFAULT_RX_SIZE,
};






/*** DHCP client Initialization Data ***/
const TCPIP_DHCP_MODULE_CONFIG tcpipDHCPInitData =
{     
    .dhcpEnable     = TCPIP_DHCP_CLIENT_ENABLED,   
    .dhcpTmo        = TCPIP_DHCP_TIMEOUT,
    .dhcpCliPort    = TCPIP_DHCP_CLIENT_CONNECT_PORT,
    .dhcpSrvPort    = TCPIP_DHCP_SERVER_LISTEN_PORT,

};


/*** ICMP Server Initialization Data ***/
const TCPIP_ICMP_MODULE_CONFIG tcpipICMPInitData = 
{
    0
};

/*** NBNS Server Initialization Data ***/
const TCPIP_NBNS_MODULE_CONFIG tcpipNBNSInitData =
{ 
    0
};





/*** ETH PHY Initialization Data ***/



const DRV_ETHPHY_INIT tcpipPhyInitData =
{    
    .ethphyId               = TCPIP_INTMAC_MODULE_ID,
    .phyAddress             = TCPIP_INTMAC_PHY_ADDRESS,
    .phyFlags               = TCPIP_INTMAC_PHY_CONFIG_FLAGS,
    .pPhyObject             = &DRV_ETHPHY_OBJECT_KSZ8081,
    .resetFunction          = 0,
    .pMiimObject            = &DRV_MIIM_OBJECT_BASE_Default,
    .pMiimInit              = &drvMiimInitData,
    .miimIndex              = DRV_MIIM_DRIVER_INDEX,

};

/*** GMAC MAC Initialization Data ***/
const TCPIP_MODULE_MAC_PIC32C_CONFIG tcpipMACPIC32CINTInitData =
{ 
	/** QUEUE 0 Intialization**/
		.gmac_queue_config[0].queueEnable	= true,
	.gmac_queue_config[0].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE0,
	.gmac_queue_config[0].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE0,
	.gmac_queue_config[0].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE0,
	.gmac_queue_config[0].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE0,
	.gmac_queue_config[0].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE0,
	.gmac_queue_config[0].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE0,
	.gmac_queue_config[0].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE0,

	/** QUEUE 1 Intialization**/
		.gmac_queue_config[1].queueEnable	= false,	
	.gmac_queue_config[1].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE1,
	.gmac_queue_config[1].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE1,
	.gmac_queue_config[1].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE1,
	.gmac_queue_config[1].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE1,
	.gmac_queue_config[1].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE1,
	.gmac_queue_config[1].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE1,
	.gmac_queue_config[1].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE1,

	/** QUEUE 2 Intialization**/
		.gmac_queue_config[2].queueEnable	= false,	
	.gmac_queue_config[2].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE2,
	.gmac_queue_config[2].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE2,
	.gmac_queue_config[2].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE2,
	.gmac_queue_config[2].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE2,
	.gmac_queue_config[2].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE2,
	.gmac_queue_config[2].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE2,
	.gmac_queue_config[2].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE2,

	/** QUEUE 3 Intialization**/
		.gmac_queue_config[3].queueEnable	= false,	
	.gmac_queue_config[3].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE3,
	.gmac_queue_config[3].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE3,
	.gmac_queue_config[3].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE3,
	.gmac_queue_config[3].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE3,
	.gmac_queue_config[3].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE3,
	.gmac_queue_config[3].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE3,
	.gmac_queue_config[3].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE3,

	/** QUEUE 4 Intialization**/
		.gmac_queue_config[4].queueEnable	= false,	
	.gmac_queue_config[4].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE4,
	.gmac_queue_config[4].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE4,
	.gmac_queue_config[4].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE4,
	.gmac_queue_config[4].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE4,
	.gmac_queue_config[4].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE4,
	.gmac_queue_config[4].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE4,
	.gmac_queue_config[4].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE4,

	/** QUEUE 5 Intialization**/
	.gmac_queue_config[5].queueEnable	= false,	
	.gmac_queue_config[5].nRxDescCnt	= TCPIP_GMAC_RX_DESCRIPTORS_COUNT_QUE5,
	.gmac_queue_config[5].nTxDescCnt	= TCPIP_GMAC_TX_DESCRIPTORS_COUNT_QUE5,
	.gmac_queue_config[5].rxBufferSize	= TCPIP_GMAC_RX_BUFF_SIZE_QUE5,
	.gmac_queue_config[5].txBufferSize	= TCPIP_GMAC_TX_BUFF_SIZE_QUE5,
	.gmac_queue_config[5].nRxBuffCount	= TCPIP_GMAC_RX_BUFF_COUNT_QUE5,
	.gmac_queue_config[5].nRxBuffCntThres	= TCPIP_GMAC_RX_BUFF_COUNT_THRESHOLD_QUE5,
	.gmac_queue_config[5].nRxBuffAllocCnt	= TCPIP_GMAC_RX_BUFF_ALLOC_COUNT_QUE5,
	.ethFlags               = TCPIP_GMAC_ETH_OPEN_FLAGS,	
	.linkInitDelay          = TCPIP_INTMAC_PHY_LINK_INIT_DELAY,
    .ethModuleId            = TCPIP_INTMAC_MODULE_ID,
    .pPhyBase               = &DRV_ETHPHY_OBJECT_BASE_Default,
    .pPhyInit               = &tcpipPhyInitData,
};











/*** DNS Client Initialization Data ***/
const TCPIP_DNS_CLIENT_MODULE_CONFIG tcpipDNSClientInitData =
{
    .deleteOldLease         = TCPIP_DNS_CLIENT_DELETE_OLD_ENTRIES,
    .cacheEntries           = TCPIP_DNS_CLIENT_CACHE_ENTRIES,
    .entrySolvedTmo         = TCPIP_DNS_CLIENT_CACHE_ENTRY_TMO,    
    .nIPv4Entries  = TCPIP_DNS_CLIENT_CACHE_PER_IPV4_ADDRESS,
    .ipAddressType       = TCPIP_DNS_CLIENT_ADDRESS_TYPE,
    .nIPv6Entries  = TCPIP_DNS_CLIENT_CACHE_PER_IPV6_ADDRESS,
};




TCPIP_STACK_HEAP_INTERNAL_CONFIG tcpipHeapConfig =
{
    .heapType = TCPIP_STACK_HEAP_TYPE_INTERNAL_HEAP,
    .heapFlags = TCPIP_STACK_HEAP_USE_FLAGS,
    .heapUsage = TCPIP_STACK_HEAP_USAGE_CONFIG,
    .malloc_fnc = TCPIP_STACK_MALLOC_FUNC,
    .calloc_fnc = TCPIP_STACK_CALLOC_FUNC,
    .free_fnc = TCPIP_STACK_FREE_FUNC,
    .heapSize = TCPIP_STACK_DRAM_SIZE,
};


const TCPIP_NETWORK_CONFIG __attribute__((unused))  TCPIP_HOSTS_CONFIGURATION[] =
{
	/*** Network Configuration Index 0 ***/
    {
        TCPIP_NETWORK_DEFAULT_INTERFACE_NAME_IDX0,       // interface
        TCPIP_NETWORK_DEFAULT_HOST_NAME_IDX0,            // hostName
        TCPIP_NETWORK_DEFAULT_MAC_ADDR_IDX0,             // macAddr
        TCPIP_NETWORK_DEFAULT_IP_ADDRESS_IDX0,           // ipAddr
        TCPIP_NETWORK_DEFAULT_IP_MASK_IDX0,              // ipMask
        TCPIP_NETWORK_DEFAULT_GATEWAY_IDX0,              // gateway
        TCPIP_NETWORK_DEFAULT_DNS_IDX0,                  // priDNS
        TCPIP_NETWORK_DEFAULT_SECOND_DNS_IDX0,           // secondDNS
        TCPIP_NETWORK_DEFAULT_POWER_MODE_IDX0,           // powerMode
        TCPIP_NETWORK_DEFAULT_INTERFACE_FLAGS_IDX0,      // startFlags
       &TCPIP_NETWORK_DEFAULT_MAC_DRIVER_IDX0,           // pMacObject
    },
};

const size_t TCPIP_HOSTS_CONFIGURATION_SIZE = sizeof (TCPIP_HOSTS_CONFIGURATION) / sizeof (*TCPIP_HOSTS_CONFIGURATION);

const TCPIP_STACK_MODULE_CONFIG TCPIP_STACK_MODULE_CONFIG_TBL [] =
{
    {TCPIP_MODULE_IPV4,             0},

    {TCPIP_MODULE_ICMP,             0},                             // TCPIP_MODULE_ICMP

    {TCPIP_MODULE_ARP,              &tcpipARPInitData},             // TCPIP_MODULE_ARP
    {TCPIP_MODULE_UDP,              &tcpipUDPInitData},             // TCPIP_MODULE_UDP
    {TCPIP_MODULE_TCP,              &tcpipTCPInitData},             // TCPIP_MODULE_TCP
    {TCPIP_MODULE_DHCP_CLIENT,      &tcpipDHCPInitData},            // TCPIP_MODULE_DHCP_CLIENT
    {TCPIP_MODULE_ANNOUNCE,         &tcpipAnnounceInitData},        // TCPIP_MODULE_ANNOUNCE
    {TCPIP_MODULE_DNS_CLIENT,       &tcpipDNSClientInitData},       // TCPIP_MODULE_DNS_CLIENT
    {TCPIP_MODULE_NBNS,             &tcpipNBNSInitData},            // TCPIP_MODULE_NBNS

    { TCPIP_MODULE_MANAGER,         &tcpipHeapConfig },             // TCPIP_MODULE_MANAGER

// MAC modules
    {TCPIP_MODULE_MAC_PIC32C,     &tcpipMACPIC32CINTInitData},     // TCPIP_MODULE_MAC_PIC32C

};

const size_t TCPIP_STACK_MODULE_CONFIG_TBL_SIZE = sizeof (TCPIP_STACK_MODULE_CONFIG_TBL) / sizeof (*TCPIP_STACK_MODULE_CONFIG_TBL);
/*********************************************************************
 * Function:        SYS_MODULE_OBJ TCPIP_STACK_Init()
 *
 * PreCondition:    None
 *
 * Input:
 *
 * Output:          valid system module object if Stack and its componets are initialized
 *                  SYS_MODULE_OBJ_INVALID otherwise
 *
 * Overview:        The function starts the initialization of the stack.
 *                  If an error occurs, the SYS_ERROR() is called
 *                  and the function de-initialize itself and will return false.
 *
 * Side Effects:    None
 *
 * Note:            This function must be called before any of the
 *                  stack or its component routines are used.
 *
 ********************************************************************/


SYS_MODULE_OBJ TCPIP_STACK_Init()
{
    TCPIP_STACK_INIT    tcpipInit;

    tcpipInit.pNetConf = TCPIP_HOSTS_CONFIGURATION;
    tcpipInit.nNets = TCPIP_HOSTS_CONFIGURATION_SIZE;
    tcpipInit.pModConfig = TCPIP_STACK_MODULE_CONFIG_TBL;
    tcpipInit.nModules = TCPIP_STACK_MODULE_CONFIG_TBL_SIZE;
    tcpipInit.initCback = 0;

    return TCPIP_STACK_Initialize(0, &tcpipInit.moduleInit);
}
// </editor-fold>



// *****************************************************************************
// *****************************************************************************
// Section: System Initialization
// *****************************************************************************
// *****************************************************************************
// <editor-fold defaultstate="collapsed" desc="SYS_TIME Initialization Data">

const SYS_TIME_PLIB_INTERFACE sysTimePlibAPI = {
    .timerCallbackSet = (SYS_TIME_PLIB_CALLBACK_REGISTER)TC0_CH0_TimerCallbackRegister,
    .timerCounterGet = (SYS_TIME_PLIB_COUNTER_GET)TC0_CH0_TimerCounterGet,
    .timerPeriodSet = (SYS_TIME_PLIB_PERIOD_SET)TC0_CH0_TimerPeriodSet,
    .timerFrequencyGet = (SYS_TIME_PLIB_FREQUENCY_GET)TC0_CH0_TimerFrequencyGet,
    .timerCompareSet = (SYS_TIME_PLIB_COMPARE_SET)TC0_CH0_TimerCompareSet,
    .timerStart = (SYS_TIME_PLIB_START)TC0_CH0_TimerStart,
    .timerStop = (SYS_TIME_PLIB_STOP)TC0_CH0_TimerStop 
};

const SYS_TIME_INIT sysTimeInitData =
{
    .timePlib = &sysTimePlibAPI,
    .hwTimerIntNum = TC0_IRQn,
};

// </editor-fold>
// <editor-fold defaultstate="collapsed" desc="SYS_CONSOLE Instance 0 Initialization Data">

static QElement sysConsole0UARTRdQueueElements[SYS_CONSOLE_UART_RD_QUEUE_DEPTH_IDX0];
static QElement sysConsole0UARTWrQueueElements[SYS_CONSOLE_UART_WR_QUEUE_DEPTH_IDX0];

/* Declared in console device implementation (sys_console_uart.c) */
extern const SYS_CONSOLE_DEV_DESC sysConsoleUARTDevDesc;

const SYS_CONSOLE_UART_PLIB_INTERFACE sysConsole0UARTPlibAPI =
{
    .read = (SYS_CONSOLE_UART_PLIB_READ)UART1_Read,
    .write = (SYS_CONSOLE_UART_PLIB_WRITE)UART1_Write,
    .readCallbackRegister = (SYS_CONSOLE_UART_PLIB_REGISTER_CALLBACK_READ)UART1_ReadCallbackRegister,
    .writeCallbackRegister = (SYS_CONSOLE_UART_PLIB_REGISTER_CALLBACK_WRITE)UART1_WriteCallbackRegister,
    .errorGet = (SYS_CONSOLE_UART_PLIB_ERROR_GET)UART1_ErrorGet,
};


const SYS_CONSOLE_UART_INTERRUPT_SOURCES sysConsole0UARTInterruptSources =
{
    /* Peripheral has single interrupt vector */
    .isSingleIntSrc                        = true,

    /* Peripheral interrupt line */
    .intSources.usartInterrupt             = UART1_IRQn,
};

const SYS_CONSOLE_UART_INIT_DATA sysConsole0UARTInitData =
{
    .uartPLIB = &sysConsole0UARTPlibAPI,
    .readQueueElementsArr = sysConsole0UARTRdQueueElements,
    .writeQueueElementsArr = sysConsole0UARTWrQueueElements,
    .readQueueDepth = SYS_CONSOLE_UART_RD_QUEUE_DEPTH_IDX0,
    .writeQueueDepth = SYS_CONSOLE_UART_WR_QUEUE_DEPTH_IDX0,
    .interruptSources = &sysConsole0UARTInterruptSources,
};

const SYS_CONSOLE_INIT sysConsole0Init =
{
    .deviceInitData = (const void*)&sysConsole0UARTInitData,
    .consDevDesc = &sysConsoleUARTDevDesc,
    .deviceIndex = 0,
};

// </editor-fold>


const SYS_CMD_INIT sysCmdInit =
{
    .moduleInit = {0},
    .consoleCmdIOParam = SYS_CMD_SINGLE_CHARACTER_READ_CONSOLE_IO_PARAM,
	.consoleIndex = 0,
};


const SYS_DEBUG_INIT debugInit =
{
    .moduleInit = {0},
    .errorLevel = SYS_DEBUG_GLOBAL_ERROR_LEVEL,
    .consoleIndex = 0,
};





/*******************************************************************************
  Function:
    void SYS_Initialize ( void *data )

  Summary:
    Initializes the board, services, drivers, application and other modules.

  Remarks:
 */

void SYS_Initialize ( void* data )
{
  
    CLK_Initialize();
	PIO_Initialize();

	PIT_TimerInitialize();

  

 
    TC0_CH0_TimerInitialize(); 
     
    
	BSP_Initialize();
	UART1_Initialize();

    MMU_Initialize();
    Matrix_Initialize();

    INT_Initialize();
    
	WDT_REGS->WDT_MR = WDT_MR_WDDIS_Msk; 		// Disable WDT 



    /* Initialize the MIIM Driver */
    sysObj.drvMiim = DRV_MIIM_Initialize( DRV_MIIM_INDEX_0, (const SYS_MODULE_INIT *) &drvMiimInitData );


    sysObj.sysTime = SYS_TIME_Initialize(SYS_TIME_INDEX_0, (SYS_MODULE_INIT *)&sysTimeInitData);
    sysObj.sysConsole0 = SYS_CONSOLE_Initialize(SYS_CONSOLE_INDEX_0, (SYS_MODULE_INIT *)&sysConsole0Init);

    SYS_CMD_Initialize((SYS_MODULE_INIT*)&sysCmdInit);

    sysObj.sysDebug = SYS_DEBUG_Initialize(SYS_DEBUG_INDEX_0, (SYS_MODULE_INIT*)&debugInit);




    /* TCPIP Stack Initialization */
    sysObj.tcpip = TCPIP_STACK_Init();
    SYS_ASSERT(sysObj.tcpip != SYS_MODULE_OBJ_INVALID, "TCPIP_STACK_Init Failed" );



    APP_Initialize();



}


/*******************************************************************************
 End of File
*/
