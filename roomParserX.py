import sys
import os
import gameState
import gameEngine

def parseNewRoomData(newGame):

	prisonCell = {}
	with open ('prisonCell.txt', 'rt') as pcFile:
		line = pcFile.readline()
		cnt = 1
		while line:
			if cnt == 1:
				prisonCell['Name'] = line
			elif cnt == 2:
				prisonCell['LongDesc'] = line
			elif cnt == 3:
				prisonCell['ShortDesc'] = line
			else:
				prisonCell['Status'] = line
			cnt += 1
			line = pcFile.readline()
	newGame.createRoom(prisonCell)

	sallyPort = {}
	with open('sallyPort.txt', 'rt') as spFile:
		line = spFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                sallyPort['Name'] = line
                        elif cnt == 2:
                                sallyPort['LongDesc'] = line
                        elif cnt == 3:
                                sallyPort['ShortDesc'] = line
                        else:
                                sallyPort['Status'] = line
                        cnt += 1
                        line = spFile.readline()
        newGame.createRoom(sallyPort)

	armory = {}
	with open('armory.txt', 'rt') as aFile:
		line = aFile.readline()
		cnt = 1
		while line:
			if cnt == 1:
                                armory['Name'] = line
                        elif cnt == 2:
                                armory['LongDesc'] = line
                        elif cnt == 3:
                                armory['ShortDesc'] = line
                        else:
                                armory['Status'] = line
                        cnt += 1
                        line = aFile.readline()
        newGame.createRoom(armory)


	visitingRoom = {}
	with open('visitingRoom.txt', 'rt') as vrFile:
		line = vrFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                visitingRoom['Name'] = line
                        elif cnt == 2:
                                visitingRoom['LongDesc'] = line
                        elif cnt == 3:
                                visitingRoom['ShortDesc'] = line
                        else:
                                visitingRoom['Status'] = line
                        cnt += 1
                        line = vrFile.readline()
        newGame.createRoom(visitingRoom)


	library = {}
	with open('library.txt', 'rt') as lFile:
		line = lFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                library['Name'] = line
                        elif cnt == 2:
                                library['LongDesc'] = line
                        elif cnt == 3:
                                library['ShortDesc'] = line
                        else:
                                library['Status'] = line
                        cnt += 1
                        line = lFile.readline()
        newGame.createRoom(library)


	cellBlockA = {}
	with open ('cellBlockA.txt', 'rt') as cbaFile:
		line = cbaFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                cellBlockA['Name'] = line
                        elif cnt == 2:
                                cellBlockA['LongDesc'] = line
                        elif cnt == 3:
                                cellBlockA['ShortDesc'] = line
                        else:
                                cellBlockA['Status'] = line
                        cnt += 1
                        line = cbaFile.readline()
        newGame.createRoom(cellBlockA)


	crawlSpace = {}
	with open ('crawlSpace.txt', 'rt') as csFile:
		line = csFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                crawlSpace['Name'] = line
                        elif cnt == 2:
                                crawlSpace['LongDesc'] = line
                        elif cnt == 3:
                                crawlSpace['ShortDesc'] = line
                        else:
                                crawlSpace['Status'] = line
                        cnt += 1
                        line = csFile.readline()
        newGame.createRoom(crawlSpace)


	messHall = {}
	with open ('messHall.txt', 'rt') as mhFile:
		line = mhFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                messHall['Name'] = line
                        elif cnt == 2:
                                messHall['LongDesc'] = line
                        elif cnt == 3:
                                messHall['ShortDesc'] = line
                        else:
                                messHall['Status'] = line
                        cnt += 1
                        line = mhFile.readline()
        newGame.createRoom(messHall)


	kitchen = {}
	with open ('kitchen.txt', 'rt') as kFile:
		line = kFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                kitchen['Name'] = line
                        elif cnt == 2:
                                kitchen['LongDesc'] = line
                        elif cnt == 3:
                                kitchen['ShortDesc'] = line
                        else:
                                kitchen['Status'] = line
                        cnt += 1
                        line = kFile.readline()
        newGame.createRoom(kitchen)


	guardHouse = {}
	with open ('guardHouse.txt', 'rt') as ghFile:
		line = ghFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                guardHouse['Name'] = line
                        elif cnt == 2:
                                guardHouse['LongDesc'] = line
                        elif cnt == 3:
                                guardHouse['ShortDesc'] = line
                        else:
                                guardHouse['Status'] = line
                        cnt += 1
                        line = ghFile.readline()
        newGame.createRoom(guardHouse)


	powerPlant = {}
	with open ('powerPlant.txt', 'rt') as ppFile:
		line = ppFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                powerPlant['Name'] = line
                        elif cnt == 2:
                                powerPlant['LongDesc'] = line
                        elif cnt == 3:
                                powerPlant['ShortDesc'] = line
                        else:
                                powerPlant['Status'] = line
                        cnt += 1
                        line = ppFile.readline()
        newGame.createRoom(powerPlant)


	lightHouse = {}
	with open ('lightHouse.txt', 'rt') as lhFile:
		line = lhFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                lightHouse['Name'] = line
                        elif cnt == 2:
                                lightHouse['LongDesc'] = line
                        elif cnt == 3:
                                lightHouse['ShortDesc'] = line
                        else:
                                lightHouse['Status'] = line
                        cnt += 1
                        line = lhFile.readline()
        newGame.createRoom(lightHouse)


	dock = {}
	with open ('dock.txt', 'rt') as dFile:
		line = dFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                dock['Name'] = line
                        elif cnt == 2:
                                dock['LongDesc'] = line
                        elif cnt == 3:
                                dock['ShortDesc'] = line
                        else:
                                dock['Status'] = line
                        cnt += 1
                        line = dFile.readline()
        newGame.createRoom(dock)


	electricShop = {}
	with open ('electricShop.txt', 'rt') as esFile:
		line = esFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                electricShop['Name'] = line
                        elif cnt == 2:
                                electricShop['LongDesc'] = line
                        elif cnt == 3:
                                electricShop['ShortDesc'] = line
                        else:
                                electricShop['Status'] = line
                        cnt += 1
                        line = esFile.readline()
        newGame.createRoom(electricShop)


	recreationYard = {}
	with open ('recreationYard.txt', 'rt') as ryFile:
		line = ryFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                recreationYard['Name'] = line
                        elif cnt == 2:
                                recreationYard['LongDesc'] = line
                        elif cnt == 3:
                                recreationYard['ShortDesc'] = line
                        else:
                                recreationYard['Status'] = line
                        cnt += 1
                        line = ryFile.readline()
        newGame.createRoom(recreationYard)


	cellHouseRoof = {}
	with open ('cellHouseRoof.txt', 'rt') as chrFile:
		line = chrFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                cellHouseRoof['Name'] = line
                        elif cnt == 2:
                                cellHouseRoof['LongDesc'] = line
                        elif cnt == 3:
                                cellHouseRoof['ShortDesc'] = line
                        else:
                                cellHouseRoof['Status'] = line
                        cnt += 1
                        line = chrFile.readline()
        newGame.createRoom(cellHouseRoof)


	boat = {}
	with open ('boat.txt', 'rt') as bFile:
		line = bFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                boat['Name'] = line
                        elif cnt == 2:
                                boat['LongDesc'] = line
                        elif cnt == 3:
                                boat['ShortDesc'] = line
                        else:
                                boat['Status'] = line
                        cnt += 1
                        line = bFile.readline()
        newGame.createRoom(boat)


	carpentryShop = {}
	with open ('carpentryShop.txt', 'rt') as carpFile:
		line = carpFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                carpentryShop['Name'] = line
                        elif cnt == 2:
                                carpentryShop['LongDesc'] = line
                        elif cnt == 3:
                                carpentryShop['ShortDesc'] = line
                        else:
                                carpentryShop['Status'] = line
                        cnt += 1
                        line = carpFile.readline()
        newGame.createRoom(carpentryShop)


	wardenOffice = {}
	with open ('wardenOffic.txt', 'rt') as woFile:
		line = woFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                wardenOffice['Name'] = line
                        elif cnt == 2:
                                wardenOffice['LongDesc'] = line
                        elif cnt == 3:
                                wardenOffice['ShortDesc'] = line
                        else:
                                wardenOffice['Status'] = line
                        cnt += 1
                        line = woFile.readline()
        newGame.createRoom(wardenOffice)


	yard = {}
	with open ('yard.txt', 'rt') as yardFile:
		line = yardFile.readline()
                cnt = 1
                while line:
                        if cnt == 1:
                                yard['Name'] = line
                        elif cnt == 2:
                                yard['LongDesc'] = line
                        elif cnt == 3:
                                yard['ShortDesc'] = line
                        else:
                                yard['Status'] = line
                        cnt += 1
                        line = yardFile.readline()
        newGame.createRoom(yard)
