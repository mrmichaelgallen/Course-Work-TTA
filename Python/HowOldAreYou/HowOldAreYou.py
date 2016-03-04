print("Let's see how long you have in days, minutes and seconds.")
name = input("What is your name: ")
print("Now enter your age.")
age = int(input("Age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
# Added in Leapyear days for greater accuracy
leapdayslived = age / 4
totaldays = days + leapdayslived
print(name, "has lived for", totaldays,"days", minutes, "minutes and", seconds,"seconds! WOW!")
      


