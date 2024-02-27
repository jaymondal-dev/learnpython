count=0
for i in  [3, 41, 12, 9, 74, 15]:
    count=count+1
print(count)

total=0
for i in  [3, 41, 12, 9, 74, 15]:
    total=total+i
print(total)

largest=None
print("before value",largest)
for i in  [3, 41, 12, 9, 74, 15]:
    if largest is None or i>largest:
        largest=i
        print("loop: ",largest," for ",i)
print("end loop",largest)

small=None
print("before value",small)
for i in  [3, 41, 12, 9, 74, 15]:
    if small is None or i<small:
        small=i
        print("loop: ",small," for ",i)
print("end loop",small)