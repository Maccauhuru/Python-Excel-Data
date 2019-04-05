import csv
tabSP = open('tabsp.tsv', 'w', newline="")
tabSPWriter = csv.writer(tabSP, delimiter='\t', lineterminator='\n\n')
tabSPWriter.writerow(['Riddim Name', 'Year', 'Rating', 'Producer'])
tabSPWriter.writerow(['Sick', '1996', '4.5', 'Dave Kelly'])
tabSPWriter.writerow(['Backpipe', '1998', '3.5', 'Stranger'])
tabSPWriter.writerow(['info', 'info', 'info', 'info', 'info', 'info'])
tabSP.close()
