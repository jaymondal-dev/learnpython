fhand=open('m.txt')
for line in fhand:
    line=line.rstrip()
    if line.find("From") >=0:
        print(line)

print("done with conditional loop")

import re
f=open("j.txt")
for line in f:
    line=line.rstrip()
    if re.search("^F..m:", line):
        print(line)
