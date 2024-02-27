
x1=0
y=0
while True:
    
    x=input("number..")
    if x=="done":
        break
    else:
        try:
            x1=float(x)+x1
            y=y+1
        except:
            print("give a valid number")
            continue
print("sum",x1)
print("count",y)       
        
print("average",x1/y)