import string
fhand=open("rmjl.txt")
di=dict()
li=list()
for i in fhand:
    line=i.translate(str.maketrans("","",string.punctuation))
    line=line.lower()
    line=line.split()
    for word in line :
        if word not in di:
            di[word]=1
        if word in di:
            di[word]+=1
for key,val in list(di.items()):
    li.append((val,key))
li.sort(reverse=True)
print(li[:1])