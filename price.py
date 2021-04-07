import requests
import json
import gspread
import time
import cbpro
from oauth2client.service_account import ServiceAccountCredentials

#Create client to access Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#Create cbpro python SDK clients: https://github.com/danpaquin/coinbasepro-python
public_client = cbpro.PublicClient()
# auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)

output = public_client.get_products()
print(output)

# authtest = auth_client.get_accounts()
# print(authtest)

#Search for currencies by name and feed their price into a list
coinList = ["BTC", "ETH", "LINK"]
priceList = []
for i in range (0, len(coinList)):   
    url = 'https://api.coinbase.com/v2/prices/%s-USD/spot' % (coinList[i])
    response = requests.get(url)
    currency_data = response.json()
    currency_tag = currency_data['data']['base']
    currency_price = currency_data['data']['amount']
    priceList.append(currency_price)

print (coinList)
print (priceList)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Finance").get_worksheet(1)

tag_cell = sheet.find("BTC") #Start with BTC

for i in range(len(coinList)):
    tag_increment_col = tag_cell.col + (1)
    tag_increment_row = tag_cell.row + i
    sheet.update_cell
    sheet.update_cell(tag_increment_row, tag_increment_col, priceList[i])