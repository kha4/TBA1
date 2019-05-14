#include statements
import sys


#returns the alias for the verb entered by the player
def findAlias(x):
    actionsGrid = [['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock'], ['pull', 'drag', 'haul', 'yank'], ['eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble'],
    ['scratch', 'claw', 'cut', 'scrape'], ['drop', 'dump', 'lower', 'release'], ['break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear'], ['throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel'],
    ['push', 'press', 'shove'], ['drink', 'sip', 'gulp', 'slurp', 'suck'], ['open', 'expand', 'free'], ['take', 'grab']]

    for idx, row in enumerate(actionsGrid):
        for item in row:
            if x == item:
                return actionsGrid[idx][0]

#retuns if the entered verb is one of the special help verbs
def helpVerbs(words):
    specialFlag = 0
    nouns = ['bed', 'desk', 'table', 'chair', 'staircase', 'lamp', 'ect']
    #pull in the valid room exits
    roomExits = ['north', 'south', 'west', 'east']
    #pull in the valid ones, hard coded for now
    adjRooms = ['cella', 'cellb']
    for idx, x in enumerate(words):
        #looking for a spcial verb
        specialVerbs = ['look', 'go', 'help', 'inventory', 'north', 'south', 'west', 'east']
        for y in specialVerbs:
            if x == y:
                print "FOUND SPECIAL VERB:", y
                #checking if there is a valid noun to look at or just using look
                if x == "look":
                    try:
                        words[idx+1]
                        if words[idx+1] == "at":
                            for i in nouns:
                                #change to try, can't do if
                                try:
                                    words[idx+2]
                                    if words[idx+2] == i:
                                        #we understand what the player wants to look at, and is a valid item
                                        specialFlag = 1
                                        print "look at noun:", i
                                        return "lookat", i
                                except:
                                    print "You need to include an item to look at.\n"
                                    return 0
                            if specialFlag == 0:
                                print "That is not a valid item to look at. You can look at items in the current room or in your inventory. Type \"inventory\" to view your inventory.\n"
                                return 0
                        else:
                            print "To get the explanation of a room, only type \'look\'.\nIf you want to look AT something, type \'look at\' followed by an item."
                            return 0
                            #put here stuff for "look under the bed" maybe?
                    except:
                        #good, we understand, they want to use "look"
                        return x
                if x == "go":
                    try:
                        words[idx+1]
                        for i in roomExits:
                            if words[idx+1] == i:
                                return i
                        for i in adjRooms:
                            if words[idx+1] == i:
                                return i
                        print "That is not a valid direction you can go in.\n"
                        return 0
                    except:
                        print "Which way would you like to go? Refer to the room description to find the exits.\n"
                        return 0
                if x == "north" or "south" or "east" or "west":
                    try:
                        words[idx+1]
                        print "To go a direction try: \"go north\" or just \"north\"."
                        return 0
                    except:
                        return x
        for i in adjRooms:
            if x == i:
                print "FOUND DIRECTION:", i
                return i

    return 1



def userInput():
    understandFlag = 0
    while(understandFlag != 1):
    #take in text
        userInput = raw_input("What would you like to do next?\n")
        sys.stdout.flush()
    #split text by " "(space)
        lowerInput = userInput.lower()
        words = lowerInput.split()
        #taking out "the" or "a", we don't need it
        for i in range(len(words) - 1, -1, -1):
            if words[i] == "the" or words[i] == "a":
                del words[i]
    #analyze each word
        specVerb = helpVerbs(words)
        if specVerb != 0 and specVerb != 1: 
            if specVerb == "look":
                specialNoun = "N/A"
                return specVerb, specialNoun
            elif specVerb[0] == "lookat":
                return specVerb[0], specVerb[1]  
            elif specVerb == "north" or "south" or "east" or "west":
                return specVerb, "N/A" 
            else:
                return specVerb, "N/A"

        if specVerb != 0:
            for idx, x in enumerate(words):
                #look for key words
                    keywords = ['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock', 'pull', 'drag', 'haul', 'yank', 'eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble', 
                    'scratch', 'claw', 'cut', 'scrape', 'drop', 'dump', 'lower', 'release', 'break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear', 'throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel',
                    'push', 'press', 'shove', 'drink', 'sip', 'gulp', 'slurp', 'suck', 'open', 'expand', 'free', 'take', 'grab']
                    for y in keywords:
                        if x == y:
                            print "FOUND VERB:", x
                            alias = findAlias(x)
                            print "FOUND ALIAS:", alias
                            #look for nouns following key words
                            nouns = ['bed', 'desk', 'table', 'chair', 'staircase', 'lamp', 'ect']
                            understandFlag = 2 
                            for i in nouns:
                                try:
                                    if words[idx+1] == i:
                                        print "FOUND NOUN:", i
                                        userNoun = i
                                        #confirm understand, we have action and noun that we know so we can exit
                                        understandFlag = 1
                                except:
                                    print "You did not provide an item that is available for your action. Please enter the phrase again with an item.\n"
                                    understandFlag = 3
                                    break
                            #if we understand the verb but not the noun
                            if understandFlag == 2:
                                print "1You did not provide an item that is available for your action. Please enter the phrase again with an item.\n"
            #if we don't understand the verb
            if understandFlag == 0:
                print "I'm sorry, I don't understand. Please enter a different phrase.\n"

    return alias, userNoun


if __name__ == '__main__':
    SV = "startingValue"
    actionNoun = userInput()
    finalActions = ['hit', 'pull', 'eat', 'scratch', 'drop', 'break', 'throw', 'push', 'drink', 'open', 'take', 'look', 'lookat', 'north', 'south', 'east', 'west']
    finalRooms = ['cella', 'cellb']
    for idx, x in enumerate(finalActions):
        if actionNoun[0] == x:
            #set flag
            flag = idx 
            print "\nFlag:", flag
            print "User Noun:", actionNoun[1]
    counter = 20
    for idx, x in enumerate(finalRooms):
        if actionNoun[0] == x:
            #set flag
            flag = counter 
            print "\nFlag:", flag
            print "User Noun:", actionNoun[1]
        counter = counter + 1
            
            #this is how it would go back to the main program, with the correct flag and item
            # return flag, actionNoun[1]

#NOTES:

#in order for me to verify if the item is able to be used, I will need to pull in the list of items in each room from the room files
#need to wait for those to be created, can do a practice one
#how are we pulling this together? If I have this program, will the other programs call it or are we putting it all in one program?
    #put it all in one main and each program is a "function" that we call when needed?
#mid point check-in
#update on the features we want to use? How do we want to use them?

#create a create verb or build verb - if they don't have all the required items then throw a "You don't have all the items you need to build"
#how to read in all the items in the room from the txt files

#ADD TOLOWER FUNCTION


def printRoomDescription(self):
    for item in self.roomList:
        rmName = str(item['Name'])
        if (item['Name'] == self.currentRoom):
            if (item['Status'] == 'visited'):
                print ("Location: ", item['Name'])
                print (item['ShortDesc'])
            else:
                print ("Location: ", item['Name'])
                print (item['LongDesc'])
                self.setRoomStatus(self.currentRoom)
        break
