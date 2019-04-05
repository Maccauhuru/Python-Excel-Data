import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Holding Firm', 'Chant Dem Down',
                       'Deep Cover', 'Seek The Word'])
outputWriter.writerow(
    ['Hello,world!', 'Babylon', 'Tell Them Again', 'Algorithms'])
outputWriter.writerow([1, 2, 3, 4])
outputFile.close()
