import urllib.error, urllib.parse, urllib.request
import ssl
import time
import json
import sqlite3


api_key=False
if api_key is False:
    api_key=42
    serviceurl="http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl="https://maps.googleapis.com/maps/api/geocode/json?"




ctx=ssl.create_default_context()
ctx.check_hostname=None
ctx.verify_mode=ssl.CERT_NONE


conn=sqlite3.connect("fe.sqlite")
cur=conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS locations (address TEXT geodata TEXT)''')



fh=open("where.data")
count=0


for line in fh:
    if count>200:
        print("Retrieved 200 locations, restart to retrieve more.")
        break

    address=line.strip()
    cur.execute("SELECT geodata FROM locations WHERE address=?",
                (memoryview(address.encode()),))
    
    try:
        data=cur.fetchone()[0]
        print("found in database ",address)
        continue
    except:
        pass

    parms=dict()
    parms["address"]=address
    if api_key is not False: parms['key']=api_key
    url=serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    print("Retrieved", len(data), 'characters',data[:20].replace("\n"," "))
    count=count+1

    try:
        js=json.loads(data)
    except:
        print(data)
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('====Failure To Retrieve ====')
        print(data)
        break

    cur.execute(''' INSERT INTO locations (address, geodata) VALUES (?,?)''',(memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()

    if count %10 ==0 :
        print('pausing for a bit .....')
    time.sleep(5)

print("done for geoload.py")
