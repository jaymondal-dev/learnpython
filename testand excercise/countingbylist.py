numlist=list()
while True:
    inp=input("print number in integer: ")
    if inp=="done":
        break
    a=float(inp)
    numlist.append(a)

print("sum",sum(numlist))
print("len",len(numlist))
print("average",sum(numlist)/len(numlist))
