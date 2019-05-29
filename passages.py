import sys
import os
import gameState
import gameEngine

def createPassages(newGame):


    PCtoCBA = {'Name': 'PCtoCBA', 'Description': 'Cell Block A', 'Location': 'Prison Cell', 'Direction': 'South', 'Locked': 'y', 'KeytoOpen': 'key'}
    newGame.addPassage(PCtoCBA)

    CBAtoPC = {'Name': 'CBAtoPC', 'Description': 'Prison Cell', 'Location': 'Cell Block A', 'Direction': 'North', 'Locked': 'y', 'KeytoOpen': 'key'}
    newGame.addPassage(CBAtoPC)

    CBAtoMH = {'Name': 'CBAtoMH', 'Description': 'Mess Hall', 'Location': 'Cell Block A', 'Direction': 'West', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(CBAtoMH)

    MHtoCBA = {'Name': 'MHtoCBA', 'Description': 'Cell Block A', 'Location': 'Mess Hall', 'Direction': 'East', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(MHtoCBA)

    MHtoK = {'Name': 'MHtoK', 'Description': 'Kitchen', 'Location': 'Mess Hall', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(MHtoK)

    KtoMH = {'Name': 'KtoMH', 'Description': 'Mess Hall', 'Location': 'Kitchen', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(KtoMH)

    CBAtoL = {'Name': 'CBAtoL', 'Description': 'Library', 'Location': 'Cell Block A', 'Direction': 'South', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(CBAtoL)

    LtoCBA = {'Name': 'LtoCBA', 'Description': 'Cell Block A', 'Location': 'Library', 'Direction': 'North', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(LtoCBA)

    CBAtoSP = {'Name': 'CBAtoSP', 'Description': 'Sally Port', 'Location': 'Cell Block A', 'Direction': 'East', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(CBAtoSP)

    SPtoCBA = {'Name': 'SPtoCBA', 'Description': 'Cell Block A', 'Location': 'Sally Port', 'Direction': 'West', 'Locked': 'y', 'KeytoOpen': 'lockingMech'}
    newGame.addPassage(SPtoCBA)

    SPtoA = {'Name': 'SPtoA', 'Description': 'Armory', 'Location': 'Sally Port', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(SPtoA)

    AtoSP = {'Name': 'AtoSP', 'Description': 'Sally Port', 'Location': 'Armory', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(AtoSP)

    SPtoVR = {'Name': 'SPtoVR', 'Description': 'Visiting Room', 'Location': 'Sally Port', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(SPtoVR)

    VRtoSP = {'Name': 'VRtoSP', 'Description': 'Sally Port', 'Location': 'Visiting Room', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(VRtoSP)

    VRtoYARD = {'Name': 'VRtoYARD', 'Description': 'Yard', 'Location': 'Visiting Room', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(VRtoYARD)
	
    YARDtoVR = {'Name': 'YARDtoVR', 'Description': 'Visiting Room', 'Location': 'Yard', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(YARDtoVR)

    RYtoYARD = {'Name': 'RYtoYARD', 'Description': 'Yard', 'Location': 'Recreation Yard', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(RYtoYARD)

    YARDtoRY = {'Name': 'YARDtoRY', 'Description': 'Recreation Yard', 'Location': 'Yard', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(YARDtoRY)

    YARDtoGH = {'Name': 'YARDtoGH', 'Description': 'Guardhouse', 'Location': 'Yard', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(YARDtoGH)

    GHtoYARD = {'Name': 'GHtoYARD', 'Description': 'Yard', 'Location': 'Guardhouse', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(GHtoYARD)

    YARDtoDOCK = {'Name': 'YARDtoDOCK', 'Description': 'Dock', 'Location': 'Yard', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(YARDtoDOCK)

    DOCKtoYARD = {'Name': 'DOCKtoYARD', 'Description': 'Yard', 'Location': 'Dock', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(DOCKtoYARD)

    DOCKtoBOAT = {'Name': 'DOCKtoBOAT', 'Description': 'Boat', 'Location': 'Dock', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(DOCKtoBOAT)

    BOATtoDOCK = {'Name': 'BOATtoDOCK', 'Description': 'Dock', 'Location': 'Boat', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(BOATtoDOCK)

    LtoRY = {'Name': 'LtoRY', 'Description': 'Recreation Yard', 'Location': 'Library', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(LtoRY)

    RYtoL = {'Name': 'RYtoL', 'Description': 'Library', 'Location': 'Recreation Yard', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(RYtoL)

    RYtoWO = {'Name': 'RYtoWO', 'Description': 'Warden Office', 'Location': 'Recreation Yard', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(RYtoWO)

    WOtoRY = {'Name': 'WOtoRY', 'Description': 'Recreation Yard', 'Location': 'Warden Office', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(WOtoRY)
