fhand=open('mobx.txt.txt')
li=dict()
for i in fhand:
    
    if i.startswith("From"):
        
        word=i.split()
        if len(word)>2:
            li[word[2]]=li.get(word[2],0)+1
            #print(word[2])
        
        
    
        

print(li)