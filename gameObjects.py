import sys
import os
import gameEngine
import gameState


def createObjectList(newGame):

	bed = {'Name': 'bed', 'Description': 'Looks like and old, bug-infested mattress.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(bed)

	poster = {'Name': 'poster', 'Description': 'You see a pleasant picture of Clint Eastwood staring back at you.', 'Location': 'Prison Cell', 'Movable': 'y'}
	newGame.addObject(poster)

	toilet = {'Name': 'toilet', 'Description': 'The stench is overpowering. It has not been cleaned in months.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(toilet)

	sink = {'Name': 'sink', 'Description': 'It is a putrid looking sink. At least the water is somewhat clear.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(sink)

	airVent = {'Name': 'air vent', 'Description': 'Seems like there is room for a small person to fit in the air vent.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(airVent)

	airVentB = {'Name': 'air vent', 'Description': 'Back into the air vent we go.', 'Location': 'Cell House Roof', 'Movable': 'n'}
	newGame.addObject(airVentB)

	drainPipes = {'Name': 'drain pipes', 'Description': 'You found a key.', 'ShortDesc': 'It seems moist and moldy. Nothing interesting here.', 'Location': 'Cell House Roof', 'Movable': 'n', 'HiddenItem': 'Key'}
	newGame.addObject(drainPipes)

	skyLights = {'Name': 'sky lights', 'Description': 'The light illuminating from the sky looks beautiful despite the gloomy looking clouds.', 'Location': 'Cell House Roof', 'Movable': 'n'}
	newGame.addObject(skyLights)

	key = {'Name': 'key', 'Description': 'Someone seems to have left this key. I wonder what it opens.', 'Location': 'Cell House Roof', 'Movable': 'y'}
	newGame.addObject(key)

	lockingMechanism = {'Name': 'locking mechanism', 'Description': 'Seems like this can open locked doors.', 'ShortDesc': 'Seems like the locking mechanism has already been deactivated. Doors are open in Cell Block A.', 'Location': 'Cell Block A', 'Movable': 'n', 'HiddenItem': 'locked'}
	newGame.addObject(lockingMechanism)

	guard = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Cell Block A', 'Movable': 'n'}
	newGame.addObject(guard)

	guardB = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Mess Hall', 'Movable': 'n'}
	newGame.addObject(guardB)

	guardC = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Sally Port', 'Movable': 'n'}
	newGame.addObject(guardC)

	guardD = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Armory', 'Movable': 'n'}
	newGame.addObject(guardD)

	guardE = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Visitation Room', 'Movable': 'n'}
	newGame.addObject(guardE)

	guardF = {'Name': 'guard', 'Description': 'The guard is onto you!', 'Location': 'Guardhouse', 'Movable': 'n'}
	newGame.addObject(guardF)

	tables = {'Name': 'tables', 'Description': 'You found gum.', 'ShortDesc': 'There is gum and signs of leftover food stained on these tables.', 'Location': 'Mess Hall', 'Movable': 'n', 'HiddenItem': 'gum'}
	newGame.addObject(tables)

	gum = {'Name': 'gum', 'Description': 'Looks like old, chewed up gum. Theres a hair on it too.', 'Location': 'Mess Hall', 'Movable': 'y'}
	newGame.addObject(gum)

	dishSink = {'Name': 'dish sink', 'Description': 'Someone needs to do the dishes.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(dishSink)

	pantry = {'Name': 'pantry', 'Description': 'Looks like the rats have made a home in here. Smells disgusting.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(pantry)

	bookShelves = {'Name': 'book shelves', 'Description': 'The book shelves are filled with old, dusty books. Nothing looks interesting here.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookShelves)

	desk = {'Name': 'desk', 'Description': 'You found glue.', 'Shortdesc': ' Looks like an ordinary desk. There are books scattered around. Someone was reading \"Rafts for Dummies\". Looks intriguing.', 'Location': 'Library', 'Movable': 'n', 'HiddenItem': 'Glue'}
	newGame.addObject(desk)

	bookCart = {'Name': 'book cart', 'Description': 'The wheel is broken. It has not been used in months.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookCart)

	glue = {'Name': 'glue', 'Description': 'Seems like very durable glue. You should probably not glue your fingers together.', 'Location': 'Library', 'Movable': 'y'}
	newGame.addObject(glue)

	doorLockControlPanel = {'Name': 'door lock control panel', 'Description': 'Looks like it opens the door to the Armory.', 'ShortDesc': 'The door lock control panel has already been used. Door to the Armory is open.', 'Location': 'Sally Port', 'Movable': 'n', 'HiddenItem': 'locked', 'KeyToOpen': 'warden key'}
	newGame.addObject(doorLockControlPanel)

	metalDetector = {'Name': 'metal detector', 'Description': 'Seems to be out of order.', 'Location': 'Sally Port', 'Movable': 'n'}
	newGame.addObject(metalDetector)

	gunRacks = {'Name': 'gun racks', 'Description': 'Looks like there are only large guns here. It would be too noticeable to sneak around with one. Better to just leave them here.', 'Location': 'Armory', 'Movable': 'n'}
	newGame.addObject(gunRacks)

	rope = {'Name': 'rope', 'Description': 'This rope seems very sturdy and reliable. This could be useful.', 'Location': 'Armory', 'Movable': 'y'}
	newGame.addObject(rope)

	visitationPhone = {'Name': 'visitation phone', 'Description': 'You cannot hear anything. There is no one on the other side.', 'Location': 'Visiting Room', 'Movable': 'n'}
	newGame.addObject(visitationPhone)

	coatRack = {'Name': 'coat rack', 'Description': 'You found raincoats.', 'ShortDesc': 'The coat rack seems to be empty.', 'Location': 'Visiting Room', 'Movable': 'n', 'HiddenItem': 'raincoats'}
	newGame.addObject(coatRack)

	raincoats = {'Name': 'raincoats', 'Description': 'These raincoats seem to be extremely reliable. No water would be able to get on you. Looks like they were probably made for visitors', 'Location': 'Visiting Room', 'Movable': 'y'}
	newGame.addObject(raincoats)

	wardenDesk = {'Name': 'warden desk', 'Description': 'Looks like a messy desk. The warden is a slob.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(wardenDesk)

	warden = {'Name': 'warden', 'Description': 'You found the warden key. Looks useful.', 'ShortDesc': 'The warden seems to be sleeping. Better not wake him up', 'Location': 'Warden Office', 'Movable': 'n', 'HiddenItem': 'warden key'}
	newGame.addObject(warden)

	wardenKey = {'Name': 'warden key', 'Description': 'Looks like an important key. Wonder what it opens.', 'Location': 'Warden Office', 'Movable': 'y'}
	newGame.addObject(wardenKey)

	bookshelf = {'Name': 'bookshelf', 'Description': 'Just an ordinary bookshelf. Nothing to see here.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(bookshelf)

	birdCage = {'Name': 'bird cage', 'Description': 'The bird inside is all skin and bones. Poor bird.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(birdCage)

	walls = {'Name': 'walls', 'Description': 'These tall brick walls keeps prisoners inside.', 'Location': 'Recreation Yard', 'Movable': 'n'}
	newGame.addObject(walls)

	horseshoePit = {'Name': 'horseshoe pit', 'Description': 'Seems like a fun way to spend time.', 'Location': 'Recreation Yard', 'Movable': 'n'}
	newGame.addObject(horseshoePit)

	fence = {'Name': 'fence', 'Description': 'This barbed wire fence is keeping prisoners inside of the yard. Does not seem too high though. You can see the shore from here.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(fence)

	guardTower = {'Name': 'guard tower', 'Description': 'The guard tower seems to be impregnable. Looks like no one is home.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(guardTower)

	spotlight = {'Name': 'Spotlight', 'Description': 'What a large light. It is probably used to spot prisoners. Does not seem to be working though.', 'Location': 'Guardhouse', 'Movable': 'n'}
	newGame.addObject(spotlight)

	dockDesk = {'Name': ' dock desk', 'Description': 'Seems like an ordinary desk. Nothing much going on here.', 'Location': 'Dock', 'Movable': 'n'}
	newGame.addObject(dockDesk)

	lockers = {'Name': 'lockers', 'Description': 'Looks like some of these lockers are being used. Maybe something useful is inside of them.', 'Location': 'Dock', 'Movable': 'n'}
	newGame.addObject(lockers)

	storageChest = {'Name': 'storage chest', 'Description': 'You found scissors.', 'ShortDesc': 'Looks empty now. Everything has been taken.', 'Location': 'Boat', 'Movable': 'n', 'HiddenItem': 'scissors'}
	newGame.addObject(storageChest)

	scissors = {'Name': 'scissors', 'Description': 'The scissors look extremely dull but still could be useful.', 'Location': 'Boat', 'Movable': 'n'}
	newGame.addObject(scissors)

	boatControls = {'Name': 'boat controls', 'Description': 'Does not seem to work. Must be malfunctioning.', 'Location': 'Boat', 'Movable': 'n'}
	newGame.addObject(boatControls)
