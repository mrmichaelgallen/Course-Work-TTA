Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
{'Guido von Rassum': 'gvr@gmail.com', 'Sergey Brin': 'sb@gmail.com', 'Tim Berners-Lee': 'tbl@gmail.com', 'Linus Torvalds': 'lt@gmail.com', 'Larry Page': 'lp@gmail.com'}
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
{'Guido von Rassum': ['gvr@gmail.com', 222], 'Sergey Brin': ['sb@gmail.com', 555], 'Tim Berners-Lee': ['tbl@gmail.com', 111], 'Linus Torvalds': ['lt@gmail.com', 333], 'Larry Page': ['lp@gmail.com', 444]}
>>> print epic_programmer_dict['Tim Berners-Lee']
['tbl@gmail.com', 111]
>>> print epic_programmer_dict['Tim Berners-Lee'][1]
111
>>> programmer = epic_programmer_dict['Tim Berners-Lee']
>>> print programmer[1]
111
>>> personsName = raw_input('Please enter a name: ')
Please enter a name: Michael
>>> personsName = raw_input('Please enter a name: ')
Please enter a name: 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Michael
Michael
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Michael
Michael

Traceback (most recent call last):
  File "C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py", line 16, in <module>
    personsInfo = epic_programmer_dict[personsName]
KeyError: 'Michael'
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Michael
Michael
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Michael
Michael
No information found for that name
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Linus
Linus
No information found for that name
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Tim Berners-Lee
Tim Berners-Lee
['tbl@gmail.com', 111]
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LinUS Torvalds
LinUS Torvalds
No information found for that name
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LinuS TOrvald
linus torvald
No information found for that name
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LiNUS TorvalDS
linus torvalds
['lt@gmail.com', 333]
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LinuS Torvalds
linus torvalds
Name: linus torvalds
Email: lt@gmail.com
No information found for that name
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LiNUS ToRVALDS
linus torvalds
Name: Linus torvalds
Email: lt@gmail.com
No information found for that name
>>> print "number: ' + personsInfo[1]
SyntaxError: EOL while scanning string literal
>>> print 'Number: ' + personsInfo[1]

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print 'Number: ' + personsInfo[1]
TypeError: cannot concatenate 'str' and 'int' objects
>>> print 'Number: ' + str(personsInfo[1])
Number: 333
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: SERgey BRin
sergey brin
Name: Sergey Brin
Email: sb@gmail.com
Number: 555
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: LiNUS Torvalds
Name: Linus Torvalds
Email: lt@gmail.com
Number: 333
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Linus TorValds
Name: Linus Torvalds
Email: lt@gmail.com
Number: 333
Search again? (y/n)y

Traceback (most recent call last):
  File "C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py", line 39, in <module>
    if searchAgain == 'y':
NameError: name 'searchAgain' is not defined
>>> 
===== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py =====
Please enter a name: Linus Torvalds
Name: Linus Torvalds
Email: lt@gmail.com
Number: 333
Search again? (y/n)n

Traceback (most recent call last):
  File "C:/Users/Michael/Desktop/New Game/Python_Item35_Script.py", line 39, in <module>
    if searchAgain == 'y':
NameError: name 'searchAgain' is not defined
>>> 
