import re
fhand=open(input("give the file name >>>>>> "))
for line in fhand:
    line=line.rstrip()
    lst=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if len(lst)>0:
        print(lst)