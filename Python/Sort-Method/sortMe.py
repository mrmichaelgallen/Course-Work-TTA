def sortMethod(sortMe):
    sortDone = []
    while sortMe: 
        lowestNumber = sortMe[0]
        for x in sortMe: 
            if x < lowestNumber:
                lowestNumber = x
        sortDone.append(lowestNumber)
        sortMe.remove(lowestNumber)  
    return sortDone

x = [67, 45, 2, 13, 1, 998]
y = [89, 23, 33, 45, 10, 12, 45, 45, 45]

print sortMethod(x)
print sortMethod(y)
