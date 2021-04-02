import requests
import json

coinList = ["BTC", "ETH", "LINK"]
for i in range (0, len(coinList)):   
    url = 'https://api.coinbase.com/v2/prices/%s-USD/spot' % (coinList[i])
    response = requests.get(url)
    currency_data = response.json()
    currency_tag = currency_data['data']['base']
    currency_price = currency_data['data']['amount']
    print (currency_tag + ' ' + currency_price)