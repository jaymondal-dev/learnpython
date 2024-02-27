a=['a','d','f','h']
def chop(i):
    i[1:-1]
    return None
def middle(i):
    v=[]
    b=i[1:-1]
    v.extend(b)
    return v
print(chop(a))
print(middle(a))