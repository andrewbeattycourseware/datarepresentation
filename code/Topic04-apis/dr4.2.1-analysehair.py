from webbrowser import get
from valoffdao import getAll

data = getAll()
totalArea = 0
for entry in data:
    valuationReports = entry["ValuationReport"]
    #print(valuationReports)
    for valuationReport in valuationReports:
        #print(valuationReport)
        #if valuationReport["FloorUse"] == "HAIR SALON":
            #print (valuationReport["Area"],"+", totalArea,"=", end="")
        totalArea += valuationReport["Area"]
            #print(totalArea)

print (totalArea)