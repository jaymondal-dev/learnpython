file=input("give the file name ;")
try:
    fhand=open(file)
except:
    print("give the correct value")
    exit()

s=dict()
for i in fhand:
    words=i.split()
    for i in words:
        s[i]=s.get(i,0)+1
print(s)

for keys in s:
    print(keys,s[keys])

li=list(s.keys())
li.sort()
for i in li:
    print(i,s[i])
