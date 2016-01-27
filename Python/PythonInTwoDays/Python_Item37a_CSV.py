import os, csv
# The path to the script
currentPath = os.path.dirname(os.path.abspath("__file__"))
print currentPath


# Make the spreadsheet path
outputCsv = currentPath + '/mydata.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, "wb")

### Writing to the file
##csvFile.write('Testing')

# Create writer object
writer = csv.writer(csvFile, delimiter=',')

# Data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# Write rows to csv
writer.writerow(row_1)
writer.writerow(row_2)
writer.writerow(row_3)
