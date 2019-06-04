#include statements
import sys
import gameEngine
import gameState

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
def helpVerbs(words, newGame, gameNouns, adjRooms, dirRooms):
    specialFlag = 0

    for idx, x in enumerate(words):
        #looking for a spcial verb
        specialVerbs = ['look', 'go', 'help', 'inventory', 'north', 'south', 'west', 'east', 'savegame', 'loadgame', 'quit']
        for y in specialVerbs:
            if x == y:
                #checking if there is a valid noun to look at or just using look
                if x == "look":
                    try:
                        words[idx+1]
                        if words[idx+1] == "at":                 
                            del words[idx]
                            del words[idx]
                            if words:
                                newWords = ' '.join(map(str, words))
                            else:
                                print ("You need to include an item to look at.\n")
                                return 0                            
                            for i in gameNouns:
                                if newWords == i:
                                    #we understand what the player wants to look at, and is a valid item
                                    specialFlag = 1
                                    return "lookat", i
                                   
                            if specialFlag == 0:
                                print ("That is not a valid item to look at. You can look at items in the current room or in your inventory. Type \"inventory\" to view your inventory.\n")
                                return 0
                        else:
                            print ("To get the explanation of a room, only type \'look\'.\nIf you want to look AT something, type \'look at\' followed by an item.")
                            return 0
                    except:
                        #good, we understand, they want to use "look"
                        return x
                if x == "go":
                    try:
                        words[idx+1]
                        for i in dirRooms:
                            if words[idx+1] == i:
                                return i
                        for i in range(len(words) - 1, -1, -1):
                            if words[i] == "go":
                                del words[i]
                        newWords = ' '.join(map(str, words))
                        for i in adjRooms:
                            if newWords == i:
                                return i
                        print (newWords,"is not a valid direction you can go in.")
                        print ("The available exits are:", adjRooms, "or the directions", dirRooms, ".\n")
                        return 0
                    except:
                        print ("Which way would you like to go? Refer to the room description to find the exits.\n")
                        return 0

                for l in dirRooms:
                    if words[idx] == l:
                        try:
                            words[idx+1]
                            print ("To go a direction try: \"go north\" or just \"north\".")
                            return 0
                        except:
                            return l

                print ("X is", x)
                if x == "south" or x == "north" or x == "east" or x == "west":
                    print (x,"is not a valid direction you can go in.")
                    print ("The available exits are:", adjRooms, "or the directions", dirRooms, ".\n")
                    return 0                    

                if x == "help" or x == "inventory" or x == "savegame" or x == "loadgame" or x == "quit":
                    try:
                        words[idx+1]
                        print ("To use the command", x, "just type:", x, "\n")
                        return 0
                    except:
                        pass
                    try:
                        words[idx-2]
                        print ("To use the command", x, "just type:", x, "\n")
                        return 0
                    except:
                        return x
        
        catRooms = ['cell', 'prison', 'mess', 'kitchen', 'library', 'sally', 'armory', 'visiting', 'yard', 'recreation', 'guardhouse', 'dock', 'boat', 'warden']
        for i in catRooms:
            if x == i:
                newWords = ' '.join(map(str, words))
                for p in adjRooms:
                    if newWords == p:
                        return p
                    else:
                        print (newWords,"is not a valid direction you can go in.")
                        print ("The available exits are:", adjRooms, "or the directions", dirRooms, ".\n")
                        return 0
                            
    return 1



