
colnames=['id','name','age']
result=(1,"mary", 21)
item = {}

for i, colName in enumerate(colnames):
    value = result[i]
    item[colName] = value

print(item)
