#!/usr/bin/python3

import json,requests
#import time
#import base64

url = 'https://koinex.in/api/ticker'
url_bitBNS = 'https://bitbns.com/order/getTickerAll'
resp = requests.get(url)
resp_bitBNS = requests.get(url_bitBNS)
data = json.loads(resp.text)
data_bitBNS = json.loads(resp_bitBNS.text)
#print("XRP:\t%s\nBTC:\t%s" %(data['prices']['XRP'], data['prices']['BTC']))
print("\tKOINEX")
print("\t{}".format("=" * 6))
for coin in data['prices']:
    print("{}:\t{}".format(coin, data['prices'][coin]))
print("\n")
print("=" * 10)
print("\n\tBITBNS")
print("\t{}".format("=" * 6))
for coins_and_prices in data_bitBNS:
    for coin, prices in coins_and_prices.items():
        print(coin)
        for key, price in prices.items():
            print(key, price)

