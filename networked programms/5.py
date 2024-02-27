import urllib.request,urllib.parse,urllib.error
d=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
c=dict()
for line in d:
    words=line.decode().split()
    for w in words:
        c[w]=c.get(w,0)+1
print(c)