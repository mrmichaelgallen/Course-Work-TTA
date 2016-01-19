Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dictionary_name = {'item_1':1,'item_2':2, 'item_3':3 }
>>> print dictionary_name['item_1']
1
>>> 
== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py ==
>>> print epic_programmer_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Tim Berners-Lee': 'tbl@gmail.com', 'Linus Torvalds': 'lt@gmail.com'}
>>> print epic_programmer_dict['Tim Berners-Lee']
tbl@gmail.com
>>> 
== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py ==

Traceback (most recent call last):
  File "C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py", line 6, in <module>
    epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'
NameError: name 'epic_programmer_dict' is not defined
>>> 
== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py ==
New email for Tim: tim@gmail.com
>>> 
== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py ==
New email for Tim: tim@gmail.com
>>> print epic_programmer_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Tim Berners-Lee': 'tim@gmail.com', 'Linus Torvalds': 'lt@gmail.com', 'Larry Page': 'lp@gmail.com'}
>>> 
== RESTART: C:/Users/Michael/Desktop/New Game/Python_Item29_ShellOutput.py ==
New email for Tim: tim@gmail.com
>>> epic_programmer_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Larry Page': 'lp@gmail.com', 'Sergey Brin': 'sb@gmail.com', 'Tim Berners-Lee': 'tim@gmail.com', 'Linus Torvalds': 'lt@gmail.com', 'Michael Allen': 'ma@gmail.com'}
>>> del epic_programmer_dict['Sergey Brin']
>>> epic_programmer_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Larry Page': 'lp@gmail.com', 'Tim Berners-Lee': 'tim@gmail.com', 'Linus Torvalds': 'lt@gmail.com', 'Michael Allen': 'ma@gmail.com'}
>>> del epic_programmer_dict['Michael Allen']
>>> epic_programmer_dict
{'Guido van Rossum': 'gvr@gmail.com', 'Larry Page': 'lp@gmail.com', 'Tim Berners-Lee': 'tim@gmail.com', 'Linus Torvalds': 'lt@gmail.com'}
>>> 
