import re
fhand=open("m.txt")
for line in fhand:
    lne=line.rstrip()
    if re.search('^X\S+: [0-9.]+',lne): #Translating this, we are saying, we want lines that start with X-, followed by zero or more characters (.*), followed by a colon (:) and then a space. After the space we are looking for one or more characters that are either a digit (0-9) or a period [0-9.]+. Note that inside the square brackets, the period matches an actual period (i.e., it is not a wildcard between the square brackets).
        print(lne)