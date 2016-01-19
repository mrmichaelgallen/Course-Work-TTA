Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "This stuff rocks!"
This stuff rocks!
>>> print This stuff rocks!
SyntaxError: invalid syntax
>>> x = 10
>>> print x
10
>>> y = 2
>>> print (x+y)
12
>>> pring (x-y)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pring (x-y)
NameError: name 'pring' is not defined
>>> print (x-y)
8
>>> print (x*y)
20
>>> print (x/y)
5
>>> print X

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print X
NameError: name 'X' is not defined
>>> 
