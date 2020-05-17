from sys import exit

leave = "\n*You leave the room*\n"
enter = "\n*You enter the room for the first time*\n"
fight = "\nChoice(s): flee, hug, kick, slap\n"
linebreak = "\n========================================\n"

def start():
	print("\n\n\n\n\n\n\n\n\n\n")
	print("\nWelcome to my dungeon.")
	print("\nThe goal is to aquire the key and escape through the locked door.\n")
	print("Good Luck!\n")
	choice = input("Do you think you can handle it?[y/n]> ")

	global room_1_exit, room_2_exit, room_3_exit, room_4_exit, room_4_item, bleed

	room_1_exit = True
	room_2_exit = True
	room_3_exit = True
	room_4_exit = True
	room_4_item = True
	bleed = ['i give up', '...k', 'k like... there are 3 choices... how the fuck', 'you\'re fucking helpless', 'you\'re running out of blood', 'you\'re bleeding even more', 'you\'re bleeding']

	if choice == "y":
		entryway()

	elif choice == "n":
		print(linebreak,"You've already entered so you must die now.")
		print("A bright light and heat engulfs you from the inside.")
		print("As you soon as you take a breath to scream in pain everything goes black")
		death()

	else:
		print("\n\n... Try Again...")
		start()

def death():
	print(linebreak,"You're dead AF, thanks for playing")
	print("Okay, Goodbye now, Try again soon!")
	exit(0)


def entryway():
	print(linebreak)
	print("You are at the begining of this dungeon")
	print("Which way would you like to go?")
	print("\nThere are rooms to your north, south, east, and west.\n")

	choice = input("> ")

	if choice == "east" and room_1_exit:
		print(leave, linebreak)
		room1fight()

	elif choice == "east" and not room_1_exit:
		print(leave, linebreak)
		room1()

	elif choice == "north" and room_2_exit:
		print(leave, linebreak)
		room2fight()

	elif choice == "north" and not room_2_exit:
		print(leave, linebreak)
		room2()

	elif choice == "west" and room_3_exit:
		print(leave, linebreak)
		room3fight()

	elif choice == "west" and not room_3_exit:
		print(leave, linebreak)
		room3()

	elif choice == "south" and room_4_item:
		print(linebreak, "The door is locked, you stuck, find the key first pussy", linebreak)
		entryway()

	elif choice == "south" and not room_4_item:
		print(linebreak, "MY HERO!")
		print("YOU DID IT!")
		print("LIKE AND SUBSCRIBE!")
		print("Here is your trophie: (.) (.)")
		exit(0)

	else:
		print(linebreak, "There is nothing to do in this room, choose a room to enter.")
		entryway()
	
def room1fight():
	print(enter)
	print("An Angry Badger is standing in the room.")
	print("Behind the Angry Badger there is a pecuilar Shining Star.")
	print("The only way out of the room is the way you came.")
	print("What would you like to do?")
	while True:
		print("\nChoice(s): flee, hug, kick, slap, or pickup item\n")
		choice = input("> ")

		if choice == "slap":
			print(linebreak,"The Angry Badger gets sad and walks off.", linebreak)
			room1()

		elif choice == "kick":
			print(linebreak,"The Angry Badger takes the kick in stride and now looks more angry.")

		elif choice == "hug":
			print(linebreak,f"The Angry Badger takes the opportunity to gnaw your neck and now {bleed.pop()}")

		elif choice == "pickup item":
			print(linebreak,"The Angry Badger lunges at your neck as you stoop down to pickup the Item")

		elif choice == "flee":
			print(linebreak,"K bai")
			entryway()

		else:
			print(linebreak,"The Angry Badger starts moving closer towards you.", linebreak)

def room1():
	global room_1_exit

	print("You are now in an empty room except for the Shining Star.")
	print("What will you do?")
	print("\nChoice(s): pickup item or west\n")

	choice = input("> ")

	if choice == "pickup item":
		print(linebreak,"You pickup the item.... everything goes black... or grey... maybe white? Not sure... players choice.", linebreak)
		death()

	elif choice == "west":
		print(leave, linebreak)
		room_1_exit = False
		entryway()

	else:
		print(linebreak,"You dance uncontrollably, you watch 5 years pass as you do the floss.", linebreak)
		room1()

def room2fight():
	print(enter)
	print("A Tranquil Badger is doing yoga?.")
	print("As his attention is on you now, he looks much less tranquil.")
	print("Tranquil Badger evolves into his FINAL FORM: Angry Badger.")
	print("The only way out of the room is the way you came.")
	print("What would you like to do?")
	while True:
		print(fight)
		choice = input("> ")

		if choice == "slap":
			print(linebreak,"The Angry Badger gets sad and walks off.", linebreak)
			room2()

		elif choice == "kick":
			print(linebreak,"The badger takes the kick in stride and now looks more angry.")

		elif choice == "hug":
			print(linebreak, f"The badger takes the opportunity to gnaw your neck and now {bleed.pop()}")

		elif choice == "flee":
			print(linebreak, "K bai")
			entryway()

		else:
			print(linebreak,"You dance uncontrollably outside of your control wasting time as the Angry Badger approaches.", linebreak)

def room2():
	global room_2_exit

	print("You are now in an empty room.")
	print("What will you do?")
	print("There is a room to the south.")

	choice = input("> ")

	if choice == "south":
		print(leave, linebreak)
		room_2_exit = False
		entryway()

	else:
		print(linebreak,"You dance uncontrollably... Yeet", linebreak)
		room2()	

