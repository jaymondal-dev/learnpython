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

stuff=ET.fromstring(data)
list=stuff.findall('users/user')
print(list)