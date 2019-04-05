import csv
exampleFile = open('example2.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row#' + str(exampleReader.line_num) + '' + str(row))
