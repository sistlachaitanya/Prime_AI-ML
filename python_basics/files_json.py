import json

data = {
    "name": "Rama",
    "age": 30,
    "wife": "Sita",
    "isKing": True,
    "expertice": ["wars", "strategist", "all"],
}

with open("sdf.json", "w") as f:
    data = json.dump(data, f, indent=4, sort_keys=True)
