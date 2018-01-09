import json,requests
#import time
#import base64

url = 'https://koinex.in/api/ticker'
resp = requests.get(url)
data = json.loads(resp.text)
print "XRP:%s" %(data['prices']['XRP']) 
print "BTC:%s" %(data['prices']['BTC'])