def room3fight():
	print(enter)
	print("An Undead Squirrel is crawling around the room.")
	print("The Undead Squirel focuses on you and starts moving slowly towards you.")
	print("What would you like to do?")
	while True:
		print(fight)
		choice = input("> ")

		if choice == "slap":
			print(linebreak,"The squirrel quickly dodges and you miss.")
			
		elif choice == "kick":
			print(linebreak,"That was a little overkill I think... it was just a squirrel...")
			print("Regardless... it was effective... the squirrel cowers in the corner.", linebreak)
			room3()

		elif choice == "hug":
			print(linebreak, f"As you lean down to hug the squirrel it jumps onto your back and scratches violently before jumping off {bleed.pop()}")

		elif choice == "flee":
			print(linebreak,"K bai")
			entryway()

		else:
			print(linebreak, "You decide you love Nickleback and uncontrollably dance.", linebreak)

def room3():
	global room_3_exit

	print("The squirrel is cowering in the corner.")
	print("What will you do?")
	print("There are rooms to your north, east, and west")

	choice = input("> ")

	if choice == "west" and room_4_exit and room_4_item:
		print(leave, linebreak)
		room4fight()

	elif choice == "west" and not room_4_exit and room_4_item:
		print(leave, linebreak)
		room4choice()

	elif choice == "west" and not room_4_exit and not room_4_item:
		print(linebreak,"You have already been here.")
		print("A strong unctrollable urge keeps you from entering.")
		print("Choice(s): north, east, west")
		room3done()


	elif choice == "north":
		print(leave, linebreak)
		room5()

	elif choice == "east":
		print(leave, linebreak)
		room_3_exit = False
		entryway()

	else:
		print(linebreak, "You dance uncontrollably outside of your control... Shakira appears from nowhere, soffs, and tells you to choose a fkin direction.", linebreak)
		room3()

def room3done():
	global room_3_exit

	choice = input("> ")

	if choice == "west" and not room_4_exit and not room_4_item:
		print(linebreak,"You have already been here.")
		print("A strong unctrollable urge keeps you from entering.")
		print("Choice(s): north, east, west")
		room3done()

	elif choice == "north":
		print(leave, linebreak)		
		room5()

	elif choice == "east":
		print(leave, linebreak)
		room_3_exit = False
		entryway()

	else:
		print(linebreak,"You dance uncontrollably outside of your control... Shakira appears from nowhere, soffs, and tells you to choose a fkin direction.", linebreak)
		room3done()			

def room4fight():
	print(enter)
	print("A Prickely Hedgehog looks at you in fear.")
	print("The only way out of the room is the way you came.")
	print("Behind the hedgehog is a metal hexagon sitting on a table.")
	print("What would you like to do?")

	while True:
		print("Choice(s): flee, hug, kick, slap, or pickup item")
		choice = input("> ")

		if choice == "slap":
			print(linebreak,f"Whelp... you're hand is full of spines... that was stupid {bleed.pop()}.")
			
		elif choice == "kick":
			print(linebreak,f"As you pull back your foot full of spines a tear drops from the Prickely Hedgehog's eye {bleed.pop()}.")
		
		elif choice == "hug":
			print(linebreak,"Although Your chest is full of spines and bleeding... the Prickely Hedgehog looks very satisfied and crawls to a corner to nap.", linebreak)
			room4choice()

		elif choice == "pickup item":
			print(linebreak,"The Prickely Hedgehog moves towards your hand to pet itself... out of reaction you pull your hand back.")

		elif choice == "flee":
			print(linebreak,"K bai")
			entryway()

		else:
			print(linebreak, "You look at \"this photograph\" for a good while." , linebreak)

def room4choice():
	global room_4_exit, room_4_item

	print("The Prickely Hedgehog is fast asleep in the corner.")
	print("The metal Hexagon is still sitting on the table")
	print("Upon closer inspection it looks like it might be a key.")
	print("What would you like to do?")
	print("Choice(s): pickup item, leave")
	choice = input("> ")

	if choice == "pickup item":
		print(linebreak, "You pickup the Metal Key and place it into a pouch at your side.", linebreak)
		room_4_item = False
		room_4_exit = False
		room4()

	elif choice == "leave":
		print(leave, linebreak)
		room_4_exit = False
		room3()

	else:
		print(linebreak,f"You lay down and take a snooze next to the Hedgehog... ouch... spines...{bleed.pop()}", linebreak)
		room4choice()

def room4():

	print("The Prickely Hedgehog is now snoring...")
	print("What will you do?")
	print("Choice(s): east")

	choice = input("> ")

	if choice == "east":
		print(leave, linebreak)
		room3()

	else:
		print(linebreak,f"You lay down and take a snooze next to the Hedgehog... ouch... spines...{bleed.pop()}", linebreak)
		room4()

def room5():
	print("Are you sure??? I think someone told me there was something wrong with that room...")
	print("I can't really remember why... hmm...")
	print("Choice(s): y/n")
	choice = input("> ")
	
	if choice == "y":
		print("ERROR: ROOM NOT RENDERED")		
		print("You fall off the map and die.")
		death()

	elif choice == "n":
		print(leave)
		print(linebreak,"Loading last save...", linebreak)
		room3()

	else:
		print(linebreak,"Too late for that.... better choose wisely", linebreak)
		room5()

start()

