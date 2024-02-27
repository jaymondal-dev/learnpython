file=input("give the file name: ")
fhand=open(file)
count=0
for i in fhand:
    if i.startswith("From"):
        count=count+1
print("total account name is",count)


