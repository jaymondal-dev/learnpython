import re
fhand=open("mobxshort.txt")
for line in fhand:
    line=line.rstrip()
    if re.search("^F..m", line):
        print(line)
