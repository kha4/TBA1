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

	sink = {'Name': 'Sink', 'Description': 'It is a putrid looking sink. At least there is clean water.', 'Location': 'Prison Cell', 'Movable': 'n'}
	newGame.addObject(sink)

	airVent = {'Name': 'Air Vent', 'Description': 'You found a key.', 'ShortDesc': 'Seems like there is room for a small person to fit in the air vent.', 'Location': 'Prison Cell', 'Movable': 'n', 'HiddenItem': 'Key'}
	newGame.addObject(airVent)

	key = {'Name': 'Key', 'Description': 'Someone seems to have dropped this key. I wonder what it opens.', 'Location': 'Prison Cell', 'Movable': 'y'}
	newGame.addObject(key)

	lockingMechanism = {'Name': 'Locking Mechanism', 'Description': 'Seems like the locking mechanism has already been deactivated. Doors shoould be open in Cell Block A.', 'Location': 'Cell Block A', 'Movable': 'n'}
	newGame.addObject(lockingMechanism)

	bookShelves = {'Name': 'Book Shelves', 'Description': 'The book shelves are filled with old, dusty books. Nothing looks interesting here.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookShelves)

	desk = {'Name': 'Desk', 'Description': 'You found glue.', 'Looks like an ordinary desk. There are books scattered around. Someone was reading "Rafts for Dummies". Looks intriguing.', 'Location': 'Library', 'Movable': 'n', 'HiddenItem': 'Glue'}
	newGame.addObject(desk)

	bookCart = {'Name': 'Book Cart', 'Description': 'The wheel is broken. It has not been used in months.', 'Location': 'Library', 'Movable': 'n'}
	newGame.addObject(bookCart)

	glue = {'Name': 'Glue', 'Description': 'Seems like very durable glue. You probably should not glue your fingers together.', 'Location': 'Library', 'Movable': 'y'}
	newGame.addObject(glue)

	visitationPhone = {'Name': 'Visitation Phone', 'Description': 'You cannot hear anything. There is no one on the other side.', 'Location': 'Visiting Room', 'Movable': 'n'}
	newGame.addObject(visitationPhone)

	coatRack = {'Name': 'Coat Rack', 'Description': 'You found raincoats.', 'ShortDesc': 'The coat rack seems to be empty.', 'Location': 'Visiting Room', 'Movable': 'n', 'HiddenItem': 'Raincoats'}
	newGame.addObject(coatRack)

	raincoats = {'Name': 'Raincoats', 'These raincoats seem to be extremely reliable. No water would be able to get on you. Looks like they were probably made for visitors', 'Location': 'Visiting Room', 'Movable': 'y'}
	newGame.addObject(raincoats)

	fence = {'Name': 'Fence', 'Description': 'This barbed wire fence is keeping prisoners inside of the yard. Does not seem too high though. You can see the shore from here.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(fence)

	guardTower = {'Name': 'Guard Tower', 'Description': 'The guard tower seems to be impregnable. Looks like no one is home.', 'Location': 'Yard', 'Movable': 'n'}
	newGame.addObject(guardTower)
