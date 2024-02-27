import urllib.parse,urllib.error,urllib.request
fhand=urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
f=open('cover.jpg','wb')
size=0
while True:
    data=fhand.read(1000)
    if len(data)<1:break
    size=size+1
    f.write(data)
print("total data length",size)
f.close()