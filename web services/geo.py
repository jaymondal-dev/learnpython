import urllib.request, urllib.parse, urllib.error # importing necessary libray to connect with internet
import json
import ssl

api_key=42
serviceurl='http://py4e-data.dr-chuck.net/json?'
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

address=input('enter lcation : ')

parms=dict()
parms['address']=address
parms['key']=api_key
url=serviceurl+urllib.parse.urlencode(parms)
print('retieving', url)
uh=urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()
print('retrieved',len(data), 'characters')

js=json.loads(data)
print(json.dumps(js, indent=4))
lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)