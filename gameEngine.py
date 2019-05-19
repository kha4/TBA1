from time import sleep
import mainMenu
import gameState
import roomParser
import textParser
import sys
from os import system, name

def main():

    menuSelection = mainMenu.display()

    #print(menuSelection) #for testing

    if (menuSelection == "1"):
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
    elif (menuSelection == "2"):
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
        newGame.loadSavedGame()
    else:
        print ("Goodbye")

    #gameplay loop would start here
    newGame.printRoomDescription()

    #print (newGame.objectList)
    #print (newGame.passageList)

    while (newGame.gameOver() == 0):
        verb, noun = textParser.userInput()
        newGame.modifyState(verb, noun)
        #newGame.displayInventory() #for testing






if __name__ == "__main__":
    main()
