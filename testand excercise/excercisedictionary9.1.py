s="dkhsjksdfneryenvbieru"
v=dict()
for i in s:
    if i not in v:
        v[i]=1
    if i in v:
        v[i]=v[i]+1
print(v)



