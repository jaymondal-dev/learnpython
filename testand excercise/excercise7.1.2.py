file=input("give me the file name: ")
f=open(file)
count=0
x=0.0
for i in f:
    i.rstrip()
    if i.startswith("X-DSPAM-Confidence:"):
        #print(i)
        count=count+1
        y=i.find(":")
        
        x=x+float(i[y+1:])
print(count)
print("average spam ",x/count)