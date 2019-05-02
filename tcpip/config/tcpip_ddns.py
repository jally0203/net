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

    
def instantiateComponent(tcpipDdnsComponent):
	print("TCPIP DNS Client Component")
	configName = Variables.get("__CONFIGURATION_NAME")
	
	# Enable Dynamis DNS Module
	tcpipDdns = tcpipDdnsComponent.createBooleanSymbol("TCPIP_USE_DDNS", None)
	tcpipDdns.setLabel("Dynamic DNS Module")
	tcpipDdns.setVisible(False)
	tcpipDdns.setDescription("Enable Dynamic DNS Module")
	tcpipDdns.setDefaultValue(True)
	#tcpipDdns.setDependencies(tcpipDdnsMenuVisible, ["tcpipIPv4.TCPIP_STACK_USE_IPV4", "tcpipUdp.TCPIP_USE_UDP"])

	# Default CheckIP server for Determining Current IP Address
	tcpipDdnsChkIpServer = tcpipDdnsComponent.createStringSymbol("TCPIP_DDNS_CHECKIP_SERVER", None)
	tcpipDdnsChkIpServer.setLabel("Default CheckIP server for Determining Current IP Address")
	tcpipDdnsChkIpServer.setVisible(True)
	tcpipDdnsChkIpServer.setDescription("Default CheckIP server for Determining Current IP Address")
	tcpipDdnsChkIpServer.setDefaultValue("checkip.dyndns.com")
	#tcpipDdnsChkIpServer.setDependencies(tcpipDdnsMenuVisible, ["TCPIP_USE_DDNS"])

	# Dynamic DNS Task Rate in msec
	tcpipDdnsTskRate = tcpipDdnsComponent.createIntegerSymbol("TCPIP_DDNS_TASK_TICK_RATE", None)
	tcpipDdnsTskRate.setLabel("dynDNS Task Rate in msec")
	tcpipDdnsTskRate.setVisible(True)
	tcpipDdnsTskRate.setDescription("Dynamic DNS Task Rate in msec")
	tcpipDdnsTskRate.setDefaultValue(777)
	#tcpipDdnsTskRate.setDependencies(tcpipDdnsMenuVisible, ["TCPIP_USE_DDNS"])
	
	# Add to system_config.h
	tcpipDdnsHeaderFtl = tcpipDdnsComponent.createFileSymbol(None, None)
	tcpipDdnsHeaderFtl.setSourcePath("tcpip/config/ddns.h.ftl")
	tcpipDdnsHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
	tcpipDdnsHeaderFtl.setMarkup(True)
	tcpipDdnsHeaderFtl.setType("STRING")

	# Add ddns.c file
	tcpipDdnsSourceFile = tcpipDdnsComponent.createFileSymbol(None, None)
	tcpipDdnsSourceFile.setSourcePath("tcpip/src/ddns.c")
	tcpipDdnsSourceFile.setOutputName("ddns.c")
	tcpipDdnsSourceFile.setOverwrite(True)
	tcpipDdnsSourceFile.setDestPath("library/tcpip/src/")
	tcpipDdnsSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
	tcpipDdnsSourceFile.setType("SOURCE")
	tcpipDdnsSourceFile.setEnabled(True)
	#tcpipDdnsSourceFile.setDependencies(tcpipDdnsGenSourceFile, ["TCPIP_USE_DDNS"])

# make Dynamic DNS module option visible

def tcpipDdnsMenuVisible(symbol, event):
	if (event["value"] == True):
		print("DDNS Menu Visible.")		
		symbol.setVisible(True)
	else:
		print("DDNS Menu Invisible.")
		symbol.setVisible(False)	

		
def tcpipDdnsGenSourceFile(sourceFile, event):
	sourceFile.setEnabled(event["value"])
	

def destroyComponent(component):
	Database.setSymbolValue("tcpipDdns", "TCPIP_USE_DDNS", False, 2)