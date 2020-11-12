# answer designed by catherineives

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale' , 'platypus']

print """\nFirst a brief explanation of cardinal and ordinal numbers:
the ordinal number is the position of the element in a list, eg. first, second, 
third, etc. 
The cardinal number begins at 0 and is an unordered number, eg. zero, one, two, three
"""

print """\nNow I'm going to ask you a series of questions relating to this list:
 %s.""" % animals

print "What is the animal at 1?"
one = raw_input("> ")
print "What is the third animal?"
third = raw_input("> ")
print "What is the first animal?"
first = raw_input("> ")
print "What is the animal at 3?"
three = raw_input("> ")
print "What is the fifth animal?"
fifth = raw_input("> ")
print "What is the animal at 2?"
two = raw_input("> ")
print "What is the sixth animal?"
sixth = raw_input("> ")
print "What is the animal at 4?"
four = raw_input("> ")

print "\nNow let's see how you did!"

print "Question one: you answered %s" % one
if one == animals[1]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[1]
print "Question two: you answered %s" % third
if third == animals[2]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[2]
print "Question 3: you answered %s" % first
if first == animals[0]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[0]
print "Question 4: you answered %s" % three
if three == animals[3]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[3]
print "Question 5: you answered %s" % fifth
if fifth == animals[4]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[4]
print "Question 6: you answered %s" % two
if two == animals[2]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[2]
print "Question 7: you answered %s" % sixth
if sixth == animals[5]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[5]
print "Question 8: you answered %s" % four
if four == animals[4]:
	print "Correct answer!"
else:
	print "Wrong answer!"
	print animals[4]

