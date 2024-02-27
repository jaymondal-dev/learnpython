fhand=open('mobx.txt.txt')
li=dict()
for i in fhand:
    
    if i.startswith("From"):
        
        #word=i.split()
        if len(i)>33:
           l=i.find("@")
           l2=i.find(" ",l)
           line=i[l:l2]
           print(line)
           li[line]=li.get(line,0)+1
            #print(word[2])
print(li)
for keys in li:
    print(keys,li[keys])       