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
csvFile.write('Checking to see if this works')
