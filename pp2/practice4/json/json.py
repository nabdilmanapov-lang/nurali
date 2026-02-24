#Convert from JSON to Python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])

#Convert from Python to JSON:
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)

#Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a Python object containing all the legal data types:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,separators(".","=")))
print(json.dumps(x,indent=4,sort_keys=True))
