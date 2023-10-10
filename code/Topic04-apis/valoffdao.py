import urllib.parse
import requests
import json
url = "https://api.valoff.ie/api/Property/GetProperties"

parameterasDict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG%,Use,FloorUse,Address,PublicationDate"   
}

def getAll():
    parameters = urllib.parse.urlencode(parameterasDict)
    #print (parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    return response.json()

if __name__ == "__main__":
    with open("valoff.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)