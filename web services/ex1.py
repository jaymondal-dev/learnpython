import xml.etree.ElementTree as et
data='''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''
tree=et.fromstring(data)
print('Name:',tree.find('name').text)
print("email:",tree.find('email').get('hide'))