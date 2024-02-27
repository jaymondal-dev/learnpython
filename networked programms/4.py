import urllib.request
f=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
s=""
for line in f:
    print(line.decode().strip())
    s1=line.decode()
    s=s+str(s1)
d=open("d.txt","w")
d.write(s)
d.close()
