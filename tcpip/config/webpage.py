global ORG_PATH
global webpageListFile
global count
global webPagePathParsing
global tcpipHttpNetWebPageDirMyPath
global createWebPageFileSymbol
global clearFileSymbols
global mytcpipHttpNetComponent
global symbolList


#Disable all the file symbols
def clearFileSymbols():
	for symbol in symbolList:
		symbol.setEnabled(False)

#Return File symbols from the Symbol list.
def createWebPageFileSymbol(count):
	return symbolList[count]

#Callback function which is called when there is a path configuration from MHC
def tcpipHttpNetWebServerMyPathVisible(sym, event):
	ORG_PATH = event["value"]
	webPagePathParsing(ORG_PATH)

tcpipHttpNetWebPageDirMyPath = tcpipHttpNetComponent.createStringSymbol("TCPIP_HTTP_NET_WEBPAGE_DIRECTORY_MYPATH", tcpipHttpNetCustTemplate)
tcpipHttpNetWebPageDirMyPath.setLabel("Configure Webpage directory path")
tcpipHttpNetWebPageDirMyPath.setVisible(False)
tcpipHttpNetWebPageDirMyPath.setDescription("Configure Webpage directory path")
tcpipHttpNetWebPageDirMyPath.setDefaultValue(Module.getPath() + "web_pages")
tcpipHttpNetWebPageDirMyPath.setDependencies(tcpipHttpNetWebServerMyPathVisible, ["TCPIP_HTTP_NET_WEBPAGE_DIRECTORY_PATH"])

def webPagePathParsing(path):
	import re
	import os
	import sys

	count = 0
	# Get the Root PATH 
	ORG_PATH = path
	clearFileSymbols()
	for (root, dirs, fileNames) in os.walk(ORG_PATH):
		for fileName in fileNames:
			file = os.path.join(root,fileName)
			#file = file[file.find(ORG_PATH):]
			#Replace the module path from the Root path with empty string
			file = file.replace(Module.path, "")
			sepWebpageDir = file[file.find(os.path.sep):]
			htmFile = sepWebpageDir.replace(os.path.sep, "",1)
			# Get the Webpage file symbol and each symbol is for the each file
			webpageListFile = createWebPageFileSymbol(count)
			#Set the source path
			webpageListFile.setSourcePath(file)
			webpageListFile.setOutputName(htmFile)
			
			fileList = file.split(os.path.sep)
			#set the destination path , the location where the webpage file will be copied
			#destPath = ".."+os.path.sep+".."+os.path.sep+fileList[0]
			destPath = ".."+os.path.sep+".."+os.path.sep+"web_pages"
			#print("destination path: "+ destPath)
			webpageListFile.setDestPath(destPath)
			fileList = fileList[0:len(fileList)-1]
			folderPath = ""
			for fileStr in fileList:
				folderPath += fileStr+os.path.sep
			#set the project path , Webpage diretory will be added to the project	
			webpageListFile.setProjectPath(folderPath)
			webpageListFile.setType("SOURCE")
			webpageListFile.setMarkup(False)
			webpageListFile.setEnabled(True)
			count += 1



#ORG_PATH = "../src/web_pages"
ORG_PATH = Module.getPath() + "web_pages"
tcpipHttpNetWebDirSymbol = tcpipHttpNetWebPageDirPath.getValue()
ORG_PATH = tcpipHttpNetWebDirSymbol
count = 0

mytcpipHttpNetComponent = tcpipHttpNetComponent
symbolList = []
fileCount = 0
MAX_NUMBER_WEBPAGE_FILES = 100
del symbolList[:]

#Create MAX_NUMBER_WEBPAGE_FILES file symbols during the instantiation . 
#use of createFileSymbol() is not possible during the dynamic configuration of webPage path configuration
#So due to that we create a max number of webpage files during componet instatiation

for fileCount in range(MAX_NUMBER_WEBPAGE_FILES):
	webPageSymbolStr = "WEBPAGE_LIST_FILE"+str(fileCount)
	mySym = tcpipHttpNetComponent.createFileSymbol(webPageSymbolStr, None)
	mySym.setEnabled(False)
	symbolList.append(mySym)
	fileCount +=1

#default webapge path and diretory parsing
webPagePathParsing(ORG_PATH)
