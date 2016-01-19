# Our epic programmer dict from before
epic_programmer_dict = {'tim berners-Lee' : ['tbl@gmail.com', 111],
                        'guido von rassum' : ['gvr@gmail.com', 222],
                        'linus torvalds' : ['lt@gmail.com', 333],
                        'larry page' : ['lp@gmail.com', 444],
                        'sergey brin' : ['sb@gmail.com',555],
                        }
##
##print epic_programmer_dict

def searchPeople(personsName):
    # Looks up the name in the epic dictionary
    try:
        # Tries the following lines of texts, and if
        # There are no errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])

    except:
        # If there are errors, then this code gets run
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    # Asks user to input persons name
    personsName = raw_input('Please enter a name: ').lower()

    # Run our new function searchPeople with what was typed in
    searchPeople(personsName)
    userWantsMore = False

    # See if user wants to search again
    searchAgain = raw_input('Search again? (y/n)')

    # Look at whey they reply and act accordingly
    if searchAgain == 'y':
        #userWantsMore stays as true so loop repeats
        userWantsMore = True

    elif searchAgain == 'n':
            # userWantsMore turns to false to stop loop
            userWantsMore = False

    else:
        # User inputs an invalid response, so we quit anyway
        print "I don't understand what you mean, quitting"
        userWantsMore = False
