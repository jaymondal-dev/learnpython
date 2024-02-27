fhand=open("words.txt")
n=dict()
for i in fhand:
    word=i.split()
    for i in word:
        n[i]=n.get(i,0)+1
print(n)