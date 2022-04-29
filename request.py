import requests
import json
import csv
from dotenv import dotenv_values

config = dotenv_values(".env")
POLYGON_API = config["POLYGON_API"]
baseURL = "https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/range/1/day/2020-01-01/2023-02-23?apiKey={}".format(POLYGON_API)
result = requests.get(baseURL)
jsonData = json.loads(result.text)
with open('btc.json', 'w') as cryptoFile:
    cryptoFile.write(result.text)

cryptoFile.close();
