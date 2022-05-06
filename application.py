from flask import Flask, app
from dotenv import dotenv_values
from flask_cors import CORS
import ml
import json
import numpy as np
import pandas as pd

config = dotenv_values(".env")
application = Flask(__name__)
CORS(application)

data = pd.read_json("./samFavoriteData.json")
@application.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/prediction")
def getPrediction():
    prediction = ml.corn("./lstm.h5", np.array(data["close"]))
    return str(prediction)

@application.route("/data")
def getData():
    f = open('btc.json')
    data = json.load(f)
    return data

if __name__=="__main__":
    application.run(host="0.0.0.0", port=5000)
