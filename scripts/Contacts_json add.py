import json

with open("data.json") as json_file:
    data = json.load(json_file)
    json_string = json.dumps(data)
print(json_string)