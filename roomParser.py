import sys
import os

def parseNewRoomData():

	prisonCell = []
	with open ('prisonCell.txt', 'rt') as pcFile:
		for pcLine in pcFile:
			prisonCell.append(pcLine)

	sallyPort = []
	with open('sallyPort.txt', 'rt') as spFile:
		for spLine in spFile:
			sallyPort.append(spLine)

	armory = []
	with open('armory.txt', 'rt') as aFile:
		for aLine in aFile:
			armory.append(aLine)

	visitingRoom = []
	with open('visitingRoom.txt', 'rt') as vrFile:
		for vrLine in vrFile:
			visitingRoom.append(vrLine)

	library = []
	with open('library.txt', 'rt') as lFile:
		for lLine in lFile:
			library.append(lLine)

	cellBlockA = []
	with open ('cellBlockA.txt', 'rt') as cbaFile:
		for cbaLine in cbaFile:
			cellBlockA.append(cbaLine)

	crawlSpace = []
	with open ('crawlSpace.txt', 'rt') as csFile:
		for csLine in csFile:
			crawlSpace.append(csLine)

	messHall = []
	with open ('messHall.txt', 'rt') as mhFile:
		for mhLine in mhFile:
			messHall.append(mhLine)

	kitchen = []
	with open ('kitchen.txt', 'rt') as kFile:
		for kLine in kFile:
			kitchen.append(kLine)

	guardHouse = []
	with open ('guardHouse.txt', 'rt') as ghFile:
		for ghLine in ghFile:
			guardHouse.append(ghLine)

	powerPlant = []
	with open ('powerPlant.txt', 'rt') as ppFile:
		for ppLine in ppFile:
			powerPlant.append(ppLine)

	lightHouse = []
	with open ('lightHouse.txt', 'rt') as lhFile:
		for lhLine in lhFile:
			lightHouse.append(lhLine)

	dock = []
	with open ('dock.txt', 'rt') as dFile:
		for dLine in dFile:
			dock.append(dLine)

	electricShop = []
	with open ('electricShop.txt', 'rt') as esFile:
		for esLine in esFile:
			electricShop.append(esLIne)

	recreationYard = []
	with open ('recreationYard.txt', 'rt') as ryFile:
		for ryLine in ryFile:
			recreationYard.append(ryLine)

	cellHouseRoof = []
	with open ('cellHouseRoof.txt', 'rt') as chrFile:
		for chrLine in chrFile:
			cellHouseRoof.append(chrLine)

	boat = []
	with open ('boat.txt', 'rt') as bFile:
		for bLine in bFile:
			boat.append(bLine)

	carpentryShop = []
	with open ('carpentryShop.txt', 'rt') as carpFile:
		for carpLine in carpFile:
			carpentryShopt.append(carpLine)

	wardenOffice = []
	with open ('wardenOffic.txt', 'rt') as woFile:
		for woLine in woFile:
			wardenOffice.append(woLine)

	yard = []
	with open ('yard.txt', 'rt') as yardFile:
		for yardLine in yardFile:
			yard.append(yardLine)

	rooms = []
	rooms.append(prisonCell)
	rooms.append(sallyPort)
	rooms.append(armory)
	rooms.append(visitingRoom)
	rooms.append(library)
	rooms.append(cellBlockA)
	rooms.append(crawlSpace)
	rooms.append(messHall)
	rooms.append(kitchen)
	rooms.append(guardHouse)
	rooms.append(powerPlant)
	rooms.append(lightHouse)
	rooms.append(dock)
	rooms.append(electricShop)
	rooms.append(recreationYard)
	rooms.append(cellHouseRoof)
	rooms.append(boat)
	rooms.append(carpentryShop)
	rooms.append(wardenOffice)
	rooms.append(yard)
