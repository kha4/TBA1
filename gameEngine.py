from time import sleep
import mainMenu
import gameState
import roomParser
import textParser
import gameObjects
import passages
import sys
from os import system, name

def main():

    menuSelection = mainMenu.display()

    if (menuSelection == "1"):
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
        gameObjects.createObjectList(newGame)
        passages.createPassages(newGame)
    elif (menuSelection == "2"):
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
        gameObjects.createObjectList(newGame)
        passages.createPassages(newGame)
        newGame.loadSavedGame()
    else:
        print ("Goodbye")

    #gameplay loop would start here
    newGame.printRoomDescription()

    #Call for testing
    newGame.testSuite()

    while (newGame.gameOver() == 0):
        verb, noun = textParser.parse(newGame)
        newGame.modifyState(verb, noun)


if __name__ == "__main__":
    main()