def userInput(newGame, gameNouns, adjRooms, dirRooms, invNouns):
    understandFlag = 0
    while(understandFlag != 1):
    #take in text
        userInput = input("What would you like to do next?\n")
        sys.stdout.flush()
    #split text by " "(space)
        lowerInput = userInput.lower()
        words = lowerInput.split()
        #replacing any prepositions with at
        prepositions = ['on', 'above', 'about', 'onto', 'into', 'below', 'in', 'around', 'behind', 'beside', 'by', 'down', 'inside', 'through', 'under']
        for i in range(len(words) - 1, -1, -1):
            for p in prepositions:
                if words[i] == p:
                    words[i] = "at"
        #taking out "the" or "a", we don't need it
        for idx, i in enumerate(words):
            if words[idx] == "the" or words[idx] == "to":
                del words[idx]
            if words[idx] == "a":
                try:
                    words[idx-1]
                    if words[idx-1] == "block":
                        pass
                    else:
                        del words[idx]
                except:
                    del words[idx]

    #analyze each word
        specVerb = helpVerbs(words, newGame, gameNouns, adjRooms, dirRooms)
        if specVerb != 0 and specVerb != 1: 
            if specVerb == "look":
                specialNoun = "N/A"
                return specVerb, specialNoun
            elif specVerb[0] == "lookat":
                return specVerb[0], specVerb[1]
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
                            alias = findAlias(x)
                            understandFlag = 2 
                            if alias == "drop":
                                understandFlag = 4
                                for p in invNouns:
                                    try:
                                        if words[idx+1] == p:
                                            userNoun = p
                                            understandFlag = 1
                                            return alias, userNoun
                                    except:
                                        print ("You have not given an item to drop. You can drop items in your inventory.")
                                        print ("Inventory:", invNouns, "\n")
                                        understandFlag = 3
                                
                                if understandFlag == 4:
                                    print ("You can not drop that item because it is not in your inventory.")
                                    print ("Inventory:", invNouns, "\n")
                                    break
                            for i in gameNouns:
                                try:
                                    if words[idx+1] == i:
                                        # print ("FOUND NOUN:", i)
                                        userNoun = i
                                        #confirm understand, we have action and noun that we know so we can exit
                                        understandFlag = 1
                                except:
                                    if understandFlag != 3:
                                        print ("You did not provide an item that is available for your action. Please enter the phrase again with an item.\n")
                                        understandFlag = 3
                                        break
                            #if we understand the verb but not the noun
                            if understandFlag == 2:
                                print ("You did not provide an item that is available for your action. Please enter the phrase again with an item.\n")
            #if we don't understand the verb
            if understandFlag == 0:
                print ("I'm sorry, I don't understand. Please enter a different phrase.\n")

    return alias, userNoun


def parse(newGame):
    SV = "startingValue"
    gameNouns = []
    for item in newGame.objectList:
        if (item['Location'] == newGame.currentRoom):
            gameNouns.append(item['Name'].lower())

    print ("nouns pulled in are: ", gameNouns)

    invNouns = []
    for item in newGame.playerInventory:
        invNouns.append(item.lower())

    print ("Inventory pulled in is: ", invNouns)

    adjRooms = []
    for item in newGame.passageList:
        if (item['Location'] == newGame.currentRoom):
            adjRooms.append(item['Description'].lower())

    print ("Exits pulled in are: ", adjRooms)

    dirRooms = []
    for item in newGame.passageList:
        if (item['Location'] == newGame.currentRoom):
            dirRooms.append(item['Direction'].lower())

    print ("Directions pulled in are: ", dirRooms)

    actionNoun = userInput(newGame, gameNouns, adjRooms, dirRooms, invNouns)
    finalActions = ['hit', 'pull', 'eat', 'scratch', 'drop', 'break', 'throw', 'push', 'drink', 'open', 'take', 'look', 'lookat', 'savegame', 'loadgame', 'help', 'inventory', 'quit']
    for x in finalActions:
        if actionNoun[0] == x:
            print ("\nVerb:", actionNoun[0])
            print ("User Noun:", actionNoun[1])
            return actionNoun[0], actionNoun[1]
    for x in adjRooms:
        if x == actionNoun[0]:
            str2 = ''.join(actionNoun[0])
            print ("\nVerb:", "go")
            print ("User Noun:", str2)
            return "go", str2
    for x in dirRooms:
        if x == actionNoun[0]:
            str1 = ''.join(actionNoun[0])
            print ("\nVerb:", "go")
            print ("User Noun:", str1)
            return "go", str1


# def printRoomDescription(self):
#     for item in self.roomList:
#         rmName = str(item['Name'])
#         if (item['Name'] == self.currentRoom):
#             if (item['Status'] == 'visited'):
#                 print ("Location: ", item['Name'])
#                 print (item['ShortDesc'])
#             else:
#                 print ("Location: ", item['Name'])
#                 print (item['LongDesc'])
#                 self.setRoomStatus(self.currentRoom)
#         break