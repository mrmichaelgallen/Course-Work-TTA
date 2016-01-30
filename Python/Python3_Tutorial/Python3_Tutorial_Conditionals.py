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


