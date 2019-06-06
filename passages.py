import sys
import os
import gameState
import gameEngine

def createPassages(newGame):

    #add passage from prison cell to cell block a
    PCtoCBA = {'Name': 'PCtoCBA', 'Description': 'Cell Block A', 'Location': 'Prison Cell', 'Direction': 'south', 'Locked': 'y', 'KeytoOpen': 'key'}
    newGame.addPassage(PCtoCBA)

    #add passage from cell block a to prison cell
    CBAtoPC = {'Name': 'CBAtoPC', 'Description': 'Prison Cell', 'Location': 'Cell Block A', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(CBAtoPC)

    #add passage from cell block a to mess hall
    CBAtoMH = {'Name': 'CBAtoMH', 'Description': 'Mess Hall', 'Location': 'Cell Block A', 'Direction': 'West', 'Locked': 'y', 'KeytoOpen': 'locking mechanism'}
    newGame.addPassage(CBAtoMH)

    #add passage from mess hall to cell block a
    MHtoCBA = {'Name': 'MHtoCBA', 'Description': 'Cell Block A', 'Location': 'Mess Hall', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(MHtoCBA)

    #add passage from mess hall to kitchen
    MHtoK = {'Name': 'MHtoK', 'Description': 'Kitchen', 'Location': 'Mess Hall', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(MHtoK)

    #add passage from kitchen to mess hall
    KtoMH = {'Name': 'KtoMH', 'Description': 'Mess Hall', 'Location': 'Kitchen', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(KtoMH)

    #add passage from cell block a to library
    CBAtoL = {'Name': 'CBAtoL', 'Description': 'Library', 'Location': 'Cell Block A', 'Direction': 'South', 'Locked': 'y', 'KeytoOpen': 'locking mechanism'}
    newGame.addPassage(CBAtoL)

    #add passage from library to cell block a
    LtoCBA = {'Name': 'LtoCBA', 'Description': 'Cell Block A', 'Location': 'Library', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(LtoCBA)

    #add passage from cell block a to sally port
    CBAtoSP = {'Name': 'CBAtoSP', 'Description': 'Sally Port', 'Location': 'Cell Block A', 'Direction': 'East', 'Locked': 'y', 'KeytoOpen': 'locking mechanism'}
    newGame.addPassage(CBAtoSP)

    #add passage from sally port to cell block a
    SPtoCBA = {'Name': 'SPtoCBA', 'Description': 'Cell Block A', 'Location': 'Sally Port', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(SPtoCBA)

    #add passage from sally port to armory
    SPtoA = {'Name': 'SPtoA', 'Description': 'Armory', 'Location': 'Sally Port', 'Direction': 'North', 'Locked': 'y', 'KeytoOpen': 'door lock control panel'}
    newGame.addPassage(SPtoA)

    #add passage from armory to sally port
    AtoSP = {'Name': 'AtoSP', 'Description': 'Sally Port', 'Location': 'Armory', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(AtoSP)

    #add passage from sally port to visiting room
    SPtoVR = {'Name': 'SPtoVR', 'Description': 'Visiting Room', 'Location': 'Sally Port', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(SPtoVR)

    #add passage from visiting room to sally port
    VRtoSP = {'Name': 'VRtoSP', 'Description': 'Sally Port', 'Location': 'Visiting Room', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(VRtoSP)

    #add passage from visiting room to yard
    VRtoYARD = {'Name': 'VRtoYARD', 'Description': 'Yard', 'Location': 'Visiting Room', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(VRtoYARD)

    #add passage from yard to visiting room
    YARDtoVR = {'Name': 'YARDtoVR', 'Description': 'Visiting Room', 'Location': 'Yard', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(YARDtoVR)

    #add passage from recreation yard to yard
    RYtoYARD = {'Name': 'RYtoYARD', 'Description': 'Yard', 'Location': 'Recreation Yard', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(RYtoYARD)

    #add passage from yard to recreation yard
    YARDtoRY = {'Name': 'YARDtoRY', 'Description': 'Recreation Yard', 'Location': 'Yard', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(YARDtoRY)

    #add passage from yard to guardhouse
    YARDtoGH = {'Name': 'YARDtoGH', 'Description': 'Guardhouse', 'Location': 'Yard', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(YARDtoGH)

    #add passage from guardhouse to yard
    GHtoYARD = {'Name': 'GHtoYARD', 'Description': 'Yard', 'Location': 'Guardhouse', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(GHtoYARD)

    #add passage from yad to dock
    YARDtoDOCK = {'Name': 'YARDtoDOCK', 'Description': 'Dock', 'Location': 'Yard', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(YARDtoDOCK)

    #add passage from dock to yard
    DOCKtoYARD = {'Name': 'DOCKtoYARD', 'Description': 'Yard', 'Location': 'Dock', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(DOCKtoYARD)

    #add passage from dock to boat
    DOCKtoBOAT = {'Name': 'DOCKtoBOAT', 'Description': 'Boat', 'Location': 'Dock', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(DOCKtoBOAT)

    #add passage from boat to dock
    BOATtoDOCK = {'Name': 'BOATtoDOCK', 'Description': 'Dock', 'Location': 'Boat', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(BOATtoDOCK)

    #add passage from library to recreation yard
    LtoRY = {'Name': 'LtoRY', 'Description': 'Recreation Yard', 'Location': 'Library', 'Direction': 'South', 'Locked': 'n'}
    newGame.addPassage(LtoRY)

    #add passage from recreation yard to library
    RYtoL = {'Name': 'RYtoL', 'Description': 'Library', 'Location': 'Recreation Yard', 'Direction': 'North', 'Locked': 'n'}
    newGame.addPassage(RYtoL)

    #add passage from recreation yard to warden office
    RYtoWO = {'Name': 'RYtoWO', 'Description': 'Warden Office', 'Location': 'Recreation Yard', 'Direction': 'West', 'Locked': 'n'}
    newGame.addPassage(RYtoWO)

    #add passage from warden office to recreation yard
    WOtoRY = {'Name': 'WOtoRY', 'Description': 'Recreation Yard', 'Location': 'Warden Office', 'Direction': 'East', 'Locked': 'n'}
    newGame.addPassage(WOtoRY)
