import roomParser
from roomParser import parseNewRoomData

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
        print ("GameState Instance Created")#for testing

    def setRoomStatus(self, roomName):
        for item in self.roomList:
            if (item['Name'] == roomName):
                if (item['Status'] == 'not visited'):
                    item['Status'] = 'visited'
                    print ("Room status changed to", item['Status'])#for testing

    # Not sure this function is needed
    def getRoomStatus(self):
        for item in self.roomList:
            if (item['Name'] == self.currentRoom):
                return (item['Status'])

    def addObject(self, objectDict):
        self.objectList.append(objectDict)
        print ("Object added to the list")#for testing

    def addPassage(self, passages):
        print("Need to discuss this one")

    def addInventory(self, item):
        print ("Code needed")#replace with code

    def removeInventory(self, item):
        print ("Code needed")#replace with code

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

    def loadSavedGame(self):
        print ("Load game function: code needed")#replace with code

    def saveGame(self):
        print ("Code needed")#replace with code

    def createRoom(self, roomDict):
        self.roomList.append(roomDict)
        print ("Room added to the list")#for testing
