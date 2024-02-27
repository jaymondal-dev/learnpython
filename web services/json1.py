import json
data='''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

stuff=json.loads(data)
for i in stuff:
    print(i['name'])
    print(i['id'])
    print(i['x'])
