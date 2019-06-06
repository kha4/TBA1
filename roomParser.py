import sys
import os
import gameState
import gameEngine

def parseNewRoomData(newGame):

	#read prisonCell text file and create dictionary for it
	prisonCell = {}
	#open the text file for reading
	with open ('prisonCell.txt', 'rt') as pcFile:
		#read the first line
		line = pcFile.readline()
		#keep count of lines
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				prisonCell['Name'] = testStr
			elif cnt == 2:
				prisonCell['LongDesc'] = testStr
			elif cnt == 3:
				prisonCell['ShortDesc'] = testStr
			else:
				prisonCell['Status'] = testStr
			cnt += 1
			line = pcFile.readline()
	#add the dictionary to room list
	newGame.createRoom(prisonCell)

	#same as above but for sallyPort
	sallyPort = {}
	with open ('sallyPort.txt', 'rt') as spFile:
		line = spFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				sallyPort['Name'] = testStr
			elif cnt == 2:
				sallyPort['LongDesc'] = testStr
			elif cnt == 3:
				sallyPort['ShortDesc'] = testStr
			else:
				sallyPort['Status'] = testStr
			cnt += 1
			line = spFile.readline()
	newGame.createRoom(sallyPort)

	#same as above but for armory
	armory = {}
	with open('armory.txt', 'rt') as aFile:
		line = aFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				armory['Name'] = testStr
			elif cnt == 2:
				armory['LongDesc'] = testStr
			elif cnt == 3:
				armory['ShortDesc'] = testStr
			else:
				armory['Status'] = testStr
			cnt += 1
			line = aFile.readline()
	newGame.createRoom(armory)

	 #same as above but for visitingRoom
	visitingRoom = {}
	with open('visitingRoom.txt', 'rt') as vrFile:
		line = vrFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				visitingRoom['Name'] = testStr
			elif cnt == 2:
				visitingRoom['LongDesc'] = testStr
			elif cnt == 3:
				visitingRoom['ShortDesc'] = testStr
			else:
				visitingRoom['Status'] = testStr
			cnt += 1
			line = vrFile.readline()
	newGame.createRoom(visitingRoom)

	#same as above but for library
	library = {}
	with open('library.txt', 'rt') as lFile:
		line = lFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				library['Name'] = testStr
			elif cnt == 2:
				library['LongDesc'] = testStr
			elif cnt == 3:
				library['ShortDesc'] = testStr
			else:
				library['Status'] = testStr
			cnt += 1
			line = lFile.readline()
	newGame.createRoom(library)

	#same as above but for cellBlockA
	cellBlockA = {}
	with open ('cellBlockA.txt', 'rt') as cbaFile:
		line = cbaFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				cellBlockA['Name'] = testStr
			elif cnt == 2:
				cellBlockA['LongDesc'] = testStr
			elif cnt == 3:
				cellBlockA['ShortDesc'] = testStr
			else:
				cellBlockA['Status'] = testStr
			cnt += 1
			line = cbaFile.readline()
	newGame.createRoom(cellBlockA)

	#same as above but for messHall
	messHall = {}
	with open ('messHall.txt', 'rt') as mhFile:
		line = mhFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				messHall['Name'] = testStr
			elif cnt == 2:
				messHall['LongDesc'] = testStr
			elif cnt == 3:
				messHall['ShortDesc'] = testStr
			else:
				messHall['Status'] = testStr
			cnt += 1
			line = mhFile.readline()
	newGame.createRoom(messHall)

	#same as above but for kitchen
	kitchen = {}
	with open ('kitchen.txt', 'rt') as kFile:
		line = kFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				kitchen['Name'] = testStr
			elif cnt == 2:
				kitchen['LongDesc'] = testStr
			elif cnt == 3:
				kitchen['ShortDesc'] = testStr
			else:
				kitchen['Status'] = testStr
			cnt += 1
			line = kFile.readline()
	newGame.createRoom(kitchen)

	#same as above but for guardhouse
	guardhouse = {}
	with open ('guardhouse.txt', 'rt') as ghFile:
		line = ghFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				guardhouse['Name'] = testStr
			elif cnt == 2:
				guardhouse['LongDesc'] = testStr
			elif cnt == 3:
				guardhouse['ShortDesc'] = testStr
			else:
				guardhouse['Status'] = testStr
			cnt += 1
			line = ghFile.readline()
	newGame.createRoom(guardhouse)

	#same as above but for dock
	dock = {}
	with open ('dock.txt', 'rt') as dFile:
		line = dFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				dock['Name'] = testStr
			elif cnt == 2:
				dock['LongDesc'] = testStr
			elif cnt == 3:
				dock['ShortDesc'] = testStr
			else:
				dock['Status'] = testStr
			cnt += 1
			line = dFile.readline()
	newGame.createRoom(dock)

	#same as above but for recreation Yard
	recreationYard = {}
	with open ('recreationYard.txt', 'rt') as ryFile:
		line = ryFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				recreationYard['Name'] = testStr
			elif cnt == 2:
				recreationYard['LongDesc'] = testStr
			elif cnt == 3:
				recreationYard['ShortDesc'] = testStr
			else:
				recreationYard['Status'] = testStr
			cnt += 1
			line = ryFile.readline()
	newGame.createRoom(recreationYard)

	#same as above but for cellHouseRoof
	cellHouseRoof = {}
	with open ('cellHouseRoof.txt', 'rt') as chrFile:
		line = chrFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				cellHouseRoof['Name'] = testStr
			elif cnt == 2:
				cellHouseRoof['LongDesc'] = testStr
			elif cnt == 3:
				cellHouseRoof['ShortDesc'] = testStr
			else:
				cellHouseRoof['Status'] = testStr
			cnt += 1
			line = chrFile.readline()
	newGame.createRoom(cellHouseRoof)

	#same as above but for boat
	boat = {}
	with open ('boat.txt', 'rt') as bFile:
		line = bFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				boat['Name'] = testStr
			elif cnt == 2:
				boat['LongDesc'] = testStr
			elif cnt == 3:
				boat['ShortDesc'] = testStr
			else:
				boat['Status'] = testStr
			cnt += 1
			line = bFile.readline()
	newGame.createRoom(boat)

	#same as above but for wardenOffice
	wardenOffice = {}
	with open ('wardenOffice.txt', 'rt') as woFile:
		line = woFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				wardenOffice['Name'] = testStr
			elif cnt == 2:
				wardenOffice['LongDesc'] = testStr
			elif cnt == 3:
				wardenOffice['ShortDesc'] = testStr
			else:
				wardenOffice['Status'] = testStr
			cnt += 1
			line = woFile.readline()
	newGame.createRoom(wardenOffice)

	#same as above but for yard
	yard = {}
	with open ('yard.txt', 'rt') as yardFile:
		line = yardFile.readline()
		cnt = 1
		while line:
			testStr = line.rstrip()
			if cnt == 1:
				yard['Name'] = testStr
			elif cnt == 2:
				yard['LongDesc'] = testStr
			elif cnt == 3:
				yard['ShortDesc'] = testStr
			else:
				yard['Status'] = testStr
			cnt += 1
			line = yardFile.readline()
	newGame.createRoom(yard)
