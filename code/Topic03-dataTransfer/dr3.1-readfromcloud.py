import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
#with open("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

euroobject = data["bpi"]["EUR"]
rate = euroobject["rate"]
print(rate)


