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
                if (item['Name'] == noun):
                    print ("You open ", item['Name'], "and inspect.")
                    print (item['Description'], "\n")
                    return
        elif (verb == 'drop'):
            for item in self.objectList:
                tmpItem = item['Name']
                lowCaseItem = tmpItem.lower()
                if (lowCaseItem == noun and item['Location'] == 'Inventory'):
                    self.removeInventory(noun)
                    print (item['Name'], " has been removed from your inventory.")
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
                print (item['Location'])
                print (self.currentRoom)
                print (item['Direction'])
                print (noun)
                print (item['Locked'])
                if (item['Location'] == self.currentRoom and item['Direction'] == noun and item['Locked'] == 'n'):
                    print ("You are entering...\n")
                    self.currentRoom = item['Description']
                    self.printRoomDescription()
                    return
                elif (item['Location'] == self.currentRoom and item['Direction'] == noun and item['Locked'] == 'y'):
                    print ("It's locked, see if you can find something to open it.")
                    return
        elif (verb == 'hit'):
            print ("I don't think you want to hit that.")
        elif (verb == 'pull'):
            print ("I don't think you want to pull that.")
        elif (verb == 'eat'):
            print ("I don't think you want to eat that.")
        elif (verb == 'scratch'):
            print ("I don't think you want to scratch that.")
        elif (verb == 'break'):
            print ("I don't think you want to break that.")
        elif (verb == 'push'):
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