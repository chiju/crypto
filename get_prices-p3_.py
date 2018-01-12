import json,requests
#import time
#import base64

url = 'https://koinex.in/api/ticker'
url_bitBNS = 'https://bitbns.com/order/getTickerAll'
resp = requests.get(url)
resp_bitBNS = requests.get(url_bitBNS)
data = json.loads(resp.text)
data_bitBNS = json.loads(resp_bitBNS.text)
print("{}\t{}\t\t\t{}".format('COIN', 'KOINEX', 'BITBNS'))
print("\t\t\tSELL\tBUY\tLAST")
for coin, prices in data['prices'].items():
    for coins_and_prices in data_bitBNS:
        for coin_bitBNS, prices_bitBNS in coins_and_prices.items():
            if coin == coin_bitBNS:
                print("{}\t{}\t{} {} {}".format(coin, prices, *prices_bitBNS.values()))
    if coin not in ['BTC', 'XRP']:
        print("{}\t{}".format(coin, prices))

            
