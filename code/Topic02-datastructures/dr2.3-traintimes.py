
from xml.dom.minidom import parseString
import requests
import csv

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# check it works
print (doc.toprettyxml(), end='') #output to console

# if I want to store the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)


# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with  open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        #print (traincode)

        # now lets get everything
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        
        # instead of printing this you could output to another format
        #print (dataList)
        # for example a CSV file  
        train_writer.writerow(dataList)

