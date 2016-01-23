import os, csv

#The path to the script
currentPath = os.path.dirname(\
    os.path.abspath("__file__"))
print currentPath 

#Make the spreadsheet path 
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv


#Open the file
csvFile = open(outputCsv, "wb")

#Writing to the file
#csvFile.write('Testing on Friday again')
#csvFile.close()

# Create writer object
writer = csv.writer(csvFile, delimiter=',')
# Data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# All rows
rows = [row_1, row_2, row_3]

# Loop rows and write each
for row in rows:
    writer.writerow(row)



