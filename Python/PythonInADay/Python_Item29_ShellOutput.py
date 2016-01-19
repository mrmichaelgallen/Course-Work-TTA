epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds' : 'lt@gmail.com', }

# Adds a different email address
epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'
print 'New email for Tim: ' + epic_programmer_dict['Tim Berners-Lee']

# Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'

# Add Sergey Brin
epic_programmer_dict['Sergey Brin'] = 'sb@gmail.com'

# Add myself
epic_programmer_dict['Michael Allen'] = 'ma@gmail.com'

# Delete Sergey Brin from the dictionary
del epic_programmer_dict['Sergey Brin']

# Delete someone else from the dictionary
del epic_programmer_dict['Michael Allen']
