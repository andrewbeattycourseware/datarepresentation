import json
filename = "dr2.4-json.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)
#print (jsonobject)
for employee in jsonobject["employees"]:
    print(employee["firstName"])
