from time import sleep
import mainMenu
import gameState
import sys
from os import system, name

def main():

    menuSelection = mainMenu.display()

    #print(menuSelection) #for testing

    if (menuSelection == "1"):
        newGame = gameState.gameState()
    elif (menuSelection == "2"):
        savedGame = gameState.gameState()
        savedGame.loadSavedGame()
    else:
        print ("Goodbye")

    #gameplay loop would start here




if __name__ == "__main__":
    main()