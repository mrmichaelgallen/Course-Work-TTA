###
### 2. Python Quick Start
###

# Selecting code with conditionals

# a, b = 0, 1
#
# if a < b:
#     print('a ({}) is less than b ({})'.format(a, b))
# else:
#     print('a ({}) is not less than b ({})'.format(a, b))
#
# print("foo" if a < b else "bar")

##
## Repeating code with a loop
##

# # simple fibonacci series
#
# a, b = 0, 1
# while b < 50:
#     print(b)
#     a, b = b, a + b
#
# print("Done")
#
# # for loop which works with iterators
# fh = open('lines.text')
# for line in fh.readlines()
#     print(line)

##
## Reusing code with a function
##

# def isprime(n):
#     if n == 1:
#         print("1 is special")
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             print("{} equals {} x {}".format(n, x, n // x))
#             return False
#     else:
#         print(n, "is a prime number")
#         return True
#
# for n in range(1, 30):
#     isprime(n)

##
## Creating sequence with generator functions
##

# def isprime(n):
#     if n == 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     else:
#         return True
#
# def primes(n = 1):
#     while(True):
#         if isprime(n): yield n
#         n += 1
#
# for n in primes():
#     if n > 100: break
#     print(n)

##
## Reusing code and data with a class
##

# class Fibonacci():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def series(self):
#         while(True):
#             yield(self.b)
#             self.a, self.b = self.b, self.a + self.b
#
# f = Fibonacci(0, 1)
# for r in f.series():
#     if r > 100: break
#     print(r, end = '  ')


##
## Greater reusability with inheritance and polymorphism
##

# class AnimalActions:
#     def quack(self): return self.strings['quack']
#     def feathers(self): return self.strings['feathers']
#     def bark(self): return self.strings['bark']
#     def fur(self): return self.strings['fur']
#
# class Duck(AnimalActions):
#     strings = dict(
#         quack = "Quaaaak!",
#         feathers = "The duck has gray and white feathers.",
#         bark = "The duck cannot bark.",
#         fur = "The duck has no fur"
#     )
#
# class Person(AnimalActions):
#     strings = dict(
#         quack = "The person imitates a duck.",
#         feathers = "The person takes a feather from the ground and shows it.",
#         bark = "The person says woof!",
#         fur = "The person puts on a fur coat."
#     )
#
# class Dog(AnimalActions):
#     strings = dict(
#         quack = "The dog cannot quack.",
#         feathers = "The dog has no feathers.",
#         bark = "Arf!",
#         fur = "The dog has white fur with black spots."
#     )
#
# def in_the_doghouse(dog):
#     print(dog.bark())
#     print(dog.fur())
#
# def in_the_forest(duck):
#     print(duck.quack())
#     print(duck.feathers())
#
# def main():
#     donald = Duck()
#     john = Person()
#     fido = Dog()
#
#     print("- In the forest: ")
#     for o in ( donald, john, fido):
#         in_the_forest(o)
#
#     print("- In the doghouse: ")
#     for o in ( donald, john, fido):
#         in_the_doghouse(o)
#
# if __name__ == "__main__": main()

###
### Another OOP way
###

# # -- VIEW --
#
# class AnimalActions:
#     def bark(self): return self._doAction('bark')
#     def fur(self): return self._doAction('fur')
#     def quack(self): return self._doAction('quack')
#     def feathers(self): return self._doAction('feathers')
#
#     def _doAction(self, action):
#         if action in self.strings:
#             return self.strings[action]
#         else:
#             return 'The {} has no {}'.format(self.animalName(), action)
#
#     def animalName(self):
#         return self.__class__.__name__.lower()
#
# # -- MODEL --
#
# class Duck(AnimalActions):
#     strings = dict(
#         quack = "Quaaaaak!",
#         feathers = "The duck has gray and white feathers."
#     )
#
# class Person(AnimalActions):
#     strings = dict(
#         bark = "The person says woof!",
#         fur = "The person puts on a fur coat.",
#         quack = "The person imitates a duck.",
#         feathers = "The person takes a feather from the ground and shows it."
#     )
#
# class Dog(AnimalActions):
#     strings = dict(
#         bark = "Arf!",
#         fur = "The dog has white fur with black spots.",
#     )
#
# # -- CONTROLLER --
#
# def in_the_doghouse(dog):
#     print(dog.bark())
#     print(dog.fur())
#
# def in_the_forest(duck):
#     print(duck.quack())
#     print(duck.feathers())
#
# def main():
#     donald = Duck()
#     john = Person()
#     fido = Dog()
#
#     print("-- In the forest:")
#     for o in ( donald, john, fido ):
#         in_the_forest(o)
#
#     print("-- In the doghouse:")
#     for o in ( donald, john, fido ):
#         in_the_doghouse(o)
#
# if __name__ == "__main__": main()

##
## Handling errors with exceptions
##

# fh = open('xlines.txt')
# for line in fh.readlines():
#     print(line)

# try:
#     fh = open('xlines.txt')
#     for line in fh.readlines():
#         print(line)
#
# except IOError as e:
#     print("Something bad happened ({}".format(e))
#
# print("after badness")

##
## 3. Setting up Python
##

# Done

##
## 4. General Syntax
##

##
## Creating a main script (helps let you call functions anytime
##

# def main():
#     print("This is the syntax.py file.")
#     egg()
#
# def egg():
#     print("egg")
#
# if __name__ == "__main__": main()

##
## Understanding whitespace in Python
##

# four spaces standard indent

## def main():
##     print("This is an example.")
##     print("another line, has to be at same indentation")

# Indenting is important if you have multiple commands, but if you have only one, than the function cna reside on one line
## def main(): print("This is the example.")

##
## Commenting Code
##

# comments use hash tag
# Don't comment too much, its purpose is to make the code clear

##
## Assigning Values
##

# def main():
#     # a = "one"
#     # a, b = 0, 1
#     # a, b = b, a
#     # a = True
#     a = [1, 2, 3, 4, 5]   # This is  tuple where you have list assigned to a variable. A tuple is a finite ordered list of elements
#     print(type(a), a)
#
# if __name__ == "__main__": main()

##
## Selecting code and values with conditionals
##

## Conditional Executions (traditional)
# def main():
#     a, b = 1, 1
#     if a < b:
#         print("a is less than b")
#     elif a > b:
#         print("a is greater than b")
#     else:
#         print("a is equal b")
#
# if __name__ == "__main__": main()

## Conditional Expressions
# def main():
#     a, b = 1, 1
#     s = "Less than" if a < b else "not less than"
#     print(s)
#
# if __name__ == "__main__": main()

##
## Creating and using functions
##

# def main():
#     func(1)
#     func(5)
#     func(7)
#
# def func(a):
#     for i in range(a, 10):
#         print(i, end=' ')
#     print() # prints an empty line
#
# if __name__ == "__main__": main()
#


##
## Creating and using objects
##

# class Egg:
#     def __init__(self, kind = "fried"):
#         self.kind = kind
#
#     def whatKind(self):
#         return self.kind
#
#
# def main():
#     fried = Egg()
#     scrambled = Egg('scrambled')
#     print(fried.whatKind())
#     # print(scrambled.whatKind())
#
#
# if __name__ == "__main__": main()

##
## 5. Variables, Objects, and Values.
##

##
## Understanding variables and objects in Python
##

# Everything in Python is an object. Every object has a ID, Type and a value
#
# X = 42 the 42 is the value
# x
# 42
# id(x)
# a unique number that is as an Identifer
# type(x)
# <class 'int'>

##
## Distingquishing mutable and immutable objects
##

# mutable objects can change
#
# immutable objects can not change (the distinction is found by the id(x) which provides a unique number )

##
## Using numbers
##

# def main():
#     num = 42 // 5 # this is integer division
#     print(num)
#     print(type(num), num)

# if __name__ == "__main__": main()


##
## Using strings (They are immutable objects)
##

# def main():
#     n = 42
#     # s = r'This is a\n string!' # The r before the string tells the system to display it "as is"
#     # s = "This is a {} string!".format(n) # Python 3 way of doing it
#     # s = "This is a %s string!" % n # This is the Python 2 way of doing the line above DONT USE, it will be deprecated
#     # s = ''' this is a string ''' # Allows to have a string that spans several lines like example below
#     s = '''\      # the \ escapes the extra line
#     This is a string
#     line after line
#     of text and more
#     text.
#     '''
#     print(s)
#
#
# if __name__ == "__main__": main()

##
## Aggregating values with lists and tuples
##

# def main():
#     # x = (1, 2, 3) # Tuple is an immutable object (cant be changed, must be fixed)
#     # x = [1, 2, 3]    # It is mutable object (can append or insert to list)
#     # x.append(5)
#     # x.insert(2, 7)
#     # x = 'string'
#     # print(type(x), x[2:4]) # slicing
#     x = 'String'
#     for i in x:
#         print(i)
#
#
#
# if __name__ == "__main__": main()


##
## Creating associative lists with dictionaries
##

# def main():
#     # d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
#     # for k in sorted(d.keys()):
#     #     print(k, d[k])
#     d = dict(
#         one = 1, two = 2, three = 3, four = 4, five = 'five'
#     )
#     d['seven'] = 7  # dict ionaries are mutable
#     for k in sorted(d.keys()):
#         print(k, d[k])
#
# if __name__ == "__main__": main()

##
## Finding the type and identity of a variable
##

# >>> x =  42
# >>> x
# 42
# >>> id(x)
# 1386935376
# >>> id(42)
# 1386935376
# >>> id(x)
# 1386935376
# >>> y = 42
# >>> x == y
# True
# >>> x is y
# True
# >>> x = dict(x = 42)
# >>> {'x':42}
# {'x': 42}
# >>> type(x)
# <class 'dict'>
# >>> id(x)
# 1596882536840
# >>> y = dict( x = 42)
# >>> id(y)
# 1596882465672
# >>> id(x)
# 1596882536840
# >>> y == x
# True
# >>> y is x
# False
# >>>

##
## Specifying logical values with True and False
##

# >>> a, b = 0, 1
# >>> a == b
# False
# >>> a < b
# True
# >>> a > b
# False
# >>> a = True
# >>> a
# True
# >>> type(a)
# <class 'bool'>
# >>> id(a)
# 1386679984
# >>> b = True
# >>> id(b)
# 1386679984
# >>> id(True)
# 1386679984
# >>>

##
## 6. Conditionals
##

##
## Selecting Code with if and else conditional statements
##

# def main():
#     a, b = 0, 1
#     if a < b:
#         print('This is true')
#     else:
#         print('This is not true')
#
#
# if __name__ == "__main__": main()

##
## Selecting multiple choice with elif
##

# def main():
#     v = 'seven'
#     if v == 'one':
#         print('v is one')
#     elif v == 'two':
#         print('v is two')
#     elif v == 'three':
#         print('v is three')
#     else:  # catch all command in event all of above are not true
#         print('v is someother thing')
#
#
# if __name__ == "__main__": main()

##
## Understanding other strategies for muliptle choice
##

# Python does not have "switch" or "case" that allows to select from multiple choice of variable
# Pythons way of doing it below

# def main():
#     choices = dict(
#         one = 'first',
#         two = 'second',
#         three = 'third',
#         four = 'fourth',
#         five = 'fifth'
#     )
#     v = 'seven'
#     print(choices.get(v, 'other'))
#
# if __name__ == "__main__": main()

##
## Using the conditional expression
##

# def main():
#     a, b = 1, 1
#     if a < b:
#         v = 'This is true'
#     else:
#         v = 'This is not true'
#     print(v)
#
# if __name__ == "__main__": main()

# Easier way

# def main():
#     a, b = 1, 1
#     v = 'this is true' if a < b else 'this is not true'
#     print(v)
#
# if __name__ == "__main__": main()

##
## 7. Loops
##

##
## Creating loops with while
##

# def main():
#     # simple fibonacci series
#     # the sum of two elements defines the next set
#     a, b = 0, 1
#     while b < 150:
#         print(b, end=' ')
#         a, b = b, a + b
#
# if __name__ == "__main__": main()

##
## Iterating with for
##

# #!/usr/bin/python3
# # for.py by Bill Weinman [http://bw.org]
# # This is an exercise file from Python 3 Essential Training lynda.com
# # Copyright 2010 The BearHeart Group, LLC
#
# def main():
#     for line in [1, 2, 3, 4, 5]:
#         print(line, end=' ')
#
# if __name__ == "__main__": main()

##
## Enumerating iterators
##

# def main():
#     fh = open('lines.txt')
#     for index, line in enumerate(fh.readlines())
#         print(index, line, end='')
#
# if __name__ == "__main__": main()

# def main():
#     s = 'this is a string'
#     for i, c in enumerate(s):
#         # print(i, c)
#         if c == 's': print('index {} is an s'.format(i))
#
# if __name__ == "__main__": main()

##
## Controlling Loop Flow with break, continue, and else
##

# def main():
#     s = 'this is a string'
#     for c in s:
#         # if c == 's': continue # skips all s characters
#         # if c == 's': break # terminates the loop
#         print(c, end='')
#     else:   # Will do all the loop actions, once done, it will do the else
#         print('else')
#
#
# if __name__ == "__main__": main()

# These controllers break, continue and else can be used in While loops

# def main():
#     s = 'this is a string'
#     i = 0
#     while(i < len(s)):
#         print(s[i], end='')
#         i += 1
#     else:
#         print('else')
#
# if __name__ == "__main__": main()

##
## 8. Operators
##

##
## Performing simple arithmetic
##

# >>> 5 + 5
# 10
# >>> 5 * 5
# 25
# >>> 5 - 3
# 2
# >>> 5 / 3
# 1.6666666666666667
# >>> 5 // 3
# 1
# >>> 5 % 3
# 2
# >>> divmod(5, 3)
# (1, 2)
# >>> num = 5
# >>> num += 1
# >>> num
# 6
# >>> num -= 1
# >>> num
# 5
# >>> num *= 5
# >>> num
# 25
# >>> num // = 5
# SyntaxError: invalid syntax
# >>> num //= 5
# >>> num
# 5
# >>> num *= 5
# >>> num /= 5
# >>> num
# 5.0
# >>>

##
## Operating on bitwise values
##

# >>> 5
# 5
# >>> 0b0101
# 5
# >>> def b(n): print('{:08b}'.format(n))
#
# >>> b(5)
# 00000101
# >>> b(10)
# 00001010
# >>> b(100)
# 01100100
# >>> x, y = 0x55, 0xaa
# >>> b(x)
# 01010101
# >>> b(y)
# 10101010
# >>> b(x | y)
# 11111111
# >>> b(x & y)
# 00000000
# >>> b(x ^ y)
# 11111111
# >>> b(x ^ 0)
# 01010101
# >>> b(x ^ 0xff)
# 10101010
# >>> b(x << 4)
# 10101010000
# >>> b(x >> 4)
# 00000101
# >>> b(~ x)
# -1010110
# >>>

##
## Comparing Values
##

# >>> 5 < 6
# True
# >>> 6 < 5
# False
# >>> 5 <= 6
# True
# >>> 5 <= 5
# True
# >>> 6 >= 5
# True
# >>> 6 >= 5
# True
# >>> 6 >= 6
# True
#
# >>> 6 >= 7
# False
#
# >>> 5 == 5
# True
# >>> 5 == 6
# False
# >>> 6 != 7
# True
# >>> 6 != 6
# False
# >>> x, y = 5, 6
# >>> id(x)
# 1353117616
# >>> id(y)
# 1353117648
# >>> x is y
# False
# >>> x is not y
# True
# >>> y = 5
# >>> id(y)
# 1353117616
# >>> x is y
# True
# >>> x, y = [5], [5]
# >>> id(x)
# 3185177271624
# >>> id(y)
# 3185177191112
# >>> x == y
# True
# >>>  x is y
#
# >>> x is y
# True
# >>>

##
## Operating on Boolean Values
##

# and or     Howver & symbol is used for bitwise equations

# >>> 5 == 5
# True
# >>> 7 < 5
# False
# >>> type(True)
# <class 'bool'>
# >>> True and False
# False
# >>> True and True
# True
# >>> True or False
# True
# >>> False or False
# False
# >>> True & True
# True
# >>> a, b = 0, 1
# >>> x, y = 'Zero', 'One'
# >>> x < y
# False
# >>> a < b
# True
# >>> if a < b and x < y: print('yes')
# else: print('no')
#
# no
# >>>

##
## Operating on parts of a container with the slice operator
##

# slices = parts of container

# >>> list = []
# >>> list = [1,2,3,4,5,6, 7,8,9,10]
# >>> list[0]
# 1
# >>> list[1]
# 2
# >>> list[9]
# 10
# >>> list[0:5]
# [1, 2, 3, 4, 5]
# >>> list[4]
# 5
# >>> list[0:5]
# [1, 2, 3, 4, 5]
# >>> range(0, 10)
# range(0, 10)
# >>> for i in range(0,10): print(i)
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# >>> list[0:10] #Code
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list[:] = range(100)
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# >>> list[27]
# 27
# >>> list[27]
# 27
# >>> list[27:42]
# [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
# >>> list[27:42:3]
# [27, 30, 33, 36, 39]
# >>> list[27:43:3] # Three arguemts start:end:step over
# [27, 30, 33, 36, 39, 42]
# >>> for i in list[27:43:3] : print(i)
#
# 27
# 30
# 33
# 36
# 39
# 42
# >>> list[27:43:3] = (99,99,99,99,99,99) # You can assign to a slice, notice the numbers replace by 99
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 99, 28, 29, 99, 31, 32, 99, 34, 35, 99, 37, 38, 99, 40, 41, 99, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# >>>

##
## Understanding operators precedence
##

# >>> 5 * 25 + 14 / 2 # Precedence 1. * 2. / 3. + 4. -
# 132.0
# >>> 5 * (25 + 14) / 2 # Parenthesis used to explicit state your intentions
# 97.5
# >>> # If code is written poorly where the intent is not clear, than refer to the Python Operator Precedence chart to help understand the order
# >>> # Be kind and use paranthesis to clearly state the intent of your code
# >>>

##
## 9. Regular Expressions
##

##
## Using the re module
##

# - Regular expressions are a very powerful method of matching patterns in text
# - Actually a small language in itself, regexes can be very simple or very complex
# - Implemented in Python with the "re" module

# import re
#
# pattern = re.compile(r'\d\d\d')
#     if re.search(regex, line): print(line)


##
## Searching with regular expressions
##

## Used to show all lines that contain Lenore and Nevermore
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         if re.search('(Len|Neverm)ore', line):
#             print(line, end='')
#
# if __name__ == "__main__": main()

# Example below for finding matches - good for finding patterns and replacing
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         match = re.search('(Len|Neverm)ore', line)
#         if match:
#             print(match.group())
#
# if __name__ == "__main__": main()

##
## Searching with regular expressions
##

# Find and replace
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         print(re.sub('(Len|Neverm)ore', '###', line), end='')
#
# if __name__ == "__main__": main()

# Search and replace modules
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         match = re.search('(Len|Neverm)ore', line)
#         if match:
#             print(line.replace(match.group(),'happy'), end='')
#
# if __name__ == "__main__": main()

##
## Reusing regular expressions with re compile
##

# A way to improve efficiency by putting search string in "pattern"
# adding re.IGNORECASE will ignore case
# import re
#
# def main():
#     fh = open('raven.txt')
#     pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
#     for line in fh:
#         if re.search(pattern, line):
#             print(pattern.sub('super happy', line), end='')
#
# if __name__ == "__main__": main()

##
## 10. Exceptions
##

##
## Learning how exceptions work
##

# -Exceptions are the key method of handling errors in Python
# -"try" something, then catch an exception with "except"

# try:
#     fh = open('filename')
# except IOError as e:
#     print(e)
# else:
#     for | in fh:print(|)

# You may raise your own exceptions with "raise"

##
## Handling exceptions
##

# def main():
#     fh = open('lines.txt')
#     for line in fh: print(line.strip())
#
# if __name__ == "__main__": main()

# Exmpale of try and catch
# def main():
#     try:
#         fh = open('lines.txt')
#     except:
#         print('could not open the file. come back in 2000 years')
#     else:
#         for line in fh: print(line.strip())
#
# if __name__ == "__main__": main()

##
## Raising exceptions
##

# def main():
#     try:
#         for line in readfile('lines.doc'): print(line.strip())
#     except IOError as e:
#         print('cannot read file:', e)
#     except ValueError as e:
#         print('bad filename', e)
#
# def readfile(filename):
#     if filename.endswith('.txt'):
#         fh = open(filename)
#         return fh.readlines()
#     else: raise ValueError('Filename must end with .txt')
#
# if __name__ == "__main__": main()

##
## 11. Functions
##

##
## Defining functions
##





###
### Template
###

# def main():
#     print("This is the template")
#
#
# if __name__ == "__main__": main()