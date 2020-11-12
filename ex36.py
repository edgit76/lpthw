from sys import exit

def house():
	print "\nYou've been walking for miles on this arid plane of sand a a few dry bushes." 
	print "You see at the distance a column of green and light reflecting from on the middle of it." 
	print "You walk towards it for another 40 minutes under the Sun." 
	print "You finally reach the place and there is a small house",
	print " surounded by a circle of tall palm trees."
	print "You knock on the door and nobody answers."
	print "It seems that there is no one home. Door is not locked though."
	front_door()
	
def front_door():
	print "\nYou are at the front door."
	around = False
	
	while True:
		front_door = raw_input("> ")
		
		if front_door == "enter" or front_door == "open door" or front_door == "enter the house" or front_door == "enter house":
			print "\nThe door makes a creeking noise as it opens." 
			kitchen()
		elif front_door == "leave" or front_door == "go away":
			dead()
		elif (front_door == "go around" or front_door == "check the windows") and not around:
			print "'nYou check around the house. All the windows are close shut and there is ", 
			print "other way in. You go back to the front door."
			around = True
		elif (front_door == "go around" or front_door == "check the windows") and around:
			print "\nYou were already dehidrated and weak."
			dead()
		elif front_door == "where":
			print "You are at the front door."
		elif front_door == "look":
			front_door()
		else:
			print "That does not work."
			
def kitchen():
	print "\nYou are in the kitchen and there is dust everywhere."
	print "It seems that there haven't been anyone in for a while."
	print "To the north there is a corridor." 
	print "To the left there is shopping bag on the table."
	print "To the right on the wall there is a calendar."
	
	while True:
		next = raw_input("> ")
			
		if next == "go north" or next == "go to the corridor" or next == "enter corridor":
			print "\nWith your eyes fixed, you walk towards the corridor."
			corridor()
		elif next == "leave" or next == "leave house" or next == "get out" or next == "leave the house" or next == "go back" or next == "go south":
			front_door()
		elif next == "go to the table" or next == "table" or next == "left" or next == "go left":
			table()
		elif next == "go right" or next == "right" or left == "calendar":
			from datetime import date
			print "\t\t\t\t\tYou look at the calendar and it shows today's date:"
			print "\t\t\t\t\t", date.today()
			kitchen()
		elif next == "where":
			print "You are in the kitchen"
		elif next == "look":
			kitchen()
		else:
			print "That does not work"
				
def corridor():
	"""Function to test if, elif and else elements"""
	print "You are at the north door of the kitchen facing a dark corridor "
	print "with a door to the left, stairs going up to the right and you "
	print "can barely see lights shinning around the curtains in what seems "
	print "to be the living room right in front of the room."
	
	while True:
		next = raw_input("> ")
	
		if next == "left" or next == "go left" or next == "enter toilet" or next == "go to the toilet":
			print "\nThis is the toilet door and it has a beautiful large shell hanging from it."
			print "You slowly open the door and enter."
			bathroom()
		elif next == "go east" or next == "go up" or next == "go upstairs" or next == "go right" or next == "right" or next == "go up the stairs":
			print "You start to go up the squicky staircase. At every step it makes noise and"
			print " even though there is no one around you have the impression someone would hear it."
			print "You reach the top and can see an empty loft space."
			loft()
		elif next == "go north" or next == "enter living room" or next == "go ahead" or next == "go straight":
			living_room1() 
		elif next == "go back" or next == "return to the kitchen" or next == "go south" or next =="south":
			kitchen()
		elif next == "where":
			print "You are in the corridor"
		elif next == "look":
			corridor()
		else:
			print "That does not work."	

def bathroom():
	print "It's a small bathroom with pink bath, sink and toilet bow."
	print "A blue towel still hanging behind the door."
	pee = False
	
	while True:
		next = raw_input("> ")
		
		if (next == "pee" or next == "poop") and not pee:
			print "You relieve yourself after being not able to do it in the vastness of the empty desert."
			pee = True
		elif (next == "pee" or next == "poop") and pee:
			print "You have nothing left in your body anymore! Go wash your hands."
		elif next == "wash hands" or next == "wash hand" or next == "clean hands":
			print "You wash your hands and dry them on the towel."
		elif next == "leave" or next == "leave the bathroom" or next == "go to corridor":
			corridor()
		elif next == "Where":
			print "You are in the bathroom."
		else:
			print "It does not work"

def loft():
	print "The loft and large and empty."
	print "You can see two skylights. The one on the north side is open."
	
	while True:
		next = raw_input("> ")
	
		if next == "go north" or next == "go to skylight" or next == "close skylight":
			print "A trap door opens under your feet when you reach the skylight."
			print "You fall on the sofa and got up your feet again."
			living_room1()
		elif next == "go down" or next == "go downstairs" or next == "back downstairs" or next == "go east":
			print "You go back down the squicking steps."
			corridor()
		elif next == "where":
			print "You are in the loft."
		elif next == "look":
			loft()
		else:
			print "That does not work."

def sofa():
	print "You shake your head and got back on your feet."
	living_room1()

def living_room1():
	print "You are in the living room."
	print "There is nothing here but the sofa and a notebook."
	open = False
	
	while True:
		next = raw_input("> ")
	
		if next == "go south" or next == "go to the corridor" or next == "leave":
			corridor()
		elif next == "kitchen" or next == "go to the kitchen":
			print "You pass the corridor and go straight back to the kitchen."
			kitchen()
			
		elif (next == "open the curtains" or next == "open curtains") and not open:
			print "You open the dusty curtains."
			open = True
		elif (next == "open the curtains" or next == "open curtains") and open:
			print "They are already open!"
			
		elif (next == "close the curtains" or next == "close curtains") and open:
			print "You close the curtains"
			open = False
		elif (next == "close the curtains" or next == "close curtains") and not open:
			print "They are already closed!"
			
		elif next == "sit on the sofa" or next == "sit":
			print "You sit down and notice words on the wall."
			print "They ask you to think about 5 numbers between 1 and 10." 
			numbers = []
			for i in range(5):
				numbers.append(int(raw_input("Enter number: ")))
				
			print "The numbers you entered are: ", numbers
			
			for i in numbers:
				print "Is", i, ">", 5, "?", i>5
				print "Ok, you had a bit of fun and return to the center ot the room."
			
			living_room1()
		elif next == "notebook":
			notebook()
		elif next == "where":
			print "You are in the living room."
		else:
			print "That does not work."

def notebook():
	print "You can write on a notebook and make notes about your stay in the house."
	print "Input 1 to leave now."
	print "Input 2 to read what is in the notebook so far, or"
	print "Input \"west\" to write a note at the end of the file:",

	while True:
		file = raw_input("> ")
	
		if file == "west" or file == "West":
			x = file +".txt"
			file1 = open(x, "a+") # ok, this working. A file is being created.
			file1.write("\n")
			file1.write(raw_input("Put something on the first line: "))
			file1.write(raw_input("Write something on the second line: "))
			file1.close()
			print "#" * 80
			a = open(x, "r")
			print a.read()
			a.close()
			print "#" * 80
			living_room1()
		elif file == "1":
			print "You walk back to where you were..."
			living_room1()
		elif file == "2":
			a = open("west.txt", "r")
			print a.read()
			notebook()
		else:
			print "That's not the name!"

def table():
	print "There is a rag bag on the table with some glowing beans, gold",
	print "coins and a bottle with a clear drinking liquid. You can:\n\t1. look at ",
	print "the beans \n\t2. Check the coins \n\t3. Drink the liquid \n\t4. Leave."""
	next = raw_input("> ")
	beans = []
	coins = []
	
	if next == "1":
		print "You are going to name the beans:"
		beans.append(raw_input("Enter 1st name: "))
		beans.append(raw_input("Enter 2nd name: "))
		beans.append(raw_input("Enter 3rd name: "))
		print "And here are the beans' names and their indexes:"
		
		for i in range(len(beans)):
			print i, beans[i]
		print raw_input("There is nothing else to this beans.")
		table()
	elif next == "2":
		print "Here you have 5 coins with different values."
		print " Input their values:"
		coins.append(float(raw_input("Enter 1st value: ")))
		coins.append(float(raw_input("Enter 2nd value: ")))
		coins.append(float(raw_input("Enter 3rd value: ")))
		coins.append(float(raw_input("Enter 5th value: ")))
		coins.append(float(raw_input("Enter 6th value: ")))
		print "The the sorted table of the values you entered and their respective indexes are:"
		
		for i in range(len(coins)):
			coins.sort()
			print i, coins[i]
			
		print raw_input("There is nothing else to this coins.")
		table()
	elif next == "3":
		print "You drunk the liquid that tastes like peach juice and pass out..."
		print "You open your eyes but everything is dark..."
		living_room()
	elif next == "4":
		kitchen()
	elif next == "where":
		print "You are at the table."
		table()
	else:
		print "That does not work"
		
def dead():
	print "\nYou step from the porch into the vast dry plane. You succumb to the heat and perish!"
	exit(0)
	
house()

