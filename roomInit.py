import sys
import os
import roomClass

def initiateRooms():
	#creating Sally Port
	sallyPort = Room(0, 0)
	sallyPort.add_feature("Guard")
	sallyPort.add_feature("Control Panel")
	sallyPort.add_feature("Metal Detector")
	sallyPort.set_shortDescr("You're back at the Sally Port. Features: " + sallyPort.print_featureList() 
				+ " Items: " + sallyPort.print_itemList())
	sallyPort.set_longDescr("You've discovered the Sally Port! ...")

	#Creating Armory
	armory = Room(0, 0)
	armory.add_feature("Guard")
	armory.add_feature("Gun Racks")
	armory.set_shortDescr("You're back at the Armory. Features: " + armory.print_featureList()
                                + " Items: " + armory.print_itemList())
        armory.set_longDescr("You've discovered the Armory! ...")

	#Creating Prison Cell
	prisonCell = Room(0, 1) #player starts out here
	prisonCell.add_feature("Bed")
	prisonCell.add_feature("Poster")
	prisonCell.add_feature("Toilet")
	prisonCell.add_feature("Sink")
	prisonCell.add_feature("Air Vent")
	prisonCell.add_feature("Bible")
	prisonCell.set_shortDescr("You're back at the Prison Cell. Features: " + prisonCell.print_featureList() 
				+ " Items: " + prisonCell.print_itemList())
        prisonCell.set_longDescr("You've arrived at your Prison Cell! ...")

	#Creating Visiting Room
	visitingRoom = Room(0, 0)
	visitingRoom.add_feature("Visitation Phone")
	visitingRoom.add_feature("Guard")
	visitingRoom.set_shortDescr("You're back at the Visiting Room. Features: " + 
				visitingRoom.print_featureList() + " Items: " + visitingRoom.print_itemList())
        visitingRoom.set_longDescr("You've discovered the Visiting Room! ...")

	#Library
	library = Room(0, 0)
	library.add_feature("Book Shelves")
	library.add_feature("Desk")
	library.add_feature("Book Cart")
	library.set_shortDescr("You're back at the Library. Features: " + library.print_featureList()
                                + " Items: " + library.print_itemList())
        library.set_longDescr("You've discovered the Library! ...")

	#Creating Cell Block A
	cellA = Room(0, 0)
	cellA.add_feature("Guard")
	cellA.add_feature("Locking Mechanism")
	cellA.set_shortDescr("You're back at Cell Block A. Features: " + cellA.print_featureList()
                                + " Items: " + cellA.print_itemList())
        cellA.set_longDescr("You've discovered Cell Block A! ...")

	#Creating Crawl Space
	crawlSpace = Room(0, 0)
	crawlSpace.add_feature("Pipes")
	crawlSpace.add_feature("Ventilation Shaft")
	crawlSpace.set_shortDescr("You're back inside the Crawl Space. Features: " + crawlSpace.print_featureList()
                                + " Items: " + crawlSpace.print_itemList())
        crawlSpace.set_longDescr("You've entered the Crawl Space! ...")

	#Creating Mess Hall
	messHall = Room(0, 0)
	messHall.add_feature("Table")
	messHall.add_feature("Guard")
	messHall.set_shortDescr("You're back at the Sally Port. Features: " + messHall.print_featureList()
                                + " Items: " + messHall.print_itemList())
        messHall.set_longDescr("You've discovered the Mess Hall! ...")

	#Creating Kitchen
	kitchen = Room(0, 0)
	kitchen.add_feature("Sink")
	kitchen.add_feature("Pantry")
	kitchen.set_shortDescr("You're back at the Kitchen. Features: " + kitchen.print_featureList()
                                + " Items: " + kitchen.print_itemList())
        kitchen.set_longDescr("You've discovered the Kitchen! ...")

	#Creating Guardhouse
	guardhouse = Room(0, 0)
	guardhouse.add_feature("Spotlight")
	guardhouse.add_feature("Guard")
	guardhouse.set_shortDescr("You're back at the Guardhouse. Features: " + guardhouse.print_featureList()
                                + " Items: " + guardhouse.print_itemList())
        guardhouse.set_longDescr("You've discovered the Guardhouse! ...")

	#Creating Powerplant
	powerplant = Room(0, 0)
        powerplant.add_feature("Desk")
        powerplant.add_feature("Cabinet")
        powerplant.set_shortDescr("You're back at the Powerplant. Features: " + powerplant.print_featureList()
                                + " Items: " + powerplant.print_itemList())
        powerplant.set_longDescr("You've discovered the Powerplant! ...")

	#Creating Lighthouse
	lighthouse = Room(0, 0)
	lighthouse.add_feature("Coat Rack")
	lighthouse.add_feature("Table")
	lighthouse.set_shortDescr("You're back at the Lighthouse. Features: " + lighthouse.print_featureList()
                                + " Items: " + lighthouse.print_itemList())
        lighthouse.set_longDescr("You've discovered the Lighthouse! ...")

	#Creating Dock
	dock = Room(0, 0)
	dock.add_feature("Desk")
	dock.add_feature("Lockers")
	dock.set_shortDescr("You're back at the Dock. Features: " + dock.print_featureList()
                                + " Items: " + dock.print_itemList())
        dock.set_longDescr("You've discovered the Dock! ...")

	#Creating Electric Shop
	electricShop = Room(0, 0)
	electricShop.add_feature("Closet")
	electricShop.add_feature("Work Bench")
	electricShop.set_shortDescr("You're back at the Electric Shop. Features: " + 
				electricShop.print_featureList() + " Items: " + electricShop.print_itemList())
        electricShop.set_longDescr("You've discovered the Electric Shop! ...")

	#Creating Recreation Yard
	recreationYard = Room(0, 0)
	recreationYard.add_feature("Walls")
	recreationYard.add_feature("Horseshoe Pit")
	recreationYard.set_shortDescr("You're back at the Recreation Yard. Features: " + 
				recreationYard.print_featureList() + " Items: " + recreationYard.print_itemList())
        recreationYard.set_longDescr("You've discovered the Recreation Yard! ...")

	#Creating Cell House Roof
	cellHouseRoof = Room(0, 0)
	cellHouseRoof.add_feature("Sky Lights")
	cellHouseRoof.add_feature("Drain Pipes")
	cellHouseRoof.set_shortDescr("You're back at the Cell House Roof. Features: " + 
				cellHouseRoof.print_featureList() + " Items: " + cellHouseRoof.print_itemList())
        cellHouseRoof.set_longDescr("You've discovered the Cell House Roof! ...")

	#Creating Boat
	boat = Room(0, 0)
	boad.add_feature("Storage Chest")
	boat.add_feature("Boat Controls")
	boat.set_shortDescr("You're back at the Boat. Features: " + boat.print_featureList()
                                + " Items: " + boat.print_itemList())
        boat.set_longDescr("You've discovered a Boat! ...")

	#Creating Carpentry Shop
	carpentryShop = Room(0, 0)
	carpentryShop.add_feature("Table Saw")
	carpentryShop.add_feature("Work Bench")
	carpentryShop.set_shortDescr("You're back at the Carpentry Shop. Features: " + 
				carpentryShop.print_featureList() + " Items: " + carpentryShop.print_itemList())
        carpentryShop.set_longDescr("You've discovered the Carpentry Shop! ...")

	#Creating Warden's Office
	wardenOffice = Room(0, 0)
	wardenOffice.add_feature("Bookshelf")
	wardenOffice.add_feature("Desk")
	wardenOffice.add_feature("Warden")
	wardenOffice.add_feature("Bird Cage")
	wardenOffice.set_shortDescr("You're back at the Warden's Office. Features: " + 
				wardenOffice.print_featureList() + " Items: " + wardenOffice.print_itemList())
        wardenOffice.set_longDescr("You've discovered the Warden's Office! ...")

	#Creating Yard
	yard = Room(0, 0)
	yard.add_feature("Fence")
	yard.add_feature("Guard Tower")
	yard.set_shortDescr("You're back at the Yard. Features: " + yard.print_featureList()
                                + " Items: " + yard.print_itemList())
        yard.set_longDescr("You've discovered the Yard! ...")



def printRoomDescription(r):
	if r.get_status == 0:
		print(r.get_longDescr())
	else:
		print(r.get_shortDescr())


def loadRoomStates:
	#parse save file and make necessary changes to rooms


def saveRoomState:
	#save room information into a save file
