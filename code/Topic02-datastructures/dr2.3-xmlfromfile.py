from xml.dom.minidom import parse

filename = "employees.xml"

# read file in two ways
doc = parse(filename)
# or
#with open(filename) as fp:
#    doc = parse(fp)

emloyeeNodeList = doc.getElementsByTagName("Employee")
print(len(emloyeeNodeList))
for employeeNode in emloyeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print (firstName)
