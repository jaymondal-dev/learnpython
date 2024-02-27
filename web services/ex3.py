import urllib.request
f=urllib.request.urlopen("https://www.thehindu.com/news/national/feeder/default.rss")
s=""
s=s+f
d=open("d.txt","w")
d.write(s)
d.close()