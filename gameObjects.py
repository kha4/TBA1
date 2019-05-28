import sys
import os
import gameEngine
import gameState


def createObjectList(newGame):

	bed = {'Name': 'Bed', 'Description': 'Looks like and old, bug-infested mattress.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(bed)

	poster = {'Name': 'Poster', 'Description': 'You see a pleasant picture of Clint Eastwood staring back at you.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(poster)

	toilet = {'Name': 'Toilet', 'Description': 'The stench is overpowering. It has not been cleaned in months.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(toilet)

	sink = {'Name': 'Sink', 'Description': 'It is a putrid looking sink. At least the water is somewhat clear.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(sink)

	airVent = {'Name': 'Air Vent', 'Description': 'Seems like there is room for a small person to fit in the air vent.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(airVent)

	drainPipes = {'Name': 'Drain Pipes', 'Description': 'You found a key.', 'ShortDesc': 'It seems moist and moldy. Nothing interesting here.', 'Location': 'Cell House Roof', 'Movable': 'n', 'HiddenItem': 'Key'}
	newGame.addObject(drainPipes)

	skyLights = {'Name': 'Sky Lights', 'Description': 'The light illuminating from the sky looks beautiful despite the gloomy looking clouds.', 'Location': 'Cell House Roof', 'Movable': 'n'}
	newGame.addObject(skyLights)

	key = {'Name': 'Key', 'Description': 'Someone seems to have left this key. I wonder what it opens.', 'Location': 'Cell House Roof', 'Movable': 'y'}
	newGame.addObject(key)

	lockingMechanism = {'Name': 'Locking Mechanism', 'Description': 'Seems like this can open locked doors.', 'ShortDesc': 'Seems like the locking mechanism has already been deactivated. Doors are open in Cell Block A.', 'Location': 'Cell Block A', 'Movable': 'n'}
	newGame.addObject(lockingMechanism)

	guard = {'Name': 'Guard', 'Description': 'The guard is onto you!', 'Location': 'Cell Block A', 'Movable': 'n'}
	newGame.addObject(guard)

	tables = {'Name': 'Tables', 'Description': 'There is gum and signs of leftover food stained on these tables.', 'Location': 'Mess Hall', 'Movable': 'n'}
	newGame.addObject(tables)

	dishSink = {'Name': 'Dish Sink', 'Description': 'Someone needs to do the dishes.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(dishSink)

	pantry = {'Name': 'Pantry', 'Description': 'Looks like the rats have made a home in here. Smells disgusting.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(pantry)

	bookShelves = {'Name': 'Book Shelves', 'Description': 'The book shelves are filled with old, dusty books. Nothing looks interesting here.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookShelves)

	desk = {'Name': 'Desk', 'Description': 'You found glue.', 'Shortdesc': ' Looks like an ordinary desk. There are books scattered around. Someone was reading \"Rafts for Dummies\". Looks intriguing.', 'Location': 'Library', 'Movable': 'n', 'HiddenItem': 'Glue'}
	newGame.addObject(desk)

	bookCart = {'Name': 'Book Cart', 'Description': 'The wheel is broken. It has not been used in months.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookCart)

	glue = {'Name': 'Glue', 'Description': 'Seems like very durable glue. You should probably not glue your fingers together.', 'Location': 'Library', 'Movable': 'y'}
	newGame.addObject(glue)

	doorLockControlPanel = {'Name': 'Door Lock Control Panel', 'Description': 'Looks like it opens the door to the Armory.', 'Location': 'Sally Port', 'Movable': 'n'}
	newGame.addObject(doorLockControlPanel)

	metalDetector = {'Name': 'Metal Detector', 'Description': 'Seems to be out of order.', 'Location': 'Sally Port', 'Movable': 'n'}
	newGame.addObject(metalDetector)

	gunRacks = {'Name': 'Gun Racks', 'Description': 'Looks like there are only large guns here. It would be too conspicuous to sneak around with one. Better to just leave them here.', 'Location': 'Armory', 'Movable': 'n'}
	newGame.addObject(gunRacks)

	visitationPhone = {'Name': 'Visitation Phone', 'Description': 'You cannot hear anything. There is no one on the other side.', 'Location': 'Visiting Room', 'Movable': 'n'}
	newGame.addObject(visitationPhone)

	coatRack = {'Name': 'Coat Rack', 'Description': 'You found raincoats.', 'ShortDesc': 'The coat rack seems to be empty.', 'Location': 'Visiting Room', 'Movable': 'n', 'HiddenItem': 'Raincoats'}
	newGame.addObject(coatRack)

	raincoats = {'Name': 'Raincoats', 'Description': 'These raincoats seem to be extremely reliable. No water would be able to get on you. Looks like they were probably made for visitors', 'Location': 'Visiting Room', 'Movable': 'y'}
	newGame.addObject(raincoats)



	fence = {'Name': 'Fence', 'Description': 'This barbed wire fence is keeping prisoners inside of the yard. Does not seem too high though. You can see the shore from here.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(fence)

	guardTower = {'Name': 'Guard Tower', 'Description': 'The guard tower seems to be impregnable. Looks like no one is home.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(guardTower)
