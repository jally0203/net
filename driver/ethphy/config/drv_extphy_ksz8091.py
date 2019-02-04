
def instantiateComponent(drvExtPhyKsz8091Component):
	print("KSZ8091 PHY Driver Component")
	configName = Variables.get("__CONFIGURATION_NAME")

	# Delay for the Link Initialization in ms
	drvExtPhyKsz8091LinkInitDelay= drvExtPhyKsz8091Component.createIntegerSymbol("TCPIP_INTMAC_PHY_LINK_INIT_DELAY", None)
	drvExtPhyKsz8091LinkInitDelay.setLabel("Delay for the Link Initialization - ms") 
	drvExtPhyKsz8091LinkInitDelay.setVisible(True)
	drvExtPhyKsz8091LinkInitDelay.setDescription("Delay for the Link Initialization in ms")
	drvExtPhyKsz8091LinkInitDelay.setDefaultValue(500)
	#drvExtPhyKsz8091LinkInitDelay.setDependencies(tcpipEthMacMenuVisibleSingle, ["TCPIP_USE_ETH_MAC"])

	# PHY Address
	drvExtPhyKsz8091Addr= drvExtPhyKsz8091Component.createIntegerSymbol("TCPIP_INTMAC_PHY_ADDRESS", None)
	drvExtPhyKsz8091Addr.setLabel("PHY Address") 
	drvExtPhyKsz8091Addr.setVisible(True)
	drvExtPhyKsz8091Addr.setDescription("PHY Address")
	drvExtPhyKsz8091Addr.setDefaultValue(0)

	# External PHY Connection Flags
	drvExtPhyKsz8091ConnFlag = drvExtPhyKsz8091Component.createMenuSymbol(None, None) 
	drvExtPhyKsz8091ConnFlag.setLabel("External PHY Connection Flags")
	drvExtPhyKsz8091ConnFlag.setVisible(True)
	drvExtPhyKsz8091ConnFlag.setDescription("External PHY Connection Flags")
	
	# RMII Data Interface
	drvExtPhyKsz8091ConfigRmii = drvExtPhyKsz8091Component.createBooleanSymbol("TCPIP_INTMAC_PHY_CONFIG_RMII", drvExtPhyKsz8091ConnFlag)
	drvExtPhyKsz8091ConfigRmii.setLabel("RMII Data Interface")
	drvExtPhyKsz8091ConfigRmii.setVisible(True)
	drvExtPhyKsz8091ConfigRmii.setDescription("RMII Data Interface")
	drvExtPhyKsz8091ConfigRmii.setDefaultValue(True)
	
	# Configuration Fuses Is ALT
	drvExtPhyKsz8091ConfigAlt = drvExtPhyKsz8091Component.createBooleanSymbol("TCPIP_INTMAC_PHY_CONFIG_ALTERNATE", drvExtPhyKsz8091ConnFlag)
	drvExtPhyKsz8091ConfigAlt.setLabel("Configuration Fuses Is ALT")
	drvExtPhyKsz8091ConfigAlt.setVisible(True)
	drvExtPhyKsz8091ConfigAlt.setDescription("Configuration Fuses Is ALT")
	drvExtPhyKsz8091ConfigAlt.setDefaultValue(False)
	
	# Use The Fuses Configuration
	drvExtPhyKsz8091ConfigAuto = drvExtPhyKsz8091Component.createBooleanSymbol("TCPIP_INTMAC_PHY_CONFIG_AUTO", drvExtPhyKsz8091ConnFlag)
	drvExtPhyKsz8091ConfigAuto.setLabel("Use The Fuses Configuration")
	drvExtPhyKsz8091ConfigAuto.setVisible(True)
	drvExtPhyKsz8091ConfigAuto.setDescription("Use The Fuses Configuration")
	drvExtPhyKsz8091ConfigAuto.setDefaultValue(False)
	
	# External PHY Type
	drvExtPhyKsz8091PhyType = drvExtPhyKsz8091Component.createStringSymbol("TCPIP_EMAC_PHY_TYPE", None)
	drvExtPhyKsz8091PhyType.setVisible(False)	
	drvExtPhyKsz8091PhyType.setDefaultValue("KSZ8091")
	

	# Driver PHY Instances Number
	drvExtPhyKsz8091InstanceNum= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_INSTANCES_NUMBER", None)
	drvExtPhyKsz8091InstanceNum.setLabel("PHY Instances Number") 
	drvExtPhyKsz8091InstanceNum.setVisible(True)
	drvExtPhyKsz8091InstanceNum.setDescription("Driver PHY Instances Number")
	drvExtPhyKsz8091InstanceNum.setDefaultValue(1)
	
	# Driver PHY Clients Number
	drvExtPhyKsz8091ClientNum= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_CLIENTS_NUMBER", None)
	drvExtPhyKsz8091ClientNum.setLabel("PHY Clients Number") 
	drvExtPhyKsz8091ClientNum.setVisible(True)
	drvExtPhyKsz8091ClientNum.setDescription("Driver PHY Clients Number")
	drvExtPhyKsz8091ClientNum.setDefaultValue(1)
	
	# Driver PHY Peripheral Index Number
	drvExtPhyKsz8091IndexNum= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_INDEX", None)
	drvExtPhyKsz8091IndexNum.setLabel("PHY Peripheral Index Number") 
	drvExtPhyKsz8091IndexNum.setVisible(True)
	drvExtPhyKsz8091IndexNum.setDescription("Driver PHY Peripheral Index Number")
	drvExtPhyKsz8091IndexNum.setDefaultValue(1)
	
	# Driver PHY Peripheral ID
	drvExtPhyKsz8091PeripheralId= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_PERIPHERAL_ID", None)
	drvExtPhyKsz8091PeripheralId.setLabel("PHY Peripheral ID") 
	drvExtPhyKsz8091PeripheralId.setVisible(True)
	drvExtPhyKsz8091PeripheralId.setDescription("Driver PHY Peripheral ID")
	drvExtPhyKsz8091PeripheralId.setDefaultValue(1)
	
	# Driver PHY Negotiation Time-out - ms
	drvExtPhyKsz8091NegInitTimeout= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_NEG_INIT_TMO", None)
	drvExtPhyKsz8091NegInitTimeout.setLabel("PHY Negotiation Time-out - ms") 
	drvExtPhyKsz8091NegInitTimeout.setVisible(True)
	drvExtPhyKsz8091NegInitTimeout.setDescription("Driver PHY Negotiation Time-out - ms")
	drvExtPhyKsz8091NegInitTimeout.setDefaultValue(1)
	
	# Driver PHY Negotiation Done Time-out - ms
	drvExtPhyKsz8091NegDoneTimeout= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_NEG_DONE_TMO", None)
	drvExtPhyKsz8091NegDoneTimeout.setLabel("PHY Negotiation Done Time-out - ms") 
	drvExtPhyKsz8091NegDoneTimeout.setVisible(True)
	drvExtPhyKsz8091NegDoneTimeout.setDescription("Driver PHY Negotiation Done Time-out - ms")
	drvExtPhyKsz8091NegDoneTimeout.setDefaultValue(2000)
	
	# Driver PHY Reset Clear Time-out - ms
	drvExtPhyKsz8091ResetClearTimeout= drvExtPhyKsz8091Component.createIntegerSymbol("DRV_ETHPHY_RESET_CLR_TMO", None)
	drvExtPhyKsz8091ResetClearTimeout.setLabel("PHY Reset Clear Time-out - ms") 
	drvExtPhyKsz8091ResetClearTimeout.setVisible(True)
	drvExtPhyKsz8091ResetClearTimeout.setDescription("Driver PHY Reset Clear Time-out - ms")
	drvExtPhyKsz8091ResetClearTimeout.setDefaultValue(500)
	
	# Use a Function to be called at PHY Reset
	drvExtPhyKsz8091ResetCallbackEnable = drvExtPhyKsz8091Component.createBooleanSymbol("DRV_ETHPHY_USE_RESET_CALLBACK", None)
	drvExtPhyKsz8091ResetCallbackEnable.setLabel("Use a Function to be called at PHY Reset")
	drvExtPhyKsz8091ResetCallbackEnable.setVisible(True)
	drvExtPhyKsz8091ResetCallbackEnable.setDescription("Use a Function to be called at PHY Reset")
	drvExtPhyKsz8091ResetCallbackEnable.setDefaultValue(False)
	
	# App Function
	drvExtPhyKsz8091ResetCallback = drvExtPhyKsz8091Component.createStringSymbol("DRV_ETHPHY_RESET_CALLBACK", drvExtPhyKsz8091ResetCallbackEnable)
	drvExtPhyKsz8091ResetCallback.setLabel("App Function")
	drvExtPhyKsz8091ResetCallback.setVisible(False)
	drvExtPhyKsz8091ResetCallback.setDescription("App Function")
	drvExtPhyKsz8091ResetCallback.setDefaultValue("AppPhyResetFunction")
	drvExtPhyKsz8091ResetCallback.setDependencies(drvExtPhyKsz8091MenuVisibleSingle, ["DRV_ETHPHY_USE_RESET_CALLBACK"])

	#Add to system_config.h
	drvExtPhyKsz8091HeaderFtl = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyKsz8091HeaderFtl.setSourcePath("driver/ethphy/config/drv_extphy_ksz8091.h.ftl")
	drvExtPhyKsz8091HeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
	drvExtPhyKsz8091HeaderFtl.setMarkup(True)
	drvExtPhyKsz8091HeaderFtl.setType("STRING")
		
	# file TCPIP_ETH_PHY_H "$HARMONY_VERSION_PATH/framework/driver/ethphy/drv_ethphy.h" to                     "$PROJECT_HEADER_FILES/framework/driver/ethphy/drv_ethphy.h"
	# Add drv_ethphy.h file to project
	drvExtPhyHeaderFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyHeaderFile.setSourcePath("driver/ethphy/drv_ethphy.h")
	drvExtPhyHeaderFile.setOutputName("drv_ethphy.h")
	drvExtPhyHeaderFile.setDestPath("driver/ethphy/")
	drvExtPhyHeaderFile.setProjectPath("config/" + configName + "/driver/ethphy/")
	drvExtPhyHeaderFile.setType("HEADER")
	drvExtPhyHeaderFile.setOverwrite(True)
	drvExtPhyHeaderFile.setEnabled(True)
	#drvEthPhyHeaderFile.setDependencies(drvGmacGenHeaderFile, ["TCPIP_USE_ETH_MAC"])

	# file TCPIP_ETH_PHY_LOCAL_H "$HARMONY_VERSION_PATH/framework/driver/ethphy/src/drv_ethphy_local.h" to           "$PROJECT_HEADER_FILES/framework/driver/ethphy/src/drv_ethphy_local.h"
	# Add drv_ethphy_local.h file to project
	drvExtPhyLocalHeaderFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyLocalHeaderFile.setSourcePath("driver/ethphy/src/drv_ethphy_local.h")
	drvExtPhyLocalHeaderFile.setOutputName("drv_ethphy_local.h")
	drvExtPhyLocalHeaderFile.setDestPath("driver/ethphy/src/")
	drvExtPhyLocalHeaderFile.setProjectPath("config/" + configName + "/driver/ethphy/src/")
	drvExtPhyLocalHeaderFile.setType("HEADER")
	drvExtPhyLocalHeaderFile.setOverwrite(True)
	drvExtPhyLocalHeaderFile.setEnabled(True)
	#drvEthPhyLocalHeaderFile.setDependencies(drvGmacGenHeaderFile, ["TCPIP_USE_ETH_MAC"])


	# file TCPIP_ETH_EXT_PHY_REGS_H "$HARMONY_VERSION_PATH/framework/driver/ethphy/src/dynamic/drv_extphy_regs.h" to    "$PROJECT_HEADER_FILES/framework/driver/ethphy/src/dynamic/drv_extphy_regs.h"
	# Add drv_extphy_regs.h file to project
	drvExtPhyKsz8091RegHeaderFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyKsz8091RegHeaderFile.setSourcePath("driver/ethphy/src/dynamic/drv_extphy_regs.h")
	drvExtPhyKsz8091RegHeaderFile.setOutputName("drv_extphy_regs.h")
	drvExtPhyKsz8091RegHeaderFile.setDestPath("driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091RegHeaderFile.setProjectPath("config/" + configName + "/driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091RegHeaderFile.setType("HEADER")
	drvExtPhyKsz8091RegHeaderFile.setOverwrite(True)
	drvExtPhyKsz8091RegHeaderFile.setEnabled(True)
	
	# Add drv_extphy_ksz8091.h file to project
	drvExtPhyKsz8091HeaderFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyKsz8091HeaderFile.setSourcePath("driver/ethphy/src/dynamic/drv_extphy_ksz8091.h")
	drvExtPhyKsz8091HeaderFile.setOutputName("drv_extphy_ksz8091.h")
	drvExtPhyKsz8091HeaderFile.setDestPath("driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091HeaderFile.setProjectPath("config/" + configName + "/driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091HeaderFile.setType("HEADER")
	drvExtPhyKsz8091HeaderFile.setOverwrite(True)
	drvExtPhyKsz8091HeaderFile.setEnabled(True)



	# file TCPIP_ETH_PHY_C "$HARMONY_VERSION_PATH/framework/driver/ethphy/src/dynamic/drv_ethphy.c" to         "$PROJECT_SOURCE_FILES/framework/driver/ethphy/drv_ethphy.c"
	# Add drv_ethphy.c file
	drvExtPhySourceFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhySourceFile.setSourcePath("driver/ethphy/src/dynamic/drv_ethphy.c")
	drvExtPhySourceFile.setOutputName("drv_ethphy.c")
	drvExtPhySourceFile.setOverwrite(True)
	drvExtPhySourceFile.setDestPath("driver/ethphy/src/dynamic/")
	drvExtPhySourceFile.setProjectPath("config/" + configName + "/driver/ethphy/src/dynamic/")
	drvExtPhySourceFile.setType("SOURCE")
	drvExtPhySourceFile.setEnabled(True)

	# Add drv_extphy_ksz8091.c file
	drvExtPhyKsz8091SourceFile = drvExtPhyKsz8091Component.createFileSymbol(None, None)
	drvExtPhyKsz8091SourceFile.setSourcePath("driver/ethphy/src/dynamic/drv_extphy_ksz8091.c")
	drvExtPhyKsz8091SourceFile.setOutputName("drv_extphy_ksz8091.c")
	drvExtPhyKsz8091SourceFile.setOverwrite(True)
	drvExtPhyKsz8091SourceFile.setDestPath("driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091SourceFile.setProjectPath("config/" + configName + "/driver/ethphy/src/dynamic/")
	drvExtPhyKsz8091SourceFile.setType("SOURCE")
	drvExtPhyKsz8091SourceFile.setEnabled(True)

	
def drvExtPhyKsz8091MenuVisibleSingle(symbol, event):
	if (event["value"] == True):
		print("EthMac Menu Visible.")		
		symbol.setVisible(True)
	else:
		print("EthMac Menu Invisible.")
		symbol.setVisible(False)
		