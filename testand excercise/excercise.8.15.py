fhand1=open('mobx.txt.txt')
fhand=open(input("file name:\n"),'w')
count=1
for i in fhand1:
    if len(i)==0: continue
    if  not i.startswith("From"): continue
    v=i.split()
    print(count,v[1])
    
    
    fhand.write(str(count)+" "+v[1]+"\n")
    count+=1
fhand.close()

