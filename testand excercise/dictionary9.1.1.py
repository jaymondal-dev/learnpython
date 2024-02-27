fhand=open("words.txt")
re=dict()
for i in fhand:
    word=i.split()
    print(word)
    for i in word:
        if i not in re:
            re[i]=1
        if i in re:
            re[i]=re[i]+1
print(re)


n=dict()
for i in fhand:
    word=i.split()
    for i in word:
        n[i]=n.get(i,0)+1
print(n)
