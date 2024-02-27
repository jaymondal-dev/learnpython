fhand=open("mobx.txt.txt")
d=dict()
l=list()
for i in fhand:
    
    if i.startswith("From"):
        i=i.split()
        if len(i)>2:
            d[i[1]]=d.get(i[1],0)+1
#print(d)
for key,val in list(d.items()):
    l.append((val,key))
#print(l)
l.sort(reverse=True)
for k,v in l[:1]:
    print("most commited message is done by ",v,"and the number is",k)

