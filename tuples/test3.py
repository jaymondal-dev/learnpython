import string
fhand=open("rmjl.txt")
di=dict()
for i in fhand:
    line=i.translate(str.maketrans("","",string.punctuation))
    line=line.lower()
    line2=line.split()
    for word in line2:
        if word not in di:
            di[word]=1
        else:
            di[word]+=1
li=list()
for key,val in list(di.items()):
    li.append((val,key))#concentrate on the usage of bracket
li.sort(reverse=True)
for key,val in li[:10]:
    print(key,val)