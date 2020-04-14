# Python-Web-API
# v.1.0.0

import os
import json

class options():
    #Program Text
    PROGRAM_NAME = """
 _                                            _  ___ 
|_)    _|_ |_   _  ._   \    /  _  |_    /\  |_)  |  
|   \/  |_ | | (_) | |   \/\/  (/_ |_)  /--\ |   _|_ 
    /                                                 
v.1.0.0
	"""

    #Default Values
    DETAIL_PRINT_TEXT = "DETAIL_PRINT"
    DETAIL_PRINT_VALUE = "1"

    HOST_TEXT = "HOST_VALUE"
    HOST_VALUE = "0.0.0.0"

    PIN_TEXT = "PIN_VALUE"
    PIN_VALUE = 17

    TIME_TEXT = "TIME_VALUE"
    TIME_VALUE = 3

    #FOLDER Setup
    OP_ROOT_FOLDER_PATH_TEXT = "OP_ROOT_FOLDER_PATH"
    OP_ROOT_FOLDER_PATH_VALUE = "\\"

    OP_ROOT_FOLDER_NAME_TEXT = "OP_ROOT_FOLDER_NAME"
    OP_ROOT_FOLDER_NAME_VALUE = "python-web-api\\"

	#Config filename
    OP_ROOT_CONFIG = "python-web-api.config"

    def root_path(self):
        return os.path.abspath(os.sep)

    #Global Functions
    def printText(self, text, override):
	    if int(self.DETAIL_PRINT_VALUE) == 1:
	    	print(text)
	    else:
		    if override == True:
		    	print(text)

    def createRootfolder(self):
        self.OP_ROOT_FOLDER_PATH_VALUE = self.root_path()
        self.OP_ROOT_FOLDER_PATH_VALUE = self.OP_ROOT_FOLDER_PATH_VALUE + self.OP_ROOT_FOLDER_NAME_VALUE
        self.createFolder(self.OP_ROOT_FOLDER_PATH_VALUE)

        #Setting up full path starting
        self.OP_ROOT_CONFIG = self.OP_ROOT_FOLDER_PATH_VALUE + self.OP_ROOT_CONFIG
        self.printText("+ Config file are loacted {}".format(self.OP_ROOT_CONFIG), False)

    def createFolder(self, folder):
        if not os.path.exists(folder):
            os.mkdir(folder)
            self.printText("+ Folder created: {}".format(folder), True)
        else:
            self.printText("+ Folder loacted: {}".format(folder), True)

    def saveJSON(self):
        self.printText("+ Config export started", False)
        DATA = {}
        DATA['WEBAPI'] = []
        DATA['WEBAPI'].append({
            self.DETAIL_PRINT_TEXT : self.DETAIL_PRINT_VALUE,
            self.HOST_TEXT : self.HOST_VALUE,
            self.PIN_TEXT : self.PIN_VALUE,
            self.TIME_TEXT : self.TIME_VALUE
        })

        if os.path.exists(self.OP_ROOT_CONFIG):
            self.printText("+ File: {} exist, deleting it.".format(self.OP_ROOT_CONFIG), False)
            os.remove(self.OP_ROOT_CONFIG)

        with open(self.OP_ROOT_CONFIG, 'w') as outfile:
            json.dump(DATA, outfile)

        self.printText("+ Config export end", False)

    def setupJSON(self, export):
        if export == True:
            self.saveJSON()

        else:
            self.printText("+ Config import started", True)
            if os.path.exists(self.OP_ROOT_CONFIG):
                with open(self.OP_ROOT_CONFIG) as json_file:
                    data = json.load(json_file)
                    for p in data['WEBAPI']:
                        self.DETAIL_PRINT_VALUE = int(p[self.DETAIL_PRINT_TEXT])
                        self.HOST_VALUE = p[self.HOST_TEXT]
                        self.PIN_VALUE = int(p[self.PIN_TEXT])
                        self.TIME_VALUE = int(p[self.TIME_TEXT])

                        self.printText("+ {} are set to: {}".format(self.DETAIL_PRINT_TEXT, self.DETAIL_PRINT_VALUE), False)
                        self.printText("+ {} are set to: {}".format(self.HOST_TEXT, self.HOST_VALUE), False)   
                        self.printText("+ {} are set to: {}".format(self.PIN_TEXT, self.PIN_VALUE), False)  
                        self.printText("+ {} are set to: {}".format(self.TIME_TEXT, self.TIME_VALUE), False)   
       
            else:
                self.printText("+ Config file dosent exist - using standard", False)
                self.saveJSON()
                
        self.printText("+ Config import end", False)

    def __init__(self):
		#Starting up
        print(self.PROGRAM_NAME)
        print("+ Text Libray loaded")

        #Loading Default Value
        self.createRootfolder()
        self.setupJSON(False)
        
