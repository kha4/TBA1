import sys
import os
import gameEngine
import gameState


def createObjectList(newGame):

	#create bed
	bed = {'Name': 'bed', 'Description': 'Looks like and old, bug-infested mattress.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(bed)

	#create poster
	poster = {'Name': 'poster', 'Description': 'You see a pleasant picture of Clint Eastwood staring back at you.', 'Location': 'Prison Cell', 'Movable': 'y'}
	newGame.addObject(poster)

	#create toilet
	toilet = {'Name': 'toilet', 'Description': 'The stench is overpowering. It has not been cleaned in months.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(toilet)

	#create sink
	sink = {'Name': 'sink', 'Description': 'It is a putrid looking sink. At least the water is somewhat clear.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(sink)

	#create air vent
	airVent = {'Name': 'air vent', 'Description': 'Seems like there is room for a small person to fit in the air vent.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(airVent)

	#create second air vent
	airVentB = {'Name': 'air vent', 'Description': 'Back into the air vent we go.', 'Location': 'Cell House Roof', 'Movable': 'n'}
	newGame.addObject(airVentB)

	#creat drain pipes
	drainPipes = {'Name': 'drain pipes', 'Description': 'You found a key.', 'ShortDesc': 'It seems moist and moldy. Nothing interesting here.', 'Location': 'Cell House Roof', 'Movable': 'n', 'HiddenItem': 'Key'}
	newGame.addObject(drainPipes)

	#create sky lights
	skyLights = {'Name': 'sky lights', 'Description': 'The light illuminating from the sky looks beautiful despite the gloomy looking clouds.', 'Location': 'Cell House Roof', 'Movable': 'n'}
	newGame.addObject(skyLights)

	#create key
	key = {'Name': 'key', 'Description': 'Someone seems to have left this key. I wonder what it opens.', 'Location': 'Cell House Roof', 'Movable': 'y'}
	newGame.addObject(key)

	#create locking mechanism
	lockingMechanism = {'Name': 'locking mechanism', 'Description': 'Seems like this can open locked doors.', 'ShortDesc': 'Seems like the locking mechanism has already been deactivated. Doors are open in Cell Block A.', 'Location': 'Cell Block A', 'Movable': 'n', 'HiddenItem': 'locked'}
	newGame.addObject(lockingMechanism)

	#create all guards
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

	#create tables
	tables = {'Name': 'tables', 'Description': 'You found gum.', 'ShortDesc': 'There is gum and signs of leftover food stained on these tables.', 'Location': 'Mess Hall', 'Movable': 'n', 'HiddenItem': 'gum'}
	newGame.addObject(tables)

	#create gum
	gum = {'Name': 'gum', 'Description': 'Looks like old, chewed up gum. Theres a hair on it too.', 'Location': 'Mess Hall', 'Movable': 'y'}
	newGame.addObject(gum)

	#create sink 
	dishSink = {'Name': 'sink', 'Description': 'Someone needs to do the dishes.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(dishSink)

	#create water faucet
	waterFaucet = {'Name': 'water faucet', 'Description': 'The water coming out looks clear. Seems good to drink.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(waterFaucet)

	#create pantry
	pantry = {'Name': 'pantry', 'Description': 'Looks like the rats have made a home in here. Smells disgusting.', 'Location': 'Kitchen', 'Movable': 'n'}
	newGame.addObject(pantry)

	#create bookshelves
	bookShelves = {'Name': 'book shelves', 'Description': 'The book shelves are filled with old, dusty books. Nothing looks interesting here.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookShelves)

	#create desk
	desk = {'Name': 'desk', 'Description': 'You found glue.', 'ShortDesc': ' Looks like an ordinary desk. There are books scattered around. Someone was reading \"Rafts for Dummies\". Looks intriguing.', 'Location': 'Library', 'Movable': 'n', 'HiddenItem': 'Glue'}
	newGame.addObject(desk)

	#create book cart
	bookCart = {'Name': 'book cart', 'Description': 'The wheel is broken. It has not been used in months.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookCart)

	#create glue
	glue = {'Name': 'glue', 'Description': 'Seems like very durable glue. You should probably not glue your fingers together.', 'Location': 'Library', 'Movable': 'y'}
	newGame.addObject(glue)

	#create door lock control panel
	doorLockControlPanel = {'Name': 'door lock control panel', 'Description': 'Looks like it opens the door to the Armory.', 'ShortDesc': 'The door lock control panel has already been used. Door to the Armory is open.', 'Location': 'Sally Port', 'Movable': 'n', 'HiddenItem': 'locked', 'KeyToOpen': 'warden key'}
	newGame.addObject(doorLockControlPanel)

	#create metal detector
	metalDetector = {'Name': 'metal detector', 'Description': 'Seems to be out of order.', 'Location': 'Sally Port', 'Movable': 'n'}
	newGame.addObject(metalDetector)

	#create gun racks
	gunRacks = {'Name': 'gun racks', 'Description': 'Looks like there are only large guns here. It would be too noticeable to sneak around with one. Better to just leave them here.', 'Location': 'Armory', 'Movable': 'n'}
	newGame.addObject(gunRacks)

	#create rope
	rope = {'Name': 'rope', 'Description': 'This rope seems very sturdy and reliable. This could be useful.', 'Location': 'Armory', 'Movable': 'y'}
	newGame.addObject(rope)

	#create phone
	visitationPhone = {'Name': 'visitation phone', 'Description': 'You cannot hear anything. There is no one on the other side.', 'Location': 'Visiting Room', 'Movable': 'n'}
	newGame.addObject(visitationPhone)

	#create coat rack
	coatRack = {'Name': 'coat rack', 'Description': 'You found raincoats.', 'ShortDesc': 'The coat rack seems to be empty.', 'Location': 'Visiting Room', 'Movable': 'n', 'HiddenItem': 'raincoats'}
	newGame.addObject(coatRack)

	#create raincoats
	raincoats = {'Name': 'raincoats', 'Description': 'These raincoats seem to be extremely reliable. No water would be able to get on you. Looks like they were probably made for visitors', 'Location': 'Visiting Room', 'Movable': 'y'}
	newGame.addObject(raincoats)

	#create desk
	wardenDesk = {'Name': 'warden desk', 'Description': 'Looks like a messy desk. The warden is a slob.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(wardenDesk)

	#create warden
	warden = {'Name': 'warden', 'Description': 'You found the warden key. Looks useful.', 'ShortDesc': 'The warden seems to be sleeping. Better not wake him up', 'Location': 'Warden Office', 'Movable': 'n', 'HiddenItem': 'warden key'}
	newGame.addObject(warden)

	#create warden key
	wardenKey = {'Name': 'warden key', 'Description': 'Looks like an important key. Wonder what it opens.', 'Location': 'Warden Office', 'Movable': 'y'}
	newGame.addObject(wardenKey)

	#create bookshelf
	bookshelf = {'Name': 'bookshelf', 'Description': 'Just an ordinary bookshelf. Nothing to see here.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(bookshelf)

	#create bird cage
	birdCage = {'Name': 'bird cage', 'Description': 'The bird inside is all skin and bones. Poor bird.', 'Location': 'Warden Office', 'Movable': 'n'}
	newGame.addObject(birdCage)

	#create walls
	walls = {'Name': 'walls', 'Description': 'These tall brick walls keeps prisoners inside.', 'Location': 'Recreation Yard', 'Movable': 'n'}
	newGame.addObject(walls)

	#create horseshoe pit
	horseshoePit = {'Name': 'horseshoe pit', 'Description': 'You found a horseshoe.', 'ShortDesc': 'Seems like a fun way to spend time.', 'Location': 'Recreation Yard', 'Movable': 'n', 'HiddenItem': 'horseshoe'}
	newGame.addObject(horseshoePit)

	#create horseshoe
	horseshoe = {'Name': 'horseshoe', 'Description': 'Great to play with. Does not seem entirely useful though.', 'Location': 'Recreation Yard', 'Movable': 'y'}
	newGame.addObject(horseshoe)

	#create fence
	fence = {'Name': 'fence', 'Description': 'This barbed wire fence is keeping prisoners inside of the yard. Does not seem too high though. You can see the shore from here.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(fence)

	#create guard tower
	guardTower = {'Name': 'guard tower', 'Description': 'The guard tower seems to be impregnable. Looks like no one is home.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(guardTower)

	#create spotlight
	spotlight = {'Name': 'spotlight', 'Description': 'What a large light. It is probably used to spot prisoners. Does not seem to be working though.', 'Location': 'Guardhouse', 'Movable': 'n'}
	newGame.addObject(spotlight)

	#create desk
	dockDesk = {'Name': ' dock desk', 'Description': 'Seems like an ordinary desk. Nothing much going on here.', 'Location': 'Dock', 'Movable': 'n'}
	newGame.addObject(dockDesk)

	#create lockers
	lockers = {'Name': 'lockers', 'Description': 'Looks like some of these lockers are being used. Maybe something useful is inside of them.', 'Location': 'Dock', 'Movable': 'n'}
	newGame.addObject(lockers)

	#create storage chest
	storageChest = {'Name': 'storage chest', 'Description': 'You found scissors.', 'ShortDesc': 'Looks empty now. Everything has been taken.', 'Location': 'Boat', 'Movable': 'n', 'HiddenItem': 'scissors'}
	newGame.addObject(storageChest)

	#create scissors
	scissors = {'Name': 'scissors', 'Description': 'The scissors look extremely dull but still could be useful.', 'Location': 'Boat', 'Movable': 'n'}
	newGame.addObject(scissors)

	#create boat controls
	boatControls = {'Name': 'boat controls', 'Description': 'Does not seem to work. Must be malfunctioning.', 'Location': 'Boat', 'Movable': 'n'}
	newGame.addObject(boatControls)
