import requests
import json
import time

response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
# res = response.status_code
currencyData = response.json()

currencyTag = currencyData['data']['base']
currencyPrice = currencyData['data']['amount']

print (currencyTag + ' ' + currencyPrice)

# data = response.json()
# currency = ['data']['base']
# price = data
# print(f"Currency: {currency} Price: {price}.")
# time.sleep(5)