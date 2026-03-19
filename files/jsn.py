import json
b = {"a" : 123, "asd" : 35}

with open("example.json", "w") as file:
    json.dump(b, file)
with open("example.json", "r") as file:
    
    a = json.load(file)
for key, items in a.items():
    print(f"{key} : {items}")