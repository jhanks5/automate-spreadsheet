import pip
import subprocess
import sys

def install(coinbase):
    subprocess.check_call([sys.executable, "-m", "pip", "install", coinbase])

from coinbase.wallet.client import Client

with open ("/Users/jameshanks/PersonalProj/CoinbaseRegAPI/pubKey.txt") as pub:
    pubKey = pub.readlines()

with open ("/Users/jameshanks/PersonalProj/CoinbaseRegAPI/secretKey.txt") as priv:
    apiSecret = priv.readlines()

client = Client(pubKey, apiSecret, api_version='YYYY-MM-DD')

currency_code = 'USD'  # can also use EUR, CAD, etc.

# Make the request
price = client.get_spot_price(currency=currency_code)

print 'Current bitcoin price in %s: %s' % (currency_code, price.amount)
