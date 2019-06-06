################################################################################
## TBA1 - Melissa Barr/ Kevin Ha / Christopher Perry                          ##
## CS 467 - Capstone - June 4, 2019                                           ##
## This file contains the main function, starts the game, and initiates the   ##
## a game instance.                                                           ##
################################################################################


from time import sleep
import mainMenu
import gameState
import roomParser
import textParser
import gameObjects
import passages
import sys
import os
from os import system, name

def main():

    #checking that the column size is big enough
    rows, columns = os.popen('stty size', 'r').read().split()
    if int(columns) < 172:
        print ("Please increase your column size to at least 176")
        exit()
    menuSelection = 0
    # Main menu display is called
    menuSelection = mainMenu.display()
    # Validation for main menu input
    while (menuSelection != '1' and menuSelection != "2" and menuSelection != "3"):
        print ("Try again, enter 1, 2, or 3.")
        menuSelection  = input("> ")

    if (menuSelection == "1"): # New game is started
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
        gameObjects.createObjectList(newGame)
        passages.createPassages(newGame)
    elif (menuSelection == "2"): # Saved game is loaded
        newGame = gameState.gameState()
        roomParser.parseNewRoomData(newGame)
        gameObjects.createObjectList(newGame)
        passages.createPassages(newGame)
        newGame.loadSavedGame()
    else:
        print ("Goodbye")
        return 0;

    # Print starting room description
    newGame.printRoomDescription()

    #Call for testing
    #newGame.testSuite()

    verb = 'blank' # verb intialized 

    ##############################################################
    ## Gameplay loop begins here, winning state is checked for  ##
    ## time as well as if the player wants to quit.             ##
    ##############################################################
    while (newGame.gameOver() == 0 and verb != 'quit'):
        verb, noun = textParser.parse(newGame)
        if (verb == 'quit'):
            newGame.quitGame()
        else:
            newGame.modifyState(verb, noun)


if __name__ == "__main__":
    main()
