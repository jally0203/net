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

    
def instantiateComponent(tcpipFtpsComponent):
    print("TCPIP FTP Server Component")
    configName = Variables.get("__CONFIGURATION_NAME")
        
    # Use FTP Module
    tcpipFtpsModule = tcpipFtpsComponent.createBooleanSymbol("TCPIP_USE_FTP_MODULE", None)
    tcpipFtpsModule.setLabel("Use FTP Module")
    tcpipFtpsModule.setVisible(False)
    tcpipFtpsModule.setDescription("Use FTP Module")
    tcpipFtpsModule.setDefaultValue(True)
    #tcpipFtpsModule.setDependencies(tcpipFtpsModuleMenuVisible, ["tcpipIPv4.TCPIP_STACK_USE_IPV4", "tcpipTcp.TCPIP_USE_TCP"])

    # Maximum Length for User Name
    tcpipFtpsUsrNameMaxLen = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_USER_NAME_LEN", None)
    tcpipFtpsUsrNameMaxLen.setLabel("Maximum Length for User Name")
    tcpipFtpsUsrNameMaxLen.setVisible(True)
    tcpipFtpsUsrNameMaxLen.setDescription("Maximum Length for User Name")
    tcpipFtpsUsrNameMaxLen.setDefaultValue(10)
    #tcpipFtpsUsrNameMaxLen.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # Maximum Length of FTP Login Password
    tcpipFtpsLoginPswdMaxLen = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_PASSWD_LEN", None)
    tcpipFtpsLoginPswdMaxLen.setLabel("Maximum Length of FTP Login Password")
    tcpipFtpsLoginPswdMaxLen.setVisible(True)
    tcpipFtpsLoginPswdMaxLen.setDescription("Maximum Length of FTP Login Password")
    tcpipFtpsLoginPswdMaxLen.setDefaultValue(10)
    #tcpipFtpsLoginPswdMaxLen.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # Maximum Number of FTP Connections Allowed per Interface
    tcpipFtpsConnMaxNum = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_MAX_CONNECTIONS", None)
    tcpipFtpsConnMaxNum.setLabel("Maximum Number of FTP Connections Allowed per Interface")
    tcpipFtpsConnMaxNum.setVisible(True)
    tcpipFtpsConnMaxNum.setDescription("Maximum Number of FTP Connections Allowed per Interface")
    tcpipFtpsConnMaxNum.setDefaultValue(1)
    #tcpipFtpsConnMaxNum.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # Transmit Buffer Size for the FTP Data Socket
    tcpipFtpsDataSktTxBuffSize = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_DATA_SKT_TX_BUFF_SIZE", None)
    tcpipFtpsDataSktTxBuffSize.setLabel("TX Buffer for the FTP Data Socket")
    tcpipFtpsDataSktTxBuffSize.setVisible(True)
    tcpipFtpsDataSktTxBuffSize.setDescription("Transmit Buffer Size for the FTP Data Socket")
    tcpipFtpsDataSktTxBuffSize.setDefaultValue(0)
    #tcpipFtpsDataSktTxBuffSize.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # Receive Buffer Size for the FTP Data Socket
    tcpipFtpsDataSktRxBuffSize = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_DATA_SKT_RX_BUFF_SIZE", None)
    tcpipFtpsDataSktRxBuffSize.setLabel("RX Buffer for the FTP Data Socket")
    tcpipFtpsDataSktRxBuffSize.setVisible(True)
    tcpipFtpsDataSktRxBuffSize.setDescription("Receive Buffer Size for the FTP Data Socket")
    tcpipFtpsDataSktRxBuffSize.setDefaultValue(0)
    #tcpipFtpsDataSktRxBuffSize.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # FTP Server Task Rate in msec
    tcpipFtpsTskTickRate = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTPS_TASK_TICK_RATE", None)
    tcpipFtpsTskTickRate.setLabel("FTP Server Task Rate in msec")
    tcpipFtpsTskTickRate.setVisible(True)
    tcpipFtpsTskTickRate.setDescription("FTP Server Task Rate in msec")
    tcpipFtpsTskTickRate.setDefaultValue(33)
    #tcpipFtpsTskTickRate.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # FTP Server timeout in seconds
    tcpipFtpsTimeout = tcpipFtpsComponent.createIntegerSymbol("TCPIP_FTP_TIMEOUT", None)
    tcpipFtpsTimeout.setLabel("FTP Server timeout in sec")
    tcpipFtpsTimeout.setVisible(True)
    tcpipFtpsTimeout.setDescription("FTP Server timeout in seconds")
    tcpipFtpsTimeout.setDefaultValue(180)
    #tcpipFtpsTimeout.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])


    # FTP Login User Name
    tcpipFtpsLoginUsrName = tcpipFtpsComponent.createStringSymbol("TCPIP_FTP_USER_NAME", None)
    tcpipFtpsLoginUsrName.setLabel("FTP Login User Name")
    tcpipFtpsLoginUsrName.setVisible(True)
    tcpipFtpsLoginUsrName.setDescription("FTP Login User Name")
    tcpipFtpsLoginUsrName.setDefaultValue("Microchip")
    #tcpipFtpsLoginUsrName.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # FTP Login Password
    tcpipFtpsLoginUsrName = tcpipFtpsComponent.createStringSymbol("TCPIP_FTP_PASSWORD", None)
    tcpipFtpsLoginUsrName.setLabel("FTP Login Password")
    tcpipFtpsLoginUsrName.setVisible(True)
    tcpipFtpsLoginUsrName.setDescription("FTP Login Password")
    tcpipFtpsLoginUsrName.setDefaultValue("Harmony")
    #tcpipFtpsLoginUsrName.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    # Enable FTP File PUT Command
    tcpipFtpsFilePut = tcpipFtpsComponent.createBooleanSymbol("TCPIP_FTP_PUT_ENABLED", None)
    tcpipFtpsFilePut.setLabel("FTP File PUT Command")
    tcpipFtpsFilePut.setVisible(True)
    tcpipFtpsFilePut.setDescription("Enable FTP File PUT Command")
    tcpipFtpsFilePut.setDefaultValue(True)
    #tcpipFtpsFilePut.setDependencies(tcpipFtpsMenuVisible, ["TCPIP_USE_FTP_MODULE"])

    #Add to system_config.h
    tcpipFtpsHeaderFtl = tcpipFtpsComponent.createFileSymbol(None, None)
    tcpipFtpsHeaderFtl.setSourcePath("tcpip/config/ftp.h.ftl")
    tcpipFtpsHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipFtpsHeaderFtl.setMarkup(True)
    tcpipFtpsHeaderFtl.setType("STRING")    

    # Add ftp.c file
    tcpipFtpsSourceFile = tcpipFtpsComponent.createFileSymbol(None, None)
    tcpipFtpsSourceFile.setSourcePath("tcpip/src/ftp.c")
    tcpipFtpsSourceFile.setOutputName("ftp.c")
    tcpipFtpsSourceFile.setOverwrite(True)
    tcpipFtpsSourceFile.setDestPath("library/tcpip/src/")
    tcpipFtpsSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipFtpsSourceFile.setType("SOURCE")
    tcpipFtpsSourceFile.setEnabled(True)
    #tcpipFtpsSourceFile.setDependencies(tcpipFtpsGenSourceFile, ["TCPIP_USE_FTP_MODULE"])

    # Default FTP Mount point directory
    tcpipFtpRootDir = tcpipFtpsComponent.createStringSymbol("TCPIP_FTP_MOUNT_POINT", None)
    tcpipFtpRootDir.setLabel("FTP Server Root Directory Path")
    tcpipFtpRootDir.setVisible(True)
    tcpipFtpRootDir.setDescription("FTP Server Root Directory Path")
    tcpipFtpRootDir.setDefaultValue("/mnt/mchpSite1/")

    
def tcpipFtpsMenuVisible(symbol, event):
    if (event["value"] == True):
        print("FTP server Menu Visible.")       
        symbol.setVisible(True)
    else:
        print("FTP Server Menu Invisible.")
        symbol.setVisible(False)    
        
# make FTP Module option visible
def tcpipFtpsModuleMenuVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipIPv4 = Database.getSymbolValue("tcpipIPv4","TCPIP_STACK_USE_IPV4")
    tcpipTcp = Database.getSymbolValue("tcpipTcp","TCPIP_USE_TCP")

    if(tcpipIPv4 and tcpipTcp):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)
        
def tcpipFtpsGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])

def destroyComponent(component):
    Database.setSymbolValue("tcpipFtps", "TCPIP_USE_FTP_MODULE", False, 2)
    
def onAttachmentConnected(source, target):
    if (source["id"] == "Ftps_TcpipFs_Dependency"): 
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_SYS_FS_CONNECT") != True):
            Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_SYS_FS_CONNECT", True)