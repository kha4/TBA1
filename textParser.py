#include statements
import sys


#returns the alias for the verb entered by the player
def findAlias(x):
    actionsGrid = [['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock'], ['pull', 'drag', 'haul', 'yank'], ['eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble'],
    ['sratch', 'claw', 'cut', 'scrape'], ['drop', 'dump', 'lower', 'release'], ['break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear'], ['throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel'],
    ['push', 'press', 'shove'], ['drink', 'sip', 'gulp', 'slurp', 'suck'], ['open', 'expand', 'free']]

    for idx, row in enumerate(actionsGrid):
        for item in row:
            if x == item:
                return actionsGrid[idx][0]

def userInput():
    understandFlag = 0
    while(understandFlag != 1):
    #take in text
        userInput = raw_input("What would you like to do next?\n")
        sys.stdout.flush()
    #split text by " "(space)
        words = userInput.split()
        #taking out "the" or "a", we don't need it
        for i in range(len(words) - 1, -1, -1):
            if words[i] == "the" or words[i] == "a":
                del words[i]
        # print "Final string: ", words
    #analyze each word
        for idx, x in enumerate(words):
            #look for key words
                keywords = ['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock', 'pull', 'drag', 'haul', 'yank', 'eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble', 
                'sratch', 'claw', 'cut', 'scrape', 'drop', 'dump', 'lower', 'release', 'break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear', 'throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel',
                'push', 'press', 'shove', 'drink', 'sip', 'gulp', 'slurp', 'suck', 'open', 'expand', 'free']
                for y in keywords:
                    if x == y:
                        print "FOUND VERB:", x
                        alias = findAlias(x)
                        print "FOUND ALIAS:", alias
                        #look for nouns following key words
                        nouns = ['bed', 'desk', 'table', 'chair', 'staircase', 'lamp', 'ect']
                        understandFlag = 2 
                        for i in nouns:
                            if words[idx+1] == i:
                                print "FOUND NOUN:", i
                                userNoun = i
                                #confirm understand, we have action and noun that we know so we can exit
                                understandFlag = 1
                        #if we understand the verb but not the noun
                        if understandFlag == 2:
                            print "You did not provide an item for your action. Please enter the phrase again with an item.\n"
        #if we don't understand the verb
        if understandFlag == 0:
            print "I'm sorry, I don't understand. Please enter a different phrase.\n"

    return alias, userNoun


if __name__ == '__main__':
    actionNoun = userInput()
    finalActions = ['hit', 'pull', 'eat', 'scratch', 'drop', 'break', 'throw', 'push', 'drink', 'open']
    for idx, x in enumerate(finalActions):
        if actionNoun[0] == x:
            #set flag
            flag = idx 
            print "\nFlag:", flag


