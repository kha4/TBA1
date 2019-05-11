import sys
import os
import gameState
import gameEngine

def createPassages(newGame):


	PCtoCBA = {'Name': 'PCtoCBA', 'Description': 'Moving to Cell Block A.', 'Location': 'Prison Cell', 'Locked': 'y', 'KeytoOpen': 'key'}
	newGame.addPassage(PCtoCBA)

	CBAtoPC = {'Name': 'CBAtoPC', 'Description': 'Moving to Prison Cell.', 'Location': 'Cell Block A', 'Locked': 'y', 'KeytoOpen': 'key'}
	newGame.addPassage(CBAtoPC)

	CBAtoL = {'Name': 'CBAtoL', 'Description': 'Moving to Library.', 'Location': 'Cell Block A', 'Locked': 'n'}
	newGame.addPassage(CBAtoL)

	LtoCBA = {'Name': 'LtoCBA', 'Description': 'Moving to Cell Block A.', 'Location': 'Library', 'Locked': 'n'}
	newGame.addPassage(LtoCBA)

	CBAtoVR = {'Name': 'CBAtoVR', 'Description': 'Moving to Visiting Room.', 'Location': 'Cell Block A', 'Locked': 'n'}
	newGame.addPassage(CBAtoVR)

	VRtoCBA = {'Name': 'VRtoCBA', 'Description': 'Moving to Cell Block A.', 'Location': 'Visiting Room', 'Locked': 'n'}
	newGame.addPassage(VRtoCBA)

	VRtoYARD = {'Name': 'VRtoYARD', 'Description': 'Moving to Yard.', 'Location': 'Visiting Room', 'Locked': 'n'}
	newGame.addPassage(VRtoYARD)

	YARDtoVR = {'Name': 'YARDtoVR', 'Description': 'Moving to Visiting Room.', 'Location': 'Yard', 'Locked': 'n'}
	newGame.addPassage(YARDtoVR)
