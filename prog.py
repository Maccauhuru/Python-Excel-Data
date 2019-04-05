import csv
exampleFile = open('example2.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
