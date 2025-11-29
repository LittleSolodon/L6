import json
print("hello world")

with open("nothing here.json", 'r', encoding='utf-8') as file:
    print(json.loads(file.read()))