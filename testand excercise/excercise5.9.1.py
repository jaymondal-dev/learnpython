x=input("give the list: \n >>>>>")
List=list(x)
largest=None
smallest=None
for i in List:
    if largest is None or i>largest:
        largest=i
    elif smallest is None or i<smallest:
        smallest=i
print("largest >",largest)
print("smallest >",smallest)
