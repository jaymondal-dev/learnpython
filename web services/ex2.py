import xml.etree.ElementTree as ET
input=''' 
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
stuff=ET.fromstring(input) #creating a string out of the xml data so that we can parse it 
list=stuff.findall('users/user')
print('user count :',len(lst))
for item in list:
    print('name',item.find('name').text)
    print('id',item.find('id').text)
    print('attribute',item.get('x'))