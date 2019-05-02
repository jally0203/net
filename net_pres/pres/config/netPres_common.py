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

def instantiateComponent(netPresCommonComponent):

	print("Network Presentation Component")
	configName = Variables.get("__CONFIGURATION_NAME")

	# Network Presentation Layer
	netPresNeeded = netPresCommonComponent.createBooleanSymbol("NET_PRES_NEEDED", None)
	netPresNeeded.setLabel("Use Network Presentation Layer")
	netPresNeeded.setVisible(False)
	netPresNeeded.setDefaultValue(True)

	# Use MPLAB Harmony Networking Presentation Layer
	netPresUse = netPresCommonComponent.createBooleanSymbol("NET_PRES_USE", None)
	netPresUse.setLabel("Use MPLAB Harmony Networking Presentation Layer")
	netPresUse.setVisible(False)
	netPresUse.setDefaultValue(True)
	
	# RTOS Configuration
	netPresRtosMenu = netPresCommonComponent.createMenuSymbol("NET_PRES_RTOS_MENU", None)
	netPresRtosMenu.setLabel("RTOS Configuration")
	netPresRtosMenu.setDescription("RTOS Configuration")
	netPresRtosMenu.setVisible(False)
	netPresRtosMenu.setVisible((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal") and (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != None))
	netPresRtosMenu.setDependencies(netPresshowRTOSMenu, ["HarmonyCore.SELECT_RTOS"])
	
	# Net Pres Execution mode
	netPresExecMode = netPresCommonComponent.createComboSymbol("NET_PRES_RTOS", netPresRtosMenu, ["Standalone"]) 
	netPresExecMode.setLabel("Run this driver instance as")
	netPresExecMode.setVisible(False)
	netPresExecMode.setDescription("Net Pres Execution mode")
	netPresExecMode.setDefaultValue("Standalone")
	
	# Net Pres Task Size
	netPresTaskSize = netPresCommonComponent.createIntegerSymbol("NET_PRES_RTOS_STACK_SIZE", netPresRtosMenu)
	netPresTaskSize.setLabel("Task Size")
	netPresTaskSize.setVisible(True)
	netPresTaskSize.setDescription("Net Pres Task Size")
	netPresTaskSize.setDefaultValue(1024)
	netPresTaskSize.setDependencies(netPresRTOSStandaloneMenu, ["NET_PRES_RTOS"])
	
	# Net Pres Task Priority
	netPresTaskPriority = netPresCommonComponent.createIntegerSymbol("NET_PRES_RTOS_TASK_PRIORITY", netPresRtosMenu)
	netPresTaskPriority.setLabel("Task Priority")
	netPresTaskPriority.setVisible(True)
	netPresTaskPriority.setDescription("Net Pres Task Priority")
	netPresTaskPriority.setDefaultValue(1)
	netPresTaskPriority.setDependencies(netPresRTOSStandaloneMenu, ["NET_PRES_RTOS"])
	
	# Net Pres Task Delay?
	netPresUseTaskDelay = netPresCommonComponent.createBooleanSymbol("NET_PRES_RTOS_USE_DELAY", netPresRtosMenu)
	netPresUseTaskDelay.setLabel("Use Task Delay?")
	netPresUseTaskDelay.setVisible(True)
	netPresUseTaskDelay.setDescription("Net Pres Use Task Delay?")
	netPresUseTaskDelay.setDefaultValue(True)
	netPresUseTaskDelay.setDependencies(netPresRTOSStandaloneMenu, ["NET_PRES_RTOS"])
	
	# Net Pres Task Delay
	netPresTaskDelay = netPresCommonComponent.createIntegerSymbol("NET_PRES_RTOS_DELAY", netPresRtosMenu)
	netPresTaskDelay.setLabel("Task Delay")
	netPresTaskDelay.setVisible(True)
	netPresTaskDelay.setDescription("Net Pres Task Delay")
	netPresTaskDelay.setDefaultValue(1000)
	netPresTaskDelay.setDependencies(netPresRTOSTaskDelayMenu, ["NET_PRES_RTOS","NET_PRES_RTOS_USE_DELAY"])
		
	# Number of Presentation Sockets
	netPresSocketCnt = netPresCommonComponent.createIntegerSymbol("NET_PRES_SOCKETS", None)
	netPresSocketCnt.setLabel("Number of Presentation Sockets")
	netPresSocketCnt.setVisible(True)
	netPresSocketCnt.setDescription("Number of Presentation Sockets")
	netPresSocketCnt.setDefaultValue(10)

	# Use Fixed Flash Based Certificate Repository for Encryption?
	netPresBlobCertRepo = netPresCommonComponent.createBooleanSymbol("NET_PRES_BLOB_CERT_REPO", None)
	netPresBlobCertRepo.setLabel("Use Fixed Flash Based Certificate Repository for Encryption?")
	netPresBlobCertRepo.setVisible(True)
	netPresBlobCertRepo.setDescription("Use Fixed Flash Based Certificate Repository for Encryption?")
	netPresBlobCertRepo.setDefaultValue(False)
	
	# Generate Certificate Store Stubs?
	netPresGenCertStub = netPresCommonComponent.createBooleanSymbol("NET_PRES_CERT_STORE_STUBS", None)
	netPresGenCertStub.setLabel("Generate Certificate Store Stubs?")
	netPresGenCertStub.setVisible(True)
	netPresGenCertStub.setDescription("Generate Certificate Store Stubs?")
	netPresGenCertStub.setDefaultValue(False)	
	netPresBlobCertRepo.setDependencies(netPresCertRepo, ["NET_PRES_CERT_STORE_STUBS"])
	netPresGenCertStub.setDependencies(netPresCertRepo, ["NET_PRES_BLOB_CERT_REPO"])
	
	# Support Client Certificates?
	netPresBlobClientSupport = netPresCommonComponent.createBooleanSymbol("NET_PRES_BLOB_CLIENT_SUPPORT", netPresBlobCertRepo)
	netPresBlobClientSupport.setLabel("Support Client Certificates?")
	netPresBlobClientSupport.setVisible(False)
	netPresBlobClientSupport.setDescription("Support Client Certificates?")
	netPresBlobClientSupport.setDefaultValue(True)	
	netPresBlobClientSupport.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_CERT_REPO"])

	# File name containing definitions for Client Certificates?
	netPresBlobClientCertFileName = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_CLIENT_CERT_FILENAME", netPresBlobClientSupport) 
	netPresBlobClientCertFileName.setLabel("File name containing definitions for Client Certificates?")
	netPresBlobClientCertFileName.setVisible(True)
	netPresBlobClientCertFileName.setDescription("File name containing definitions for Client Certificates?")
	netPresBlobClientCertFileName.setDefaultValue("ca-certs.h")
	netPresBlobClientCertFileName.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_CLIENT_SUPPORT"])	

	# Variable Name Containing Data for Client Certificates?
	netPresBlobClientCertVar = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_CLIENT_CERT_VARIABLE", netPresBlobClientSupport) 
	netPresBlobClientCertVar.setLabel("Variable Name Containing Data for Client Certificates?")
	netPresBlobClientCertVar.setVisible(True)
	netPresBlobClientCertVar.setDescription("Variable Name Containing Data for Client Certificates?")
	netPresBlobClientCertVar.setDefaultValue("caCert")
	netPresBlobClientCertVar.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_CLIENT_SUPPORT"])	

	# Variable Name Containing Size of Client Certificates?
	netPresBlobClientCertLenVar = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_CLIENT_CERT_LEN_VARIABLE", netPresBlobClientSupport) 
	netPresBlobClientCertLenVar.setLabel("Variable Name Containing Size of Client Certificates?")
	netPresBlobClientCertLenVar.setVisible(True)
	netPresBlobClientCertLenVar.setDescription("Variable Name Containing Size of Client Certificates?")
	netPresBlobClientCertLenVar.setDefaultValue("caCert_len")
	netPresBlobClientCertLenVar.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_CLIENT_SUPPORT"])

	# Support Server Certificate?"
	netPresBlobServerSupport = netPresCommonComponent.createBooleanSymbol("NET_PRES_BLOB_SERVER_SUPPORT", netPresBlobCertRepo)
	netPresBlobServerSupport.setLabel("Support Server Certificate?")
	netPresBlobServerSupport.setVisible(False)
	netPresBlobServerSupport.setDescription("Support Server Certificate?")
	netPresBlobServerSupport.setDefaultValue(True)	
	netPresBlobServerSupport.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_CERT_REPO"])

	# File name containing definitions for Server Certificates?
	netPresBlobServerCertFileName = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_CERT_FILENAME", netPresBlobServerSupport) 
	netPresBlobServerCertFileName.setLabel("File name containing definitions for Server Certificates?")
	netPresBlobServerCertFileName.setVisible(True)
	netPresBlobServerCertFileName.setDescription("File name containing definitions for Server Certificates?")
	netPresBlobServerCertFileName.setDefaultValue("ca-certs.h")
	netPresBlobServerCertFileName.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])	

	# Variable Name Containing Data for Server Certificates?
	netPresBlobServerCertVar = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_CERT_VARIABLE", netPresBlobServerSupport) 
	netPresBlobServerCertVar.setLabel("Variable Name Containing Data for Server Certificates?")
	netPresBlobServerCertVar.setVisible(True)
	netPresBlobServerCertVar.setDescription("Variable Name Containing Data for Server Certificates?")
	netPresBlobServerCertVar.setDefaultValue("serverCert")
	netPresBlobServerCertVar.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])	

	# Variable Name Containing Size of Server Certificates?
	netPresBlobServerCertLenVar = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_CERT_LEN_VARIABLE", netPresBlobServerSupport) 
	netPresBlobServerCertLenVar.setLabel("Variable Name Containing Size of Server Certificates?")
	netPresBlobServerCertLenVar.setVisible(True)
	netPresBlobServerCertLenVar.setDescription("Variable Name Containing Size of Server Certificates?")
	netPresBlobServerCertLenVar.setDefaultValue("serverCert_len")
	netPresBlobServerCertLenVar.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])

	# File name containing definitions for Server Private Key?
	netPresBlobServerKeyFileName = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_KEY_FILENAME", netPresBlobServerSupport) 
	netPresBlobServerKeyFileName.setLabel("File name containing definitions for Server Private Key?")
	netPresBlobServerKeyFileName.setVisible(True)
	netPresBlobServerKeyFileName.setDescription("File name containing definitions for Server Private Key?")
	netPresBlobServerKeyFileName.setDefaultValue("ca-certs.h")
	netPresBlobServerKeyFileName.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])
	
	# Variable Name Containing Data for Server Private Key?
	netPresBlobServerKeyVar = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_KEY_VARIABLE", netPresBlobServerSupport) 
	netPresBlobServerKeyVar.setLabel("Variable Name Containing Data for Server Private Key?")
	netPresBlobServerKeyVar.setVisible(True)
	netPresBlobServerKeyVar.setDescription("Variable Name Containing Data for Server Private Key?")
	netPresBlobServerKeyVar.setDefaultValue("serverKey")
	netPresBlobServerKeyVar.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])
	
	# Variable Name Containing Size of Server Private Key?
	netPresBlobServerKeyLen = netPresCommonComponent.createStringSymbol("NET_PRES_BLOB_SERVER_KEY_LEN_VARIABLE", netPresBlobServerSupport) 
	netPresBlobServerKeyLen.setLabel("Variable Name Containing Size of Server Private Key?")
	netPresBlobServerKeyLen.setVisible(True)
	netPresBlobServerKeyLen.setDescription("Variable Name Containing Size of Server Private Key?")
	netPresBlobServerKeyLen.setDefaultValue("serverKey_len")
	netPresBlobServerKeyLen.setDependencies(netPresMenuVisible, ["NET_PRES_BLOB_SERVER_SUPPORT"])
	
	# Generate Client Certificate Stubs?
	netPresCertStoreStubClient = netPresCommonComponent.createBooleanSymbol("NET_PRES_CERT_STORE_STUBS_CLIENT", netPresGenCertStub)
	netPresCertStoreStubClient.setLabel("Generate Client Certificate Stubs?")
	netPresCertStoreStubClient.setVisible(False)
	netPresCertStoreStubClient.setDescription("Generate Client Certificate Stubs?")
	netPresCertStoreStubClient.setDefaultValue(True)	
	netPresCertStoreStubClient.setDependencies(netPresMenuVisible, ["NET_PRES_CERT_STORE_STUBS"])	
	
	# Generate Server Certificate Stubs?
	netPresCertStoreStubServer = netPresCommonComponent.createBooleanSymbol("NET_PRES_CERT_STORE_STUBS_SERVER", netPresGenCertStub)
	netPresCertStoreStubServer.setLabel("Generate Server Certificate Stubs?")
	netPresCertStoreStubServer.setVisible(False)
	netPresCertStoreStubServer.setDescription("Generate Server Certificate Stubs?")
	netPresCertStoreStubServer.setDefaultValue(True)	
	netPresCertStoreStubServer.setDependencies(netPresMenuVisible, ["NET_PRES_CERT_STORE_STUBS"])			

	# file NET_PRES1_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres.h"
	netPresHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresHeaderFile.setSourcePath("net_pres/pres/net_pres.h")
	netPresHeaderFile.setOutputName("net_pres.h")
	netPresHeaderFile.setDestPath("net_pres/pres/")
	netPresHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresHeaderFile.setType("HEADER")
	netPresHeaderFile.setOverwrite(True)
	
	# file NET_PRES2_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres_certstore.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres_certstore.h"
	netPresCertStoreHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresCertStoreHeaderFile.setSourcePath("net_pres/pres/net_pres_certstore.h")
	netPresCertStoreHeaderFile.setOutputName("net_pres_certstore.h")
	netPresCertStoreHeaderFile.setDestPath("net_pres/pres/")
	netPresCertStoreHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresCertStoreHeaderFile.setType("HEADER")
	netPresCertStoreHeaderFile.setOverwrite(True)	
	
	# file NET_PRES3_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres_encryptionproviderapi.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres_encryptionproviderapi.h"
	netPresEncryptApiHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresEncryptApiHeaderFile.setSourcePath("net_pres/pres/net_pres_encryptionproviderapi.h")
	netPresEncryptApiHeaderFile.setOutputName("net_pres_encryptionproviderapi.h")
	netPresEncryptApiHeaderFile.setDestPath("net_pres/pres/")
	netPresEncryptApiHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresEncryptApiHeaderFile.setType("HEADER")
	netPresEncryptApiHeaderFile.setOverwrite(True)		
	
	# file NET_PRES4_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres_socketapi.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres_socketapi.h"
	netPresSocketApiHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresSocketApiHeaderFile.setSourcePath("net_pres/pres/net_pres_socketapi.h")
	netPresSocketApiHeaderFile.setOutputName("net_pres_socketapi.h")
	netPresSocketApiHeaderFile.setDestPath("net_pres/pres/")
	netPresSocketApiHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresSocketApiHeaderFile.setType("HEADER")
	netPresSocketApiHeaderFile.setOverwrite(True)		
	
	# file NET_PRES5_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres_transportapi.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres_transportapi.h"
	netPresTransApiHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresTransApiHeaderFile.setSourcePath("net_pres/pres/net_pres_transportapi.h")
	netPresTransApiHeaderFile.setOutputName("net_pres_transportapi.h")
	netPresTransApiHeaderFile.setDestPath("net_pres/pres/")
	netPresTransApiHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresTransApiHeaderFile.setType("HEADER")
	netPresTransApiHeaderFile.setOverwrite(True)		
	
	# file NET_PRES_LOCAL_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/src/net_pres_local.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/src/net_pres_local.h"
	netPresLocalHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresLocalHeaderFile.setSourcePath("net_pres/pres/src/net_pres_local.h")
	netPresLocalHeaderFile.setOutputName("net_pres_local.h")
	netPresLocalHeaderFile.setDestPath("net_pres/pres/src/")
	netPresLocalHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/src/")
	netPresLocalHeaderFile.setType("HEADER")
	netPresLocalHeaderFile.setOverwrite(True)		
		
	# file NET_PRES_SOCKETAPICONVERSION_H "$HARMONY_VERSION_PATH/framework/net_pres/pres/net_pres_socketapiconversion.h"  to "$PROJECT_HEADER_FILES/framework/net_pres/pres/net_pres_socketapiconversion.h"
	netPresSktApiConvHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresSktApiConvHeaderFile.setSourcePath("net_pres/pres/net_pres_socketapiconversion.h")
	netPresSktApiConvHeaderFile.setOutputName("net_pres_socketapiconversion.h")
	netPresSktApiConvHeaderFile.setDestPath("net_pres/pres/")
	netPresSktApiConvHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresSktApiConvHeaderFile.setType("HEADER")
	netPresSktApiConvHeaderFile.setOverwrite(True)	

	# add "<#include \"/framework/net/templates/system_init.c.data.ftl\">"  to list SYSTEM_INIT_C_MODULE_INITIALIZATION_DATA
	netPresSysInitDataSourceFtl = netPresCommonComponent.createFileSymbol(None, None)
	netPresSysInitDataSourceFtl.setType("STRING")
	netPresSysInitDataSourceFtl.setOutputName("core.LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA")
	netPresSysInitDataSourceFtl.setSourcePath("net_pres/pres/templates/system/system_data_initialize.c.ftl")
	netPresSysInitDataSourceFtl.setMarkup(True)
	
	# add "<#include \"/framework/net/templates/system_init.c.call.ftl\">"  to list SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE
	netPresSysInitCallSourceFtl = netPresCommonComponent.createFileSymbol(None, None)
	netPresSysInitCallSourceFtl.setType("STRING")
	netPresSysInitCallSourceFtl.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
	netPresSysInitCallSourceFtl.setSourcePath("net_pres/pres/templates/system/system_initialize.c.ftl")
	netPresSysInitCallSourceFtl.setMarkup(True)

	netPresSystemDefFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresSystemDefFile.setType("STRING")
	netPresSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	netPresSystemDefFile.setSourcePath("net_pres/pres/templates/system/system_definitions.h.ftl")
	netPresSystemDefFile.setMarkup(True)
	
	netPresSystemDefObjFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresSystemDefObjFile.setType("STRING")
	netPresSystemDefObjFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS")
	netPresSystemDefObjFile.setSourcePath("net_pres/pres/templates/system/system_definitions_object.h.ftl")
	netPresSystemDefObjFile.setMarkup(True)
	
	netPresSystemConfigFtl = netPresCommonComponent.createFileSymbol(None, None)
	netPresSystemConfigFtl.setSourcePath("net_pres/pres/templates/system/system_config.h.ftl")
	netPresSystemConfigFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
	netPresSystemConfigFtl.setMarkup(True)
	netPresSystemConfigFtl.setType("STRING")
	
	# add "<#include \"/framework/net/templates/system_tasks.c.ftl\">"  to list SYSTEM_TASKS_C_CALL_LIB_TASKS
	netPresSysTaskSourceFtl = netPresCommonComponent.createFileSymbol(None, None)
	netPresSysTaskSourceFtl.setType("STRING")
	netPresSysTaskSourceFtl.setOutputName("core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS")
	netPresSysTaskSourceFtl.setSourcePath("net_pres/pres/templates/system/system_tasks.c.ftl")
	netPresSysTaskSourceFtl.setMarkup(True)

	netPresSystemRtosTasksFile = netPresCommonComponent.createFileSymbol("NET_PRES_SYS_RTOS_TASK", None)
	netPresSystemRtosTasksFile.setType("STRING")
	netPresSystemRtosTasksFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
	netPresSystemRtosTasksFile.setSourcePath("net_pres/pres/templates/system/system_rtos_tasks.c.ftl")
	netPresSystemRtosTasksFile.setMarkup(True)
	netPresSystemRtosTasksFile.setEnabled((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"))
	netPresSystemRtosTasksFile.setDependencies(genRtosTask, ["HarmonyCore.SELECT_RTOS"])
	
	# file NET_PRES_C "$HARMONY_VERSION_PATH/framework/net_pres/pres/src/net_pres.c" to "$PROJECT_SOURCE_FILES/framework/net_pres/pres/src/net_pres.c"
	netPresSourceFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresSourceFile.setSourcePath("net_pres/pres/src/net_pres.c")
	netPresSourceFile.setOutputName("net_pres.c")
	netPresSourceFile.setOverwrite(True)
	netPresSourceFile.setDestPath("net_pres/pres/src/")
	netPresSourceFile.setProjectPath("config/" + configName + "/net_pres/pres/src/")
	netPresSourceFile.setType("SOURCE")
	netPresSourceFile.setEnabled(True)
		
	# template NET_PRES_ENC_GLUE_H_TEMPLATE "$HARMONY_VERSION_PATH/framework/net_pres/pres/templates/net_pres_enc_glue.h.ftl" to "$PROJECT_HEADER_FILES/app/system_config/$CONFIGURATION/framework/net_pres/pres/net_pres_enc_glue.h"
	netPresEncGlueHeaderFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresEncGlueHeaderFile.setSourcePath("net_pres/pres/templates/net_pres_enc_glue.h.ftl")
	netPresEncGlueHeaderFile.setOutputName("net_pres_enc_glue.h")
	netPresEncGlueHeaderFile.setMarkup(True)
	netPresEncGlueHeaderFile.setDestPath("net_pres/pres/")
	netPresEncGlueHeaderFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresEncGlueHeaderFile.setType("HEADER")
	netPresEncGlueHeaderFile.setOverwrite(True)
	
	# template NET_PRES_ENC_GLUE_C_TEMPLATE "$HARMONY_VERSION_PATH/framework/net_pres/pres/templates/net_pres_enc_glue.c.ftl" to "$PROJECT_SOURCE_FILES/app/system_config/$CONFIGURATION/framework/net_pres/pres/net_pres_enc_glue.c"	
	netPresEncGlueSourceFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresEncGlueSourceFile.setSourcePath("net_pres/pres/templates/net_pres_enc_glue.c.ftl")
	netPresEncGlueSourceFile.setOutputName("net_pres_enc_glue.c")
	netPresEncGlueSourceFile.setDestPath("net_pres/pres/")
	netPresEncGlueSourceFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresEncGlueSourceFile.setType("SOURCE")
	netPresEncGlueSourceFile.setMarkup(True)	

	# ifblock NET_PRES_BLOB_CERT_REPO || NET_PRES_CERT_STORE_STUBS
	# template NET_PRES_ENC_CERT_STORE_C_TEMPLATE "$HARMONY_VERSION_PATH/framework/net_pres/pres/templates/net_pres_cert_store.c.ftl" to "$PROJECT_SOURCE_FILES/app/system_config/$CONFIGURATION/framework/net_pres/pres/net_pres_cert_store.c"
	# endif 
	netPresCertStoreSourceFile = netPresCommonComponent.createFileSymbol(None, None)
	netPresCertStoreSourceFile.setSourcePath("net_pres/pres/templates/net_pres_cert_store.c.ftl")
	netPresCertStoreSourceFile.setOutputName("net_pres_cert_store.c")
	netPresCertStoreSourceFile.setDestPath("net_pres/pres/")
	netPresCertStoreSourceFile.setProjectPath("config/" + configName + "/net_pres/pres/")
	netPresCertStoreSourceFile.setType("SOURCE")
	netPresCertStoreSourceFile.setMarkup(True)
	netPresCertStoreSourceFile.setEnabled(False)
	netPresCertStoreSourceFile.setDependencies(netPresGenSourceFile, ["NET_PRES_BLOB_CERT_REPO","NET_PRES_CERT_STORE_STUBS"])
	
def netPresRtosVisible(symbol, event):
	if (event["value"] == "Standalone"):	
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

def netPresRTOSTaskDelayMenu(symbol, event):
	netPresRtos = Database.getSymbolValue("netPres","NET_PRES_RTOS")
	netPresRtosUseDelay = Database.getSymbolValue("netPres","NET_PRES_RTOS_USE_DELAY")
	if((netPresRtos == 'Standalone') and netPresRtosUseDelay):		
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

		
def netPresMenuVisible(symbol, event):
	if (event["value"] == True):	
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

def netPresCertRepo(symbol, event):	
	if(event["value"] == False):
		symbol.setVisible(True)			
	else:
		symbol.setVisible(False)
		
def netPresshowRTOSMenu(symbol, event):
	if (event["value"] == None):
		symbol.setVisible(False)
		print("NetPres: OSAL Disabled")
	elif (event["value"] != "BareMetal"):
		# If not Bare Metal
		symbol.setVisible(True)
		print("NetPres rtos")
	else:
		symbol.setVisible(False)
		print("NetPres Bare Metal")	
		
def netPresRTOSStandaloneMenu(symbol, event):
	if (event["value"] == 'Standalone'):		
		symbol.setVisible(True)
		print("netPres Standalone")
	else:
		symbol.setVisible(False)
		print("netPres Combined")		

def genRtosTask(symbol, event):
    symbol.setEnabled((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"))
	
def netPresGenSourceFile(sourceFile, event):
	netPresBlob = Database.getSymbolValue("netPres","NET_PRES_BLOB_CERT_REPO")
	netPresStub = Database.getSymbolValue("netPres","NET_PRES_CERT_STORE_STUBS")
	
	if(netPresBlob or netPresStub):
		sourceFile.setEnabled(True)
	else:
		sourceFile.setEnabled(False)
		