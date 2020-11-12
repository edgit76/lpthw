the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# The first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# Same as above
for fruit in fruits:
	print "A fruit of a type %s." % fruit

# Also we can go through  mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# We cal also build lists, first start with an empty one
elements = []

# then use the range functions to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# Append is a function that lists understand
	elements.append(i)
# You could  create and empty list and add items 1 by 1 using append(). 
# The only problem is that it would take longer then using the range() function
# and the number will enter the list as you enter them, on that order.

# Now we can print them out also
for numbers in elements:
	print "Element was %d." % numbers

######################################
print #
# you can create an empty list and add items 1 by 1. They will be out of order and require
# several commands depending how long the list is.
newlist = [] # create empty list
newlist.append(110) # add value to the list
newlist.append(100) # "
newlist.append(105) # "
print newlist

# By creating a list with the help of 'for" loop, the creation of a list can be quicker
newlist2 = [] # create empty list
for g in range(100, 111): # set the 'for' loop and the range of the list to be created
	print "Adding %s to the list." % g # this output will be printed as many times as there are numbers in the range.
	newlist2.append(g) # use append function to add the range to the list

print newlist2

# for x in list:
# Everything after the 'for' loop argument is repeated as many times as there are 
# items on the list, and the 'x' is present on the function.


for i in range(-10, 10):
	print i


