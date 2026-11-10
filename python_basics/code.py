import json

json_str = """{
  "name": "Rama",
  "age": 30,
  "wife": "Sita",
  "isKing": true,
  "expertice": ["wars", "strategist", "all"]
}
"""

py_obj = json.loads(json_str)
print(type(py_obj))
print(py_obj)

con = json.dumps(py_obj)

print(type(con))
print(con)
