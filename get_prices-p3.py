#!/usr/bin/python3

import json,requests
#import time
#import base64

url = 'https://koinex.in/api/ticker'
resp = requests.get(url)
data = json.loads(resp.text)
#print("XRP:\t%s\nBTC:\t%s" %(data['prices']['XRP'], data['prices']['BTC']))
for coin in data['prices']:
    print("{}:\t{}".format(coin, data['prices'][coin]))

