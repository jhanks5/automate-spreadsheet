import requests
import json
import time


response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
data = response.json
currency = data["data"]["base"]
price = data["data"]["amount"]
print(f"Currency: {currency} Price: {price}.")
time.sleep(5)