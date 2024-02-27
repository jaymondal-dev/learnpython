import re
fhand=open("m.txt")
b=0
c=0
for line in fhand:
    line=line.rstrip()
    t=re.findall("^X\S+: ([0-9.]+)",line)
    if len(t)>0:
        print(t)
        a=float(t[0])
        b=b+a
        c=c+1

print(b/c)
        
  