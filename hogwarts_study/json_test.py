import json

data = {
    "name": ["jerry", 'nickname'],
    "age": 25,
    "gender": "female"
}

data1 = json.dumps(data)
print(data)
print(type(data))
print(data1)
print(type(data1))
data2=json.loads(data1)
print(data2)
print(type(data2))