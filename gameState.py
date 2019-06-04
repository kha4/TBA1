import roomParser
from roomParser import parseNewRoomData
import os

class gameState:
    """This class maintains current state of the game"""

    def __init__(self):
        self.player = ""
        self.currentRoom = "Prison Cell"
        self.playerInventory = []
        self.roomList = []
        self.objectList = []
        self.roomStatus = []
        self.passageList = []


    #hit', 'pull', 'eat', 'scratch', 'break', 'push', 'drink',
    def modifyState(self, verb, noun):
        if (verb == 'take'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun and item['Movable'] == 'y'):
                    print (item['Name'], "has been added to your inventory.")
                    self.addInventory(noun)
                    return
                elif (lowCaseItem == noun and item['Movable'] == 'n'):
                    print (item['Name'], "can't be added to your inventory.")
                    return
        elif (verb == 'open'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun == 'air vent'):
                        print ("You open ", item['Name'], "and inspect.")
                        print (item['Description'], "\n")
                        print ("You are entering...Cell House Roof.\n")
                        self.currentRoom = "Cell House Roof"
                        self.printRoomDescription()
                        return
                    elif (noun == 'pantry'):
                        print ("You open the ", item['Name'], "and inspect.")
                        print (item['Description'], "\n")
                        return
                    elif (noun == 'door lock control panel'):
                        if (item['HiddenItem'] == 'locked'):
                            for keyItem in self.playerInventory:
                                if (keyItem == 'warden key'):
                                    item['HiddenItem'] == 'none'
                                    print ("You open and inspect the door lock control panel.\n")
                                    print (item['Description'], "\n")
                                    print ("The door to the Armory has been unlocked.\n")
                                    self.passageList[SPtoA]['Locked'] = 'n'
                                    return
                            print (item['Description'], "\n")
                            print ("You need a certain key to open it.\n")
                            return
                        else:
                            print (item['ShortDesc'], "\n")
                            return
                    elif (noun == 'desk'):
                        if (item['HiddenItem'] == 'glue'):
                            item['HiddenItem'] = 'none'
                            print ("You open the desk.\n")
                            print (item['Description'], "\n")
                            print ("The glue has been added to your inventory.\n")
                            self.addInventory("glue")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print ("You cannot open this.\n")
                        return
        elif (verb == 'drop'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (item['Location'] == 'inventory'):
                        self.removeInventory(noun)
                        print (item['Name'], " has been removed from your inventory.")
                        return
                    else:
                        print ("This cannot be dropped.\n")
                        return
        elif (verb == 'look'):
            for item in self.roomList:
                if (item['Name'] == self.currentRoom):
                    print ("Location: ", item['Name'])
                    print (item['LongDesc'], '\n')
                    return
        elif (verb == 'lookat'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                print (lowCaseItem)
                if (lowCaseItem == noun):
                    if (noun == 'drain pipes'):
                        if (item['HiddenItem'] == 'Key'):
                            item['HiddenItem'] = 'none'
                            print (item['Description'], "\n")
                            print ("The key has been added to your inventory.")
                            self.addInventory("key")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    elif (noun == 'air vent'):
                        print (item['Description'], "\n")
                        print ("You are entering...Cell House Roof.\n")
                        self.currentRoom = "Cell House Roof"
                        self.printRoomDescription()
                        return
                    elif (noun == 'sky lights'):
                        print (item['Description'], "\n")
                        print ("You are returning to...Prison Cell.\n")
                        self.currentRoom = "Prison Cell"
                        self.printRoomDescription()
                        return
                    elif (noun == 'locking mechanism'):
                        if (item['HiddenItem'] == 'locked'):
                            item['HiddenItem'] == 'none'
                            print (item['Description'], "\n")
                            print ("The doors to the Mess Hall, Library, and Sally Port have been unlocked.\n")
                            self.passageList[CBAtoMH]['Locked'] = 'n'
                            self.passageList[CBAtoL]['Locked'] = 'n'
                            self.passageList[CBAtoSP]['Locked'] = 'n'
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    elif (noun == 'door lock control panel'):
                        if (item['HiddenItem'] == 'locked'):
                            print ("You inspect the door lock control panel. ", item['Description'], "\n")
                            print ("You need a certain key for it to work.\n")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    elif (noun == 'desk'):
                        if (item['HiddenItem'] == 'glue'):
                            item['HiddenItem'] = 'none'
                            print (item['Description'], "\n")
                            print ("The glue has been added to your inventory.")
                            self.addInventory("glue")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    elif (noun == 'coat rack'):
                        if (item['HiddenItem'] == 'raincoats'):
                            item['HiddenItem'] = 'none'
                            print (item['Description'], "\n")
                            print ("The raincoats been added to your inventory.")
                            self.addInventory("raincoats")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print (item['Name'], ": ")
                        print (item['Description'], "\n")
                        return
        elif (verb == 'help'):
            print ("Try these commands: hit, pull, eat, scratch, drop, break, throw, push, drink, ")
            print ("open, take, look, lookat, savegame, loadgame, help, inventory.")
            return
        elif (verb == 'inventory'):
            self.displayInventory()
            return
        elif (verb == 'throw'):
            for item in self.objectList:
                if (item['Name'] == noun and item['Location'] == 'Inventory'):
                    self.removeInventory(noun)
                    print (item['Name'], " has been removed from your inventory.")
                    return
        elif (verb == 'go'):
            for item in self.passageList:
                description = item['Description'].lower()
                if (item['Location'] == self.currentRoom and item['Direction'] == noun and item['Locked'] == 'n'):
                    print ("You are entering...\n")
                    self.currentRoom = item['Description']
                    self.printRoomDescription()
                    return
                elif (item['Location'] == self.currentRoom and item['Direction'] == noun and item['Locked'] == 'y'):
                    for keyItem in self.playerInventory:
                        if (item['KeytoOpen'] == keyItem):
                            print ("You use the key to unlock the door.\n")
                            item['Locked'] = 'n'
                            print ("You are entering...\n")
                            self.currentRoom = item['Description']
                            self.printRoomDescription()
                            return
                    print ("It's locked, see if you can find something to open it.")
                    return
                elif (item['Location'] == self.currentRoom and description == noun and item['Locked'] == 'n'):
                    print ("You are entering...\n")
                    self.currentRoom = item['Description']
                    self.printRoomDescription()
                    return
                elif (item['Location'] == self.currentRoom and description == noun and item['Locked'] == 'y'):
                    for keyItem in self.playerInventory:
                        if (item['KeytoOpen'] == keyItem):
                            print ("You use the key to unlock the door.\n")
                            item['Locked'] = 'n'
                            print ("You are entering...\n")
                            self.currentRoom = item['Description']
                            self.printRoomDescription()
                            return
                    print ("It's locked, see if you can find something to open it.")
                    return
        elif (verb == 'hit'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun  == 'door lock control panel'):
                        if (item['HiddenItem'] == 'locked'):
                            print ("item['Description']", "You try hitting it and pressing buttons.\n")
                            print ("Nothing works without a certain key.\n")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print ("I don't think you want to hit that.")
                        return
        elif (verb == 'pull'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun == 'air vent'):
                        print ("You pull open the air vent.\n")
                        print (item['Description'], "\n")
                        print ("You are entering...Cell House Roof.\n")
                        self.currentRoom = "Cell House Roof"
                        self.printRoomDescription()
                        return
                    elif (noun == 'coat rack'):
                        if (item['HiddenItem'] == 'raincoats'):
                            item['HiddenItem'] = 'none'
                            print ("You tug on the coat rack.\n")
                            print (item['Description'], "\n")
                            print ("The raincoats been added to your inventory.")
                            self.addInventory("raincoats")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print ("I don't think you want to pull that.")
                        return
        elif (verb == 'eat'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun == 'gum' and item['Location'] == 'Inventory'):
                        print ("You want to eat the old gum? That is disgusting.\n")
                        return
                    else:
                        print ("I don't think you want to eat that.\n")
                        return
        elif (verb == 'scratch'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun == 'tables' and item['Location'] == 'Mess Hall'):
                        if (item['HiddentItem'] == 'gum'):
                            item['HiddenItem'] = 'none'
                            print ("You scratch at the tables.\n")
                            print (item['Description'], "\n")
                            print ("The gum has been added to your inventory.\n")
                            self.addInventory("gum")
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print ("I don't think you want to scratch that.")
                        return
        elif (verb == 'break'):
            print ("I don't think you want to break that.")
        elif (verb == 'push'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun):
                    if (noun == 'locking mechanism'):
                        if (item['HiddenItem'] == 'locked'):
                            item['HiddenItem'] == 'none'
                            print (item['Description'], "\n")
                            print ("The doors to the Mess Hall, Library, and Sally Port have been unlocked.\n")
                            self.passageList[CBAtoMH]['Locked'] = 'n'
                            self.passageList[CBAtoL]['Locked'] = 'n'
                            self.passageList[CBAtoSP]['Locked'] = 'n'
                            return
                        else:
                            print (item['Name'], ": ")
                            print (item['ShortDesc'], "\n")
                            return
                    else:
                        print ("I don't think you want to push that.")
        elif (verb == 'drink'):
            print ("I don't think you want to drink that.")
        elif (verb == 'savegame'):
            self.saveGame()
            return
        elif (verb == 'loadgame'):
            self.loadSavedGame()
            self.printRoomDescription()
            return
        elif (verb == 'quit'):
            save = input("Would you like to save your game? (y or n) > ")
            if (save == 'y'):
                self.saveGame()
                return
            elif (save == 'n'):
                return
            else:
                print ("Not a valid input, next time try just y or n\n")
                print ("Quit game aborted\n")
    #hit', 'pull', 'eat', 'scratch', 'break', 'push', 'drink',  

    def setRoomStatus(self, roomName):
        for item in self.roomList:
            if (item['Name'] == roomName):
                if (item['Status'] == 'not visited'):
                    item['Status'] = 'visited'
                    #print ("Room status changed to", item['Status'])#for testing

    # Not sure this function is needed
    def getRoomStatus(self):
        for item in self.roomList:
            if (item['Name'] == self.currentRoom):
                return (item['Status'])

    def addObject(self, objectDict):
        self.objectList.append(objectDict)
        #print ("Object added to the list")#for testing

    def addPassage(self, passageDict):
        self.passageList.append(passageDict)
        #print("Passage added to list")#for testing

    def addInventory(self, itemName):
        self.playerInventory.append(itemName)
        for item in self.objectList:
            if (item['Name'] == itemName):
                item['Location'] = 'inventory'
                #print ("Item added to inventory")#for testing

    def removeInventory(self, itemName):
        for item in self.playerInventory:
            if (item == itemName):
                self.playerInventory.remove(item)
                for item in self.objectList:
                    if (item['Name'] == itemName):
                        item['Location'] = self.currentRoom
                        #print ("Item added to inventory")#for testing

    def printRoomDescription(self):
        for item in self.roomList:
            rmName = str(item['Name'])
            if (item['Name'] == self.currentRoom):
                if (item['Status'] == 'visited'):
                    print ("Location: ", item['Name'])
                    print (item['ShortDesc'], '\n')
                    print ("Inventory: ")
                    self.displayInventory()
                else:
                    print ("Location: ", item['Name'])
                    print (item['LongDesc'], '\n')
                    self.setRoomStatus(self.currentRoom)
                    print ("Inventory: ")
                    self.displayInventory()
                break

    def loadSavedGame(self):

        self.playerInventory = []
        dataSet = 0
        tempRoom = []
        tempObject = []
        tempPassage = []

        fo = open('savedgame.txt', 'r')
        
        line = fo.readlines()

        fo.close()

        for item in line:

            tempStr = item.rstrip()

            if (tempStr == '*'):
                dataSet += 1
                continue
     
            if (dataSet == 0):
                self.currentRoom = tempStr
            elif (dataSet == 1):
                tempRoom.append(tempStr)
            elif (dataSet == 2):
                tempObject.append(tempStr)
            elif (dataSet == 3):
                tempPassage.append(tempStr)
            elif (dataSet == 4):
                self.addInventory(tempStr)

        for index in range(len(tempRoom)):
            temp = self.roomList[index]
            temp['Status'] = tempRoom[index]

        for index in range(len(tempObject)):
            temp = self.objectList[index]
            temp['Location'] = tempObject[index]

        for index in range(len(tempPassage)):
            temp = self.passageList[index]
            temp['Locked'] = tempPassage[index]                   

    def saveGame(self):
        fo = open("savedgame.txt", "w+")

        fo.write(self.currentRoom + '\n*\n')

        for item in self.roomList:
            fo.write(item['Status'] + '\n')
        fo.write('*\n')

        for item in self.objectList:
            fo.write(item['Location'] + '\n')
        fo.write('*\n')

        for item in self.passageList:
            fo.write(item['Locked'] + '\n')
        fo.write('*\n')

        for item in self.playerInventory:
            fo.write(item)

        fo.close()

    def createRoom(self, roomDict):
        self.roomList.append(roomDict)
        #print ("Room added to the list")#for testing

    def printDescription(self, objectName):
        for item in self.objectList:
            if (item['Name'] == objectNameName):
                if (item['Location'] == self.currentRoom):
                    print ("Room status changed to", item['Status'])#for testing

    def displayInventory(self):
        print (self.playerInventory, '\n')

    def testSuite(self):
        #print ("**********This is a testing function that was called**********")
        #print ("List of all rooms loaded: \n")
        #print (self.roomList)
        #print ("List of all passages loaded: \n")
        #print (self.passageList)
        print ("List of all objects loaded: \n")
        print (self.objectList)
        #print ("Current room: \n")
        #print (self.currentRoom)
        print ("********************End of Test Function***********************")


    def gameOver(self):
        for item in self.objectList:
            if (item['Name'] == 'Key'):
                if (item['Location'] == 'Cell Block' and self.currentRoom == 'Cell Block'):
                    print("Demo Over")
                    return 1
        return 0
