"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
*****************************************************************************"""

def instantiateComponent(tcpipHttpNetComponent):
    import re
    import os
    import sys
    configName = Variables.get("__CONFIGURATION_NAME")
    # Enable HTTP NET Server
    tcpipHttpNetSrv = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_STACK_USE_HTTP_NET_SERVER", None)
    tcpipHttpNetSrv.setLabel("HTTP NET Server")
    tcpipHttpNetSrv.setVisible(False)
    tcpipHttpNetSrv.setDescription("Enable HTTP NET Server")
    tcpipHttpNetSrv.setDefaultValue(True)
    # H3_ToDo  
        # select USE_SYS_FS_NEEDED
        # select NET_PRES_NEEDED
        # select USE_CRYPTO_LIB_NEEDED
        # select USE_CRYPTO_MD5_NEEDED
        # select USE_CRYPTO_RANDOM_NEEDED
    #tcpipHttpNetSrv.setDependencies(tcpipHttpNetSrvVisible, ["tcpipHttp.TCPIP_STACK_USE_HTTP_SERVER" , "tcpipTcp.TCPIP_USE_TCP"]) # H3_ToDo to verify the dependency function

    # Maximum Header Length
    tcpipHttpNetHdrLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_MAX_HEADER_LEN", None)
    tcpipHttpNetHdrLenMax.setLabel("Max Header Length")
    tcpipHttpNetHdrLenMax.setVisible(True)
    tcpipHttpNetHdrLenMax.setDescription("Maximum Header Length")
    tcpipHttpNetHdrLenMax.setDefaultValue(15)
    #tcpipHttpNetHdrLenMax.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Maximum Lifetime of Static Responses in Seconds
    tcpipHttpNetCacheLen = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_CACHE_LEN", None)
    tcpipHttpNetCacheLen.setLabel("Max Lifetime of Static Responses in Seconds")
    tcpipHttpNetCacheLen.setVisible(True)
    tcpipHttpNetCacheLen.setDescription("Maximum Lifetime of Static Responses in Seconds")
    tcpipHttpNetCacheLen.setDefaultValue("600")
    #tcpipHttpNetCacheLen.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Socket Disconnect Time-out
    tcpipHttpNetTimeout = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_TIMEOUT", None)
    tcpipHttpNetTimeout.setLabel("Socket Disconnect Time-out")
    tcpipHttpNetTimeout.setVisible(True)
    tcpipHttpNetTimeout.setDescription("Socket Disconnect Time-out")
    tcpipHttpNetTimeout.setDefaultValue(45)
    #tcpipHttpNetTimeout.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Maximum Number of Simultaneous Connections
    tcpipHttpNetConnMaxNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_MAX_CONNECTIONS", None)
    tcpipHttpNetConnMaxNum.setLabel("Max Number of Simultaneous Connections")
    tcpipHttpNetConnMaxNum.setVisible(True)
    tcpipHttpNetConnMaxNum.setDescription("Maximum Number of Simultaneous Connections")
    tcpipHttpNetConnMaxNum.setDefaultValue(4)
    #tcpipHttpNetConnMaxNum.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Default HTTP NET File
    tcpipHttpNetDefaultFile = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_DEFAULT_FILE", None)
    tcpipHttpNetDefaultFile.setLabel("Default HTTP NET File")
    tcpipHttpNetDefaultFile.setVisible(True)
    tcpipHttpNetDefaultFile.setDescription("Default HTTP NET File")
    tcpipHttpNetDefaultFile.setDefaultValue("index.htm")
    #tcpipHttpNetDefaultFile.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Maximum Size of a HTTP File Name
    tcpipHttpNetFilenameLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_FILENAME_MAX_LEN", None)
    tcpipHttpNetFilenameLenMax.setLabel("Maximum Size of a HTTP File Name")
    tcpipHttpNetFilenameLenMax.setVisible(True)
    tcpipHttpNetFilenameLenMax.setDescription("Maximum Size of a HTTP File Name")
    tcpipHttpNetFilenameLenMax.setDefaultValue(25)
    #tcpipHttpNetFilenameLenMax.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Default Web pages directory
    tcpipHttpNetWebDir = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_WEB_DIR", None)
    tcpipHttpNetWebDir.setLabel("Web Pages Directory")
    tcpipHttpNetWebDir.setVisible(True)
    tcpipHttpNetWebDir.setDescription("Web Pages Directory")
    tcpipHttpNetWebDir.setDefaultValue("/mnt/mchpSite1/")
    #tcpipHttpNetWebDir.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Enable MPFS Update via HTTP NET
    tcpipHttpNetFileUpload = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE", None)
    tcpipHttpNetFileUpload.setLabel("Enable MPFS Update via HTTP NET")
    tcpipHttpNetFileUpload.setVisible(True)
    tcpipHttpNetFileUpload.setDescription("Enable MPFS Update via HTTP NET")
    tcpipHttpNetFileUpload.setDefaultValue(False)
    #tcpipHttpNetFileUpload.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # MPFS Upload Page Name
    tcpipHttpNetFileUploadName = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_FILE_UPLOAD_NAME", tcpipHttpNetFileUpload)
    tcpipHttpNetFileUploadName.setLabel("MPFS Upload Page Name")
    tcpipHttpNetFileUploadName.setVisible(False)
    tcpipHttpNetFileUploadName.setDescription("MPFS Upload Page Name")
    tcpipHttpNetFileUploadName.setDefaultValue("mpfsupload")
    tcpipHttpNetFileUploadName.setDependencies(tcpipHttpNetFileUploadVisible, ["TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE"])
    
    # MPFS NVM Mount Path
    tcpipHttpNetMpfsNvmMountPath = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_MPFS_NVM_PATH", tcpipHttpNetFileUpload)
    tcpipHttpNetMpfsNvmMountPath.setLabel("MPFS NVM Mount Path")
    tcpipHttpNetMpfsNvmMountPath.setVisible(False)
    tcpipHttpNetMpfsNvmMountPath.setDescription("MPFS NVM Mount Path")
    tcpipHttpNetMpfsNvmMountPath.setDefaultValue("/mnt/mchpSite1")
    tcpipHttpNetMpfsNvmMountPath.setDependencies(tcpipHttpNetFileUploadVisible, ["TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE"])
    
    # MPFS NVM Disk Path
    tcpipHttpNetMpfsNvmDiskPath = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_MPFS_NVM_VOL", tcpipHttpNetFileUpload)
    tcpipHttpNetMpfsNvmDiskPath.setLabel("MPFS NVM Disk Path")
    tcpipHttpNetMpfsNvmDiskPath.setVisible(False)
    tcpipHttpNetMpfsNvmDiskPath.setDescription("MPFS NVM Disk Path")
    tcpipHttpNetMpfsNvmDiskPath.setDefaultValue("/dev/nvma1")    
    tcpipHttpNetMpfsNvmDiskPath.setDependencies(tcpipHttpNetFileUploadVisible, ["TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE"])   
    
    # MPFS NVM Disk Number
    tcpipHttpNetMpfsNvmDiskNum= tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_MPFS_NVM_NUM", tcpipHttpNetFileUpload)
    tcpipHttpNetMpfsNvmDiskNum.setLabel("MPFS NVM Disk Number")
    tcpipHttpNetMpfsNvmDiskNum.setVisible(False)
    tcpipHttpNetMpfsNvmDiskNum.setDescription("MPFS NVM Disk Number")
    tcpipHttpNetMpfsNvmDiskNum.setDefaultValue(0)    
    tcpipHttpNetMpfsNvmDiskNum.setDependencies(tcpipHttpNetFileUploadVisible, ["TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE"])   
    
    # Enable POST Support
    tcpipHttpNetPostSupport = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_USE_POST", None)
    tcpipHttpNetPostSupport.setLabel("Enable POST Support")
    tcpipHttpNetPostSupport.setVisible(True)
    tcpipHttpNetPostSupport.setDescription("Enable POST Support")
    tcpipHttpNetPostSupport.setDefaultValue(True)
    #tcpipHttpNetPostSupport.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Enable Cookie Support
    tcpipHttpNetCookieSupport = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_USE_COOKIES", None)
    tcpipHttpNetCookieSupport.setLabel("Enable Cookie Support")
    tcpipHttpNetCookieSupport.setVisible(True)
    tcpipHttpNetCookieSupport.setDescription("Enable Cookie Support")
    tcpipHttpNetCookieSupport.setDefaultValue(True)
    #tcpipHttpNetCookieSupport.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Use Base 64 Decode
    tcpipHttpNetBase64Decode = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_USE_BASE64_DECODE", None)
    tcpipHttpNetBase64Decode.setLabel("Use Base 64 Decode")
    tcpipHttpNetBase64Decode.setVisible(True)
    tcpipHttpNetBase64Decode.setDescription("Use Base 64 Decode")
    tcpipHttpNetBase64Decode.setDefaultValue(False) 


    # Enable Basic Authentication Support
    tcpipHttpNetAuth = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_USE_AUTHENTICATION", None)
    tcpipHttpNetAuth.setLabel("Enable Basic Authentication Support")
    tcpipHttpNetAuth.setVisible(True)
    tcpipHttpNetAuth.setDescription("Enable Basic Authentication Support")
    tcpipHttpNetAuth.setDefaultValue(True)
    tcpipHttpNetBase64Decode.setDependencies(tcpipHttpNetBase64DecodeOpt, ["TCPIP_HTTP_NET_USE_AUTHENTICATION"])


    # Maximum Data Length (bytes) for Reading Cookie and GET/POST Arguments
    tcpipHttpNetDataLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_MAX_DATA_LEN", None)
    tcpipHttpNetDataLenMax.setLabel("Max Data Length (bytes) for Reading Cookie and GET/POST Arguments")
    tcpipHttpNetDataLenMax.setVisible(True)
    tcpipHttpNetDataLenMax.setDescription("Maximum Data Length (bytes) for Reading Cookie and GET/POST Arguments")
    tcpipHttpNetDataLenMax.setDefaultValue(100)
    #tcpipHttpNetDataLenMax.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET Socket TX Buffer Size
    tcpipHttpNetSktTxBuffsize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SKT_TX_BUFF_SIZE", None)
    tcpipHttpNetSktTxBuffsize.setLabel("HTTP NET Socket TX Buffer Size")
    tcpipHttpNetSktTxBuffsize.setVisible(True)
    tcpipHttpNetSktTxBuffsize.setDescription("HTTP NET Socket TX Buffer Size")
    tcpipHttpNetSktTxBuffsize.setDefaultValue(1024)
    #tcpipHttpNetSktTxBuffsize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET Socket RX Buffer Size
    tcpipHttpNetSktRxBuffsize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SKT_RX_BUFF_SIZE", None)
    tcpipHttpNetSktRxBuffsize.setLabel("HTTP NET Socket RX Buffer Size")
    tcpipHttpNetSktRxBuffsize.setVisible(True)
    tcpipHttpNetSktRxBuffsize.setDescription("HTTP NET Socket RX Buffer Size")
    tcpipHttpNetSktRxBuffsize.setDefaultValue(1024)
    #tcpipHttpNetSktRxBuffsize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET Listening Port
    tcpipHttpNetListenPort = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_LISTEN_PORT", None)
    tcpipHttpNetListenPort.setLabel("HTTP NET Listening Port")
    tcpipHttpNetListenPort.setVisible(True)
    tcpipHttpNetListenPort.setDescription("HTTP NET Listening Port")
    tcpipHttpNetListenPort.setDefaultValue(80)
    #tcpipHttpNetListenPort.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET Configuration Flags Settings
    tcpipHttpNetConfigFlag = tcpipHttpNetComponent.createMenuSymbol(None, None)
    tcpipHttpNetConfigFlag.setLabel("HTTP NET Configuration Flags")
    tcpipHttpNetConfigFlag.setVisible(True)
    tcpipHttpNetConfigFlag.setDescription("HTTP NET Configuration Flags Settings")
    #tcpipHttpNetConfigFlag.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Use non-persistent connections
    tcpipHttpNetConfigFlagNonpersistent = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CONFIG_FLAG_NON_PERSISTENT", tcpipHttpNetConfigFlag)
    tcpipHttpNetConfigFlagNonpersistent.setLabel("Use non-persistent connections")
    tcpipHttpNetConfigFlagNonpersistent.setVisible(True)
    tcpipHttpNetConfigFlagNonpersistent.setDescription("Use non-persistent connections")
    tcpipHttpNetConfigFlagNonpersistent.setDefaultValue(False)
    #tcpipHttpNetConfigFlagNonpersistent.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP sockets created with NO-DELAY option
    tcpipHttpNetConfigFlagNoDly = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CONFIG_FLAG_NO_DELAY", tcpipHttpNetConfigFlag)
    tcpipHttpNetConfigFlagNoDly.setLabel("HTTP sockets created with NO-DELAY option")
    tcpipHttpNetConfigFlagNoDly.setVisible(True)
    tcpipHttpNetConfigFlagNoDly.setDescription("HTTP sockets created with NO-DELAY option")
    tcpipHttpNetConfigFlagNoDly.setDefaultValue(False)
    #tcpipHttpNetConfigFlagNoDly.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # All HTTP connections have to be secure
    tcpipHttpNetConfigFlagSecureOn = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_ON", tcpipHttpNetConfigFlag)
    tcpipHttpNetConfigFlagSecureOn.setLabel("All HTTP connections have to be secure")
    tcpipHttpNetConfigFlagSecureOn.setVisible(False)
    tcpipHttpNetConfigFlagSecureOn.setDescription("All HTTP connections have to be secure")
    tcpipHttpNetConfigFlagSecureOn.setDefaultValue(False)

    # All HTTP connections have to be non-secure
    tcpipHttpNetConfigFlagSecureOff = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_OFF", tcpipHttpNetConfigFlag)
    tcpipHttpNetConfigFlagSecureOff.setLabel("All HTTP connections have to be non-secure")
    tcpipHttpNetConfigFlagSecureOff.setVisible(False)
    tcpipHttpNetConfigFlagSecureOff.setDescription("All HTTP connections have to be non-secure")
    tcpipHttpNetConfigFlagSecureOff.setDefaultValue(False)

    # HTTP security is based on the port numbers
    tcpipHttpNetConfigFlagSecureDefault = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_DEFAULT", tcpipHttpNetConfigFlag)
    tcpipHttpNetConfigFlagSecureDefault.setLabel("HTTP security is based on the port numbers")
    tcpipHttpNetConfigFlagSecureDefault.setVisible(True)
    tcpipHttpNetConfigFlagSecureDefault.setDescription("HTTP security is based on the port numbers")
    tcpipHttpNetConfigFlagSecureDefault.setDefaultValue(True)

    tcpipHttpNetConfigFlagSecureDefault.setDependencies(tcpipHttpNetSrvConfigFlagSecureDefaultEnable, ["TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_OFF", "TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_ON"])
    tcpipHttpNetConfigFlagSecureOn.setDependencies(tcpipHttpNetSrvConfigFlagSecureOnEnable, ["TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_OFF", "TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_DEFAULT"])
    tcpipHttpNetConfigFlagSecureOff.setDependencies(tcpipHttpNetSrvConfigFlagSecureOffEnable, ["TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_ON", "TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_DEFAULT"])

    # HTTP NET Task Rate - ms
    tcpipHttpNetTskRate = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_TASK_RATE", None)
    tcpipHttpNetTskRate.setLabel("HTTP NET Task Rate - ms")
    tcpipHttpNetTskRate.setVisible(True)
    tcpipHttpNetTskRate.setDescription("HTTP NET Task Rate - ms")
    tcpipHttpNetTskRate.setDefaultValue(33)
    #tcpipHttpNetTskRate.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Size of the Buffer Used for Sending Response Messages to the Client
    tcpipHttpNetRespBuffSize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_RESPONSE_BUFFER_SIZE", None)
    tcpipHttpNetRespBuffSize.setLabel("Size of the Buffer Used for Sending Response Messages to the Client")
    tcpipHttpNetRespBuffSize.setVisible(True)
    tcpipHttpNetRespBuffSize.setDescription("Size of the Buffer Used for Sending Response Messages to the Client")
    tcpipHttpNetRespBuffSize.setDefaultValue(300)
    #tcpipHttpNetRespBuffSize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Size of the Buffer Used for Sending Cookies to the Client
    tcpipHttpNetCookieBuffSize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_COOKIE_BUFFER_SIZE", None)
    tcpipHttpNetCookieBuffSize.setLabel("Size of the Buffer Used for Sending Cookies to the Client")
    tcpipHttpNetCookieBuffSize.setVisible(True)
    tcpipHttpNetCookieBuffSize.setDescription("Size of the Buffer Used for Sending Cookies to the Client")
    tcpipHttpNetCookieBuffSize.setDefaultValue(200)
    #tcpipHttpNetCookieBuffSize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Size of the Peek Buffer for Performing Searches
    tcpipHttpNetFindPeekBuffSize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_FIND_PEEK_BUFF_SIZE", None)
    tcpipHttpNetFindPeekBuffSize.setLabel("Size of the Peek Buffer for Performing Searches")
    tcpipHttpNetFindPeekBuffSize.setVisible(True)
    tcpipHttpNetFindPeekBuffSize.setDescription("Size of the Peek Buffer for Performing Searches")
    tcpipHttpNetFindPeekBuffSize.setDefaultValue(512)
    #tcpipHttpNetFindPeekBuffSize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Size of the Buffer for Processing HTML, Dynamic Variable and Binary Files
    tcpipHttpNetFileProcessBuffSize = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_FILE_PROCESS_BUFFER_SIZE", None)
    tcpipHttpNetFileProcessBuffSize.setLabel("Size of the Buffer for Processing HTML, Dynamic Variable and Binary Files")
    tcpipHttpNetFileProcessBuffSize.setVisible(True)
    tcpipHttpNetFileProcessBuffSize.setDescription("Size of the Buffer for Processing HTML, Dynamic Variable and Binary Files")
    tcpipHttpNetFileProcessBuffSize.setDefaultValue(512)
    #tcpipHttpNetFileProcessBuffSize.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Number of File Buffers to be Created
    tcpipHttpNetFileProcessBuffNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_FILE_PROCESS_BUFFERS_NUMBER", None)
    tcpipHttpNetFileProcessBuffNum.setLabel("Number of File Buffers to be Created")
    tcpipHttpNetFileProcessBuffNum.setVisible(True)
    tcpipHttpNetFileProcessBuffNum.setDescription("Number of File Buffers to be Created")
    tcpipHttpNetFileProcessBuffNum.setDefaultValue(4)
    #tcpipHttpNetFileProcessBuffNum.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Retry Limit for Allocating a File Buffer from the Pool
    tcpipHttpNetFileProcessBuffRetry = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_FILE_PROCESS_BUFFER_RETRIES", None)
    tcpipHttpNetFileProcessBuffRetry.setLabel("Retry Limit for Allocating a File Buffer from the Pool")
    tcpipHttpNetFileProcessBuffRetry.setVisible(True)
    tcpipHttpNetFileProcessBuffRetry.setDescription("Retry Limit for Allocating a File Buffer from the Pool")
    tcpipHttpNetFileProcessBuffRetry.setDefaultValue(10)
    #tcpipHttpNetFileProcessBuffRetry.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Retry Limit for Allocating a File Buffer from the Pool
    tcpipHttpNetChunksNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_CHUNKS_NUMBER", None)
    tcpipHttpNetChunksNum.setLabel("Number of Chunks to be Created")
    tcpipHttpNetChunksNum.setVisible(True)
    tcpipHttpNetChunksNum.setDescription("Number of Chunks to be Created")
    tcpipHttpNetChunksNum.setDefaultValue(10)
    #tcpipHttpNetChunksNum.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Retry Limit for Allocating a Chunk from the Pool
    tcpipHttpNetChunkRetry = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_CHUNK_RETRIES", None)
    tcpipHttpNetChunkRetry.setLabel("Retry Limit for Allocating a Chunk from the Pool")
    tcpipHttpNetChunkRetry.setVisible(True)
    tcpipHttpNetChunkRetry.setDescription("Retry Limit for Allocating a Chunk from the Pool")
    tcpipHttpNetChunkRetry.setDefaultValue(10)
    #tcpipHttpNetChunkRetry.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # The Maximum Depth of Recursive Calls for Serving a Web Page
    tcpipHttpNetRecursiveLvl = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_MAX_RECURSE_LEVEL", None)
    tcpipHttpNetRecursiveLvl.setLabel("The Maximum Depth of Recursive Calls for Serving a Web Page")
    tcpipHttpNetRecursiveLvl.setVisible(True)
    tcpipHttpNetRecursiveLvl.setDescription("The Maximum Depth of Recursive Calls for Serving a Web Page")
    tcpipHttpNetRecursiveLvl.setDefaultValue(3)
    #tcpipHttpNetRecursiveLvl.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Enable the Processing of Dynamic Variables
    tcpipHttpNetDynVarProc = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_DYNVAR_PROCESS", None)
    tcpipHttpNetDynVarProc.setLabel("Enable the Processing of Dynamic Variables")
    tcpipHttpNetDynVarProc.setVisible(True)
    tcpipHttpNetDynVarProc.setDescription("Enable the Processing of Dynamic Variables")
    tcpipHttpNetDynVarProc.setDefaultValue(True)
    #tcpipHttpNetDynVarProc.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Number of the Descriptors for Dynamic Variables Processing
    tcpipHttpNetDynVarDescNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_DYNVAR_DESCRIPTORS_NUMBER", tcpipHttpNetDynVarProc)
    tcpipHttpNetDynVarDescNum.setLabel("Number of the Descriptors for Dynamic Variables Processing")
    tcpipHttpNetDynVarDescNum.setVisible(True)
    tcpipHttpNetDynVarDescNum.setDescription("Number of the Descriptors for Dynamic Variables Processing")
    tcpipHttpNetDynVarDescNum.setDefaultValue(10)
    tcpipHttpNetDynVarDescNum.setDependencies(tcpipHttpNetDynVarVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_DYNVAR_PROCESS"])

    # Maximum Size for a Complete Dynamic Variable: Name + Args
    tcpipHttpNetDynVarLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_DYNVAR_MAX_LEN", tcpipHttpNetDynVarProc)
    tcpipHttpNetDynVarLenMax.setLabel("Maximum Size for a Complete Dynamic Variable: Name + Args")
    tcpipHttpNetDynVarLenMax.setVisible(True)
    tcpipHttpNetDynVarLenMax.setDescription("Maximum Size for a Complete Dynamic Variable: Name + Args")
    tcpipHttpNetDynVarLenMax.setDefaultValue(50)
    tcpipHttpNetDynVarLenMax.setDependencies(tcpipHttpNetDynVarVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_DYNVAR_PROCESS"])

    # Maximum Number of Arguments for a Dynamic Variable
    tcpipHttpNetDynVarArgNumMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_DYNVAR_ARG_MAX_NUMBER", tcpipHttpNetDynVarProc)
    tcpipHttpNetDynVarArgNumMax.setLabel("Maximum Number of Arguments for a Dynamic Variable")
    tcpipHttpNetDynVarArgNumMax.setVisible(True)
    tcpipHttpNetDynVarArgNumMax.setDescription("Maximum Number of Arguments for a Dynamic Variable")
    tcpipHttpNetDynVarArgNumMax.setDefaultValue(4)
    tcpipHttpNetDynVarArgNumMax.setDependencies(tcpipHttpNetDynVarVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_DYNVAR_PROCESS"])

    # Retry Limit for a Dynamic Variable Processing
    tcpipHttpNetDynVarProcRetry = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_DYNVAR_PROCESS_RETRIES", tcpipHttpNetDynVarProc)
    tcpipHttpNetDynVarProcRetry.setLabel("Retry Limit for a Dynamic Variable Processing")
    tcpipHttpNetDynVarProcRetry.setVisible(True)
    tcpipHttpNetDynVarProcRetry.setDescription("Retry Limit for a Dynamic Variable Processing")
    tcpipHttpNetDynVarProcRetry.setDefaultValue(10)
    tcpipHttpNetDynVarProcRetry.setDependencies(tcpipHttpNetDynVarVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_DYNVAR_PROCESS"])

    # Enable the Processing of SSI Commands
    tcpipHttpNetSsiProc = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_SSI_PROCESS", None)
    tcpipHttpNetSsiProc.setLabel("Enable the Processing of SSI Commands")
    tcpipHttpNetSsiProc.setVisible(True)
    tcpipHttpNetSsiProc.setDescription("Enable the Processing of SSI Commands")
    tcpipHttpNetSsiProc.setDefaultValue(True)
    #tcpipHttpNetSsiProc.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # Maximum Number of Attributes for a SSI Command
    tcpipHttpNetSsiAttrNumMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_ATTRIBUTES_MAX_NUMBER", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiAttrNumMax.setLabel("Maximum Number of Attributes for a SSI Command")
    tcpipHttpNetSsiAttrNumMax.setVisible(True)
    tcpipHttpNetSsiAttrNumMax.setDescription("Maximum Number of Attributes for a SSI Command")
    tcpipHttpNetSsiAttrNumMax.setDefaultValue(4)
    tcpipHttpNetSsiAttrNumMax.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Number of Static Attributes Associated to a SSI Command
    tcpipHttpNetSsiStaticAttrNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_STATIC_ATTTRIB_NUMBER", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiStaticAttrNum.setLabel("Number of Static Attributes Associated to a SSI Command")
    tcpipHttpNetSsiStaticAttrNum.setVisible(False)
    tcpipHttpNetSsiStaticAttrNum.setDescription("Number of Static Attributes Associated to a SSI Command")
    tcpipHttpNetSsiStaticAttrNum.setDefaultValue(2)
    tcpipHttpNetSsiStaticAttrNum.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Maximum Size for a SSI Command Line: Command + Attribute/Value Pairs
    tcpipHttpNetSsiCmdLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_CMD_MAX_LEN", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiCmdLenMax.setLabel("Maximum Size for a SSI Command Line: Command + Attribute/Value Pairs")
    tcpipHttpNetSsiCmdLenMax.setVisible(True)
    tcpipHttpNetSsiCmdLenMax.setDescription("Maximum Size for a SSI Command Line: Command + Attribute/Value Pairs")
    tcpipHttpNetSsiCmdLenMax.setDefaultValue(100)
    tcpipHttpNetSsiCmdLenMax.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Maximum Number of SSI Variables that Can Be Created at Run Time
    tcpipHttpNetSsiVarNum = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_VARIABLES_NUMBER", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiVarNum.setLabel("Maximum Number of SSI Variables that Can Be Created at Run Time")
    tcpipHttpNetSsiVarNum.setVisible(True)
    tcpipHttpNetSsiVarNum.setDescription("Maximum Number of SSI Variables that Can Be Created at Run Time")
    tcpipHttpNetSsiVarNum.setDefaultValue(13)
    tcpipHttpNetSsiVarNum.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Maximum Number of SSI Variables that Can Be Created at Run Time
    tcpipHttpNetSsiVarNameLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_VARIABLE_NAME_MAX_LENGTH", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiVarNameLenMax.setLabel("Maximum Length of a SSI Variable Name")
    tcpipHttpNetSsiVarNameLenMax.setVisible(True)
    tcpipHttpNetSsiVarNameLenMax.setDescription("Maximum Length of a SSI Variable Name")
    tcpipHttpNetSsiVarNameLenMax.setDefaultValue(10)
    tcpipHttpNetSsiVarNameLenMax.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Maximum Size of a SSI String Variable Value
    tcpipHttpNetSsiVarStrLenMax = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_SSI_VARIABLE_STRING_MAX_LENGTH", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiVarStrLenMax.setLabel("Maximum Size of a SSI String Variable Value")
    tcpipHttpNetSsiVarStrLenMax.setVisible(True)
    tcpipHttpNetSsiVarStrLenMax.setDescription("Maximum Size of a SSI String Variable Value")
    tcpipHttpNetSsiVarStrLenMax.setDefaultValue(10)
    tcpipHttpNetSsiVarStrLenMax.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Message to Echo when Echoing a Not Found Variable
    tcpipHttpNetSsiEchoNotFoundMsg = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_SSI_ECHO_NOT_FOUND_MESSAGE", tcpipHttpNetSsiProc)
    tcpipHttpNetSsiEchoNotFoundMsg.setLabel("Message to Echo when Echoing a Not Found Variable")
    tcpipHttpNetSsiEchoNotFoundMsg.setVisible(True)
    tcpipHttpNetSsiEchoNotFoundMsg.setDescription("Message to Echo when Echoing a Not Found Variable")
    tcpipHttpNetSsiEchoNotFoundMsg.setDefaultValue("SSI Echo - Not Found: ")
    tcpipHttpNetSsiEchoNotFoundMsg.setDependencies(tcpipHttpNetSsiAttrVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_SSI_PROCESS"])

    # Include HTTP NET Custom Template
    tcpipHttpNetCustTemplate = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CUSTOM_TEMPLATE", None)
    tcpipHttpNetCustTemplate.setLabel("Include HTTP NET Custom Template")
    tcpipHttpNetCustTemplate.setVisible(True)
    tcpipHttpNetCustTemplate.setDescription("Include HTTP NET Custom Template")
    tcpipHttpNetCustTemplate.setDefaultValue(True)
    #tcpipHttpNetCustTemplate.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])


    # Message to provide the source web page path which will be used for the webpage.py
    tcpipHttpNetWebPageDirPath = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_WEBPAGE_DIRECTORY_PATH", tcpipHttpNetCustTemplate)
    tcpipHttpNetWebPageDirPath.setLabel("Web pages source directory path")
    tcpipHttpNetWebPageDirPath.setVisible(True)
    tcpipHttpNetWebPageDirPath.setDescription("Configure Webpage directory path")
    tcpipHttpNetWebPageDirPath.setDefaultValue(Module.getPath() + "web_pages")
    tcpipHttpNetWebPageDirPath.setDependencies(tcpipHttpNetWebServerPathVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_CUSTOM_TEMPLATE"])

    tcpipHttpNetDestWebPageDirPath = tcpipHttpNetComponent.createKeyValueSetSymbol("TCPIP_HTTP_NET_DEST_WEBPAGE_DIRECTORY_PATH",tcpipHttpNetCustTemplate)
    tcpipHttpNetDestWebPageDirPath.setLabel("Web pages destination directory path")
    tcpipHttpNetDestWebPageDirPath.setVisible(True)
    tcpipHttpNetDestWebPageDirPath.addKey("DESTINATION PATH", "0", Module.getPath() + "apps"+os.path.sep+"<project>"+os.path.sep+"firmware"+os.path.sep+"src"+os.path.sep+"web_pages")
    tcpipHttpNetDestWebPageDirPath.setDisplayMode("Description")
    tcpipHttpNetDestWebPageDirPath.setOutputMode("Key")
    tcpipHttpNetDestWebPageDirPath.setDefaultValue(0)
    tcpipHttpNetDestWebPageDirPath.setReadOnly(True)
    tcpipHttpNetDestWebPageDirPath.setDependencies(tcpipHttpNetWebServerPathVisible, ["TCPIP_STACK_USE_HTTP_NET_SERVER" , "TCPIP_HTTP_NET_CUSTOM_TEMPLATE"])

    # Message that Number of webpage files accepted
    tcpipHttpNetWebPageFileCount = tcpipHttpNetComponent.createCommentSymbol("TCPIP_WEBPAGE_FILES_COUNT_COMMENT", tcpipHttpNetCustTemplate)
    tcpipHttpNetWebPageFileCount.setVisible(True)
    tcpipHttpNetWebPageFileCount.setLabel("*** Maximum 100 web page files currently supported ***")
    
    # Include HTTP NET Custom Template SL
    tcpipHttpNetCustTemplateSl = tcpipHttpNetComponent.createBooleanSymbol("TCPIP_HTTP_NET_CUSTOM_TEMPLATE_SL", None)
    tcpipHttpNetCustTemplateSl.setVisible(False)
    tcpipHttpNetCustTemplateSl.setDescription("Include HTTP NET Custom Template SL")
    tcpipHttpNetCustTemplateSl.setDefaultValue((Database.getSymbolValue("sys_fs", "SYS_FS_MPFS") == True))
    tcpipHttpNetCustTemplateSl.setDependencies(tcpipHttpNetCustomSlSet, ["sys_fs.SYS_FS_MPFS"])

    # Persistent Connection Idle Time-out
    tcpipHttpNetConnTimeout = tcpipHttpNetComponent.createIntegerSymbol("TCPIP_HTTP_NET_CONNECTION_TIMEOUT", None)
    tcpipHttpNetConnTimeout.setLabel("Persistent Connection Idle Time-out")
    tcpipHttpNetConnTimeout.setVisible(True)
    tcpipHttpNetConnTimeout.setDescription("Persistent Connection Idle Time-out")
    tcpipHttpNetConnTimeout.setDefaultValue(0)
    #tcpipHttpNetConnTimeout.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET allocation function, malloc style
    tcpipHttpNetMallocFunct = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_MALLOC_FUNC", None)
    tcpipHttpNetMallocFunct.setLabel("HTTP NET allocation function, malloc style")
    tcpipHttpNetMallocFunct.setVisible(True)
    tcpipHttpNetMallocFunct.setDescription("HTTP NET allocation function, malloc style")
    #tcpipHttpNetMallocFunct.setDefaultValue("")
    #tcpipHttpNetMallocFunct.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    # HTTP NET deallocation function, free style
    tcpipHttpNetFreeFunct = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_FREE_FUNC", None)
    tcpipHttpNetFreeFunct.setLabel("HTTP NET deallocation function, free style")
    tcpipHttpNetFreeFunct.setVisible(True)
    tcpipHttpNetFreeFunct.setDescription("HTTP NET deallocation function, free style")
    #tcpipHttpNetFreeFunct.setDefaultValue("")
    #tcpipHttpNetFreeFunct.setDependencies(tcpipHttpNetMenuVisibleSingle, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])

    #Add to system_config.h
    tcpipHttpNetHeaderFtl = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetHeaderFtl.setSourcePath("tcpip/config/http_net.h.ftl")
    tcpipHttpNetHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipHttpNetHeaderFtl.setMarkup(True)
    tcpipHttpNetHeaderFtl.setType("STRING")


    # Add http_net.c file
    tcpipHttpNetSourceFile = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetSourceFile.setSourcePath("tcpip/src/http_net.c")
    tcpipHttpNetSourceFile.setOutputName("http_net.c")
    tcpipHttpNetSourceFile.setOverwrite(True)
    tcpipHttpNetSourceFile.setDestPath("library/tcpip/src/")
    tcpipHttpNetSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipHttpNetSourceFile.setType("SOURCE")
    tcpipHttpNetSourceFile.setEnabled(True)
    tcpipHttpNetSourceFile.setDependencies(tcpipHttpNetGenSourceFile, ["TCPIP_STACK_USE_HTTP_NET_SERVER"])


    # ifblock TCPIP_HTTP_NET_CUSTOM_TEMPLATE

    # template HTTP_NET_PRINT_C "$HARMONY_VERSION_PATH/framework/tcpip/config/custom_app/http_net_print.c.ftl" to "$PROJECT_SOURCE_FILES/app/http_net_print.c"
    tcpipHttpNetPrintSourceFile = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetPrintSourceFile.setSourcePath("tcpip/config/custom_app/http_net_print.c.ftl")
    tcpipHttpNetPrintSourceFile.setOutputName("http_net_print.c")
    tcpipHttpNetPrintSourceFile.setDestPath("../../")
    tcpipHttpNetPrintSourceFile.setProjectPath("")
    tcpipHttpNetPrintSourceFile.setType("SOURCE")
    tcpipHttpNetPrintSourceFile.setMarkup(True)
    tcpipHttpNetPrintSourceFile.setDependencies(tcpipHttpNetGenSourceFile, ["TCPIP_HTTP_NET_CUSTOM_TEMPLATE"])
    
    # template HTTP_NET_PRINT_H "$HARMONY_VERSION_PATH/framework/tcpip/config/custom_app/http_net_print.h.ftl" to "$PROJECT_SOURCE_FILES/app/http_net_print.h"
    tcpipHttpNetPrintHeaderFile = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetPrintHeaderFile.setSourcePath("tcpip/config/custom_app/http_net_print.h.ftl")
    tcpipHttpNetPrintHeaderFile.setOutputName("http_net_print.h")
    tcpipHttpNetPrintHeaderFile.setDestPath("../../")
    tcpipHttpNetPrintHeaderFile.setProjectPath("")
    tcpipHttpNetPrintHeaderFile.setType("HEADER")
    tcpipHttpNetPrintHeaderFile.setMarkup(True)
    tcpipHttpNetPrintHeaderFile.setDependencies(tcpipHttpNetGenSourceFile, ["TCPIP_HTTP_NET_CUSTOM_TEMPLATE"])
    
    # template HTTP_NET_CUSTOM_APP_C "$HARMONY_VERSION_PATH/framework/tcpip/config/custom_app/custom_http_net_app.c.ftl" to "$PROJECT_SOURCE_FILES/app/custom_http_net_app.c"
    tcpipHttpNetCstmAppSourceFile = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetCstmAppSourceFile.setSourcePath("tcpip/config/custom_app/custom_http_net_app.c.ftl")
    tcpipHttpNetCstmAppSourceFile.setOutputName("custom_http_net_app.c")
    tcpipHttpNetCstmAppSourceFile.setDestPath("../../")
    tcpipHttpNetCstmAppSourceFile.setProjectPath("")
    tcpipHttpNetCstmAppSourceFile.setType("SOURCE")
    tcpipHttpNetCstmAppSourceFile.setMarkup(True)
    tcpipHttpNetCstmAppSourceFile.setDependencies(tcpipHttpNetGenSourceFile, ["TCPIP_HTTP_NET_CUSTOM_TEMPLATE"])
    
    # ifblock TCPIP_HTTP_NET_CUSTOM_TEMPLATE_SL
    # template HTTP_NET_MPFS_IMG "$HARMONY_VERSION_PATH/framework/tcpip/config/custom_app/mpfs_img2_net.c.ftl" to "$PROJECT_SOURCE_FILES/app/mpfs_img2_net.c"
    # endif
    tcpipHttpNetMpfsImg2SourceFile = tcpipHttpNetComponent.createFileSymbol(None, None)
    tcpipHttpNetMpfsImg2SourceFile.setSourcePath("tcpip/config/custom_app/mpfs_img2_net.c.ftl")
    tcpipHttpNetMpfsImg2SourceFile.setOutputName("mpfs_net_img.c")
    tcpipHttpNetMpfsImg2SourceFile.setDestPath("../../")
    tcpipHttpNetMpfsImg2SourceFile.setProjectPath("")
    tcpipHttpNetMpfsImg2SourceFile.setType("SOURCE")
    tcpipHttpNetMpfsImg2SourceFile.setMarkup(True)
    tcpipHttpNetMpfsImg2SourceFile.setEnabled(False)
    tcpipHttpNetMpfsImg2SourceFile.setDependencies(tcpipHttpNetGenSourceFile, ["TCPIP_HTTP_NET_CUSTOM_TEMPLATE_SL"])    

    execfile(Module.getPath() + "/tcpip/config/webpage.py")

# make Http Net Server option visible
def tcpipHttpNetSrvVisible(tcpipDependentSymbol, tcpipIPSymbol):    
    tcpipHttp = Database.getSymbolValue("tcpipHttp","TCPIP_STACK_USE_HTTP_SERVER")
    tcpipTcp = Database.getSymbolValue("tcpipTcp","TCPIP_USE_TCP")

    if(tcpipTcp):
        tcpipDependentSymbol.setVisible(True)
        if(tcpipHttp):
            tcpipDependentSymbol.setReadOnly(True)
        else:           
            tcpipDependentSymbol.setReadOnly(False)
    else:
        tcpipDependentSymbol.setVisible(False)

# # make Http Net Module file upload name option visible
# def tcpipHttpNetFileUploadVisible(tcpipDependentSymbol, tcpipIPSymbol):   
    # tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    # tcpipHttpNetFileUpload = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_FILE_UPLOAD_ENABLE")

    # if(tcpipHttpNet and tcpipHttpNetFileUpload):
        # tcpipDependentSymbol.setVisible(True)
    # else:
        # tcpipDependentSymbol.setVisible(False)

# make Http Net Module file upload name option visible
def tcpipHttpNetFileUploadVisible(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# make Http Net Server Config Flag Secure options visible
def tcpipHttpNetSrvConfigFlagSecureOnEnable(tcpipDependentSymbol, tcpipIPSymbol):   
    #tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetSrvConfigFlagSecureOff = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_OFF")
    tcpipHttpNetSrvConfigFlagSecureDefault = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_DEFAULT")

    #if(tcpipHttpNet):
    if(tcpipHttpNetSrvConfigFlagSecureOff or tcpipHttpNetSrvConfigFlagSecureDefault):
        tcpipDependentSymbol.setVisible(False)
        print("SecureOn disable")
    else:
        tcpipDependentSymbol.setVisible(True)
        print("SecureOn enable")
    # else:
        # tcpipDependentSymbol.setVisible(False)
        # print("SecureOn disable") 


def tcpipHttpNetSrvConfigFlagSecureOffEnable(tcpipDependentSymbol, tcpipIPSymbol):  
    #tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetSrvConfigFlagSecureOn = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_ON")
    tcpipHttpNetSrvConfigFlagSecureDefault = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_DEFAULT")
    
    #if(tcpipHttpNet):
    if(tcpipHttpNetSrvConfigFlagSecureOn or tcpipHttpNetSrvConfigFlagSecureDefault):
        tcpipDependentSymbol.setVisible(False)
        print("SecureOff disable")
    else:
        tcpipDependentSymbol.setVisible(True)
        print("SecureOff enable")
    # else:
        # tcpipDependentSymbol.setVisible(False)
        # print("SecureOff disable")


def tcpipHttpNetSrvConfigFlagSecureDefaultEnable(tcpipDependentSymbol, tcpipIPSymbol):  
    #tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetSrvConfigFlagSecureOn = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_ON")
    tcpipHttpNetSrvConfigFlagSecureOff = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CONFIG_FLAG_SECURE_OFF")
    
    #if(tcpipHttpNet):      
    if(tcpipHttpNetSrvConfigFlagSecureOn or tcpipHttpNetSrvConfigFlagSecureOff):
        tcpipDependentSymbol.setVisible(False)
        print("Securedefault disable")
    else:
        tcpipDependentSymbol.setVisible(True)
        print("Securedefault enable")
    # else:
        # tcpipDependentSymbol.setVisible(False)
        # print("Securedefault disable")

# make Http Net Module Dynamic Variable options visible
def tcpipHttpNetDynVarVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetDynVarProcess = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_DYNVAR_PROCESS")

    if(tcpipHttpNet and tcpipHttpNetDynVarProcess):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)  

# make Http Net Module SSI Attribute options visible
def tcpipHttpNetSsiAttrVisible(tcpipDependentSymbol, tcpipIPSymbol):    
    tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetSsiProcess= Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_SSI_PROCESS")

    if(tcpipHttpNet and tcpipHttpNetSsiProcess):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)

# make Http Net Module custom http net Attribute options visible
def tcpipHttpNetWebServerPathVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipHttpNet = Database.getSymbolValue("tcpipHttpNet","TCPIP_STACK_USE_HTTP_NET_SERVER")
    tcpipHttpNetCustomHTTPNetProcess = Database.getSymbolValue("tcpipHttpNet","TCPIP_HTTP_NET_CUSTOM_TEMPLATE")

    if(tcpipHttpNet and tcpipHttpNetCustomHTTPNetProcess):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)



def tcpipHttpNetMenuVisibleSingle(symbol, event):
    if (event["value"] == True):
        print("TFTPC Menu Visible.")
        symbol.setVisible(True)
    else:
        print("TFTPC Menu Invisible.")
        symbol.setVisible(False)

def tcpipHttpNetBase64DecodeOpt(symbol, event):
    symbol.clearValue()
    if (event["value"] == True):
        symbol.setValue(True,2)
    else:
        symbol.setValue(False,2)

def tcpipHttpNetGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])

def destroyComponent(component):
    Database.setSymbolValue("tcpipHttpNet", "TCPIP_STACK_USE_HTTP_NET_SERVER", False, 2)

def tcpipHttpNetCustomSlSet(symbol, event):
    symbol.clearValue()
    if (event["value"] == True):
        symbol.setValue(True,2)
    else:
        symbol.setValue(False,2)

def onAttachmentConnected(source, target):
    if (source["id"] == "HttpNet_TcpipFs_Dependency"): 
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_SYS_FS_CONNECT") != True):
            Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_SYS_FS_CONNECT", True)
