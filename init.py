from flask import Flask, app
from dotenv import dotenv_values
from flask_cors import CORS
import json

config = dotenv_values(".env")
application = Flask(__name__)
CORS(application)

@application.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/prediction")
def getPrediction():
    return str(50000)

@application.route("/data")
def getData():
    f = open('btc.json')
    data = json.load(f)
    return data

if __name__=="__main__":
    application.run()
