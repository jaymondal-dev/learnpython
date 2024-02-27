import re
fhand=open(input("give the file name >>>>>> "))
for line in fhand:
    line=line.rstrip()
    lst=re.findall('\S+@\S+',line)
    if len(lst)>0:
        print(lst)