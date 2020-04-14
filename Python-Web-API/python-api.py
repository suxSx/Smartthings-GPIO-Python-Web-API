# Gold Number Finder
# v.1.1.1

#Local Repo
from options import options

#Ext Repo
from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask.views import MethodView

class HomeApi(MethodView):
    """ / """

    def get(self):
        return "<h1>Python Web API</h1><p>This site is a prototype API for controlling GPIO on Raspberry PI 3 B+</p>"

    def delete(self):
        return "<h1>Home - Delete</h1><p>Sorry nothing to delete here.</p>"

class doorApi(MethodView):
    """ /door/<action> """

    #Error Messages
    error = {
        "404": {
            "errorCode": "404",
            "errorMessage": "Action Not Found, the command you tried does not exist."
        },
        "notor": {
            "errorCode": "666",
            "errorMessage": "Well this was unnexpeted, the error message does not exist or is from this world. You are really luck, this is a one in a life time experience!"
        }
    }

    doorMsg = {
        "open": {
            "doorCode": "1337",
            "doorMessage": "Signal for opening sendt"
        },

        "close": {
            "doorCode": "7331",
            "doorMessage": "Open signal terminated"
        },

        "comming": {
            "doorCode": "8888", 
            "doorMessage": "This function is still in development"
        },

        "running": {
            "doorCode": "007", 
            "doorMessage": "The server are up and running"
        }
    }

    def get(self, action):
        if action == "open":
            #Fucntion for opening the door
            print("Action for opening door have been triggered")
            return make_response(jsonify(self.doorMsg["comming"]), 400) 

        if action == "status":
            #Function for status
            return make_response(jsonify(self.doorMsg["running"]), 400)

        if action == "666":
            return make_response(jsonify(self.error["notor"]), 400)
        
        if action == "":
            return make_response(jsonify(self.error["notor"]), 400)

        else:
            #Action for error
            return make_response(jsonify(self.error["404"]), 400)

    def delete(self):
        return make_response(jsonify(self.doorMsg["comming"]), 400)

if __name__ == '__main__':
    #Adding options
    op = options()

    #Setup API server
    op.printText("\n+ Setting up API server", True)
    app = Flask(__name__)

    op.printText("+ Adding endpoint: Home", True)
    app.add_url_rule("/", view_func=HomeApi.as_view("home_page"))

    op.printText("+ Adding endpoint: Door", True)
    app.add_url_rule("/door/<action>", view_func=doorApi.as_view("door_page"))

    op.printText("+ Running Flask\n", True)
    app.run(host= op.HOST_VALUE)