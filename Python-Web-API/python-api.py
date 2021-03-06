# Python-Web-API
# v.1.0.0

#Local Repo
from options import options

#Web service
from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask.views import MethodView

#GPIO 
import RPi.GPIO as GPIO

#Ext REPO
import time

#Adding options
op = options()

#GPIO COMMANDS
def setupGPIO(PIN):
    # which naming convention is to be used.
    GPIO.setmode(GPIO.BCM)

    # Open the pin #DEFAULT = 17
    op.printText("+ SETUP FOR GPIO {} STARTED".format(PIN), False)
    GPIO.setup(PIN, GPIO.OUT)

    # Turning it off
    GPIO.output(PIN, GPIO.LOW)
    op.printText("+ GPIO {} TURNED OFF".format(PIN), False)
    op.printText("+ SETUP FOR GPIO {} ENDED".format(PIN), False)

def turnPINON(PIN, TIME):
    #Turn on
    op.printText("+ TURNING GPIO {} ON".format(PIN), False)
    GPIO.output(PIN, GPIO.HIGH)

    #Sleep for X. DEFAULT = 3
    op.printText("+ SLEEPING FOR {}".format(TIME), False)
    time.sleep(TIME)

    #Turn off. 
    op.printText("+ TURNING GPIO {} OFF".format(PIN), False)
    GPIO.output(PIN, GPIO.LOW)

def turnPINOF(PIN):
    op.printText("+ TURNING GPIO {} OFF".format(PIN), False)
    GPIO.output(PIN, GPIO.LOW)

class HomeApi(MethodView):
    """ / """

    def get(self):
        return "<h1>Python Web API</h1><p>This site is a prototype API for controlling GPIO on Raspberry PI 3 B+</p>"

    def delete(self):
        return "<h1>Home - Delete</h1><p>Sorry nothing to delete here.</p>"

class doorApi(MethodView):
    """ /door/<action> """
       
    def get(self, action):
        if action == "open":
            #Fucntion for opening the door
            op.printText("\n- Action for opening door have been triggered", False)
            turnPINON(op.PIN_VALUE, op.TIME_VALUE)
            op.printText("+ Action for opening door ended\n", False)

            return make_response(jsonify(op.doorMsg["open"]), 400) 

        if action == "close":
            #Function for closing
            op.printText("\n- Action for closing door have been triggered", False)
            turnPINOF(op.PIN_VALUE)
            op.printText("+ Action for closing door ended\n", False)
            return make_response(jsonify(op.doorMsg["close"]), 400)

        if action == "status":
            #Function for status
            return make_response(jsonify(op.doorMsg["running"]), 400)

        if action == "666":
            return make_response(jsonify(op.error["notor"]), 400)
        
        if action == "":
            return make_response(jsonify(op.error["notor"]), 400)

        else:
            #Action for error
            return make_response(jsonify(op.error["404"]), 400)

    def delete(self):
        return make_response(jsonify(op.doorMsg["comming"]), 400)

if __name__ == '__main__':
    #Setup API server
    op.printText("\n+ Setting up API server", True)
    app = Flask(__name__)

    op.printText("+ Setting up GPIO", True)
    setupGPIO(op.PIN_VALUE)

    op.printText("+ Adding endpoint: Home", True)
    app.add_url_rule("/", view_func=HomeApi.as_view("home_page"))

    op.printText("+ Adding endpoint: Door", True)
    app.add_url_rule("/door/<action>", view_func=doorApi.as_view("door_page"))

    op.printText("+ Running Flask\n", True)
    app.run(host= op.HOST_VALUE)

    op.printText("\n+ Cleaning up before exit", True)
    GPIO.cleanup()