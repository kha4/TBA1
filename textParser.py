################################################################################
## TBA1 - Melissa Barr/ Kevin Ha / Christopher Perry                          ##
## CS 467 - Capstone - June 4, 2019                                           ##
## This file contains the text parser, takes in and validates user input      ##
################################################################################

import sys
import gameEngine
import gameState

#returns the alias for the verb entered by the player
def findAlias(x):
    #all valid action verbs
    actionsGrid = [['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock'], ['pull', 'drag', 'haul', 'yank'], ['eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble'],
    ['scratch', 'claw', 'cut', 'scrape'], ['drop', 'dump', 'lower', 'release'], ['break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear'], ['throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel'],
    ['push', 'press', 'shove'], ['drink', 'sip', 'gulp', 'slurp', 'suck'], ['open', 'expand', 'free'], ['take', 'grab']]

    #if a verb is found, set it equal to the first verb in the sublist which is the alias for it
    for idx, row in enumerate(actionsGrid):
        for item in row:
            if x == item:
                return actionsGrid[idx][0]

#retuns if the entered verb is one of the special help verbs
def helpVerbs(words, newGame, gameNouns, adjRooms, dirRooms):
    specialFlag = 0

    #loops through all verbs
    for idx, x in enumerate(words):
        #looking for a spcial verb
        specialVerbs = ['look', 'go', 'help', 'inventory', 'north', 'south', 'west', 'east', 'savegame', 'loadgame', 'quit', 'exit']
        for y in specialVerbs:
            if x == y:
                #checking if there is a valid item to look at or just using look
                if x == "look":
                    try:
                        words[idx+1]
                        #if using look at then checking that the item is valid to look at
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
                #if using go then checking that the destination is valid
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
                
                #if exit, alias is quit
                if x == "exit":
                    return "quit"

                #if the user just enters a direction they want to go to, checks that it's just the direction
                for l in dirRooms:
                    if words[idx] == l:
                        try:
                            words[idx+1]
                            print ("To go a direction try: \"go north\" or just \"north\".")
                            return 0
                        except:
                            return l

                #if the user enters south, north, east, or west and it was not returned earlier, it is invalid
                if x == "south" or x == "north" or x == "east" or x == "west":
                    print (x,"is not a valid direction you can go in.")
                    print ("The available exits are:", adjRooms, "or the directions", dirRooms, ".\n")
                    return 0                    

                #if the user enters any of the other special verbs, error checks that it's just the verb
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
        
        #if the user just enters a name of the room they want to go to, checks if it is valid
        catRooms = ['cell', 'prison', 'mess', 'kitchen', 'library', 'sally', 'armory', 'visiting', 'yard', 'recreation', 'guardhouse', 'dock', 'boat', 'warden']
        for i in catRooms:
            if x == i:
                newWords = ' '.join(map(str, words))
                for p in adjRooms:
                    if newWords == p:
                        return p

                print (newWords,"is not a valid direction you can go in.")
                print ("The available exits are:", adjRooms, "or the directions", dirRooms, ".\n")
                return 0
                            
    return 1



#function that loops through the user input and checks for keywords
def userInput(newGame, gameNouns, adjRooms, dirRooms, invNouns):
    #understand flag set in the begainning so that if the flag changes, we know they do not understand
    understandFlag = 0
    while(understandFlag != 1):
    #take in text
        userInput = input("\nWhat would you like to do next?\n")
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
        #taking out "the", "to", or "a", we don't need it
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

        #loop through all verbs to find keyword
        if specVerb != 0:
            for idx, x in enumerate(words):
                #look for key words
                    keywords = ['hit', 'punch', 'swing', 'collide', 'bat', 'strike', 'bump', 'slap', 'smack', 'knock', 'pull', 'drag', 'haul', 'yank', 'eat', 'consume', 'swallow', 'chew', 'devour', 'feed', 'ingest', 'nibble', 
                    'scratch', 'claw', 'cut', 'scrape', 'drop', 'dump', 'lower', 'release', 'break', 'destroy', 'shatter', 'smash', 'crush', 'split', 'tear', 'throw', 'fling', 'heave', 'hurl', 'pitch', 'thrust', 'propel',
                    'push', 'press', 'shove', 'drink', 'sip', 'gulp', 'slurp', 'suck', 'open', 'expand', 'free', 'take', 'grab']
                    for y in keywords:
                        if x == y:
                            #function to find alias
                            alias = findAlias(x)
                            understandFlag = 2 
                            #if user enters drop we know it's in their inventory, check inventory
                            if alias == "drop":
                                understandFlag = 4
                                #if verb is found in the inventory, return it with the noun
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
                            #loop through items to check if they are valid
                            for i in gameNouns:
                                try:
                                    if words[idx+1] == i:
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
                                del words[idx]
                                newWords = ' '.join(map(str, words))
                                for i in gameNouns:
                                    if newWords == i:
                                            userNoun = i
                                            return alias, userNoun
                                print ("You did not provide an item that is available for your action. Please enter the phrase again with an item.\n")
            #if we don't understand the verb
            if understandFlag == 0:
                print ("I'm sorry, I don't understand. Please enter a different phrase.\n")

    return alias, userNoun


#function to pull in the inventory, passages, and items, returns final verb and noun
def parse(newGame):
    SV = "startingValue"
    #pulls in the game items
    gameNouns = []
    for item in newGame.objectList:
        if (item['Location'] == newGame.currentRoom):
            gameNouns.append(item['Name'].lower())

    #pulls in the inventory
    invNouns = []
    for item in newGame.playerInventory:
        invNouns.append(item.lower())

    #pulls in the adjacent rooms
    adjRooms = []
    for item in newGame.passageList:
        if (item['Location'] == newGame.currentRoom):
            adjRooms.append(item['Description'].lower())

    #pulls in the directions
    dirRooms = []
    for item in newGame.passageList:
        if (item['Location'] == newGame.currentRoom):
            dirRooms.append(item['Direction'].lower())

    #calls main parsing function
    actionNoun = userInput(newGame, gameNouns, adjRooms, dirRooms, invNouns)
    finalActions = ['hit', 'pull', 'eat', 'scratch', 'drop', 'break', 'throw', 'push', 'drink', 'open', 'take', 'look', 'lookat', 'savegame', 'loadgame', 'help', 'inventory', 'quit']
    #if final action is found
    for x in finalActions:
        if actionNoun[0] == x:
            return actionNoun[0], actionNoun[1]
    #if adjacent room is found
    for x in adjRooms:
        if x == actionNoun[0]:
            str2 = ''.join(actionNoun[0])
            return "go", str2
    #if direction is found
    for x in dirRooms:
        if x == actionNoun[0]:
            str1 = ''.join(actionNoun[0])
            return "go", str1

