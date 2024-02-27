f=input("give the file name : ")
if f=="na na boo boo":
    print("got you")
    exit()
else:
    
    fhand=open(f)
    count=0
    for i in fhand:
        if i.startswith("From"):
            count=count+1
print("total account name is",count)