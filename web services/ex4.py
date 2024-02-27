import xml.etree.ElementTree as ET
data=''' 
<stuff>
<users>
<user x="2">
<id>001</id>
<name>chuck</name>
</user>
<user x="7">
<id>009</id>
<name>brent</name>
</user>
</users>
</stuff>'''

lst=ET.fromstring(data) #it converts the xml data into a string to parse.
list=lst.findall('users/user')
print("list of user",len(list))
a=1
d=open("fun.txt",'w')
for i in list:
    print("name",a, i.find('name').text)
    print("id",a, i.find('id').text)
    s=("name"+str(a)+"_"+i.find('name').text+" , "+"id"+str(a)+"_"+i.find('id').text+"\n")
    d.write(s)
    a=a+1
d.close()