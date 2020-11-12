# Putting all in one code.

print "I",
print "love\n"
print "\ttriffles that are 11\" tall."
print "\n"
print "Avocado smoothies are", 1 + 2 * 1 * 10 * 7, "times better than guacamole.\n"
a = 3
b = 2
c = 5
d = 8
e = 7
f = ("%d, %d, %d, %d, %d\n")
print f % (a+b, b, c, d, e-d)

print "Is a = c?", a <= c
print "Is a == d - c?", a == d - c
print "Is e greater-than d?", e > d
print "Is b less-than c?", b < c
print "Is c + b <= b + e?", c + b <= b + e

pens = 30
pencils = 20
erasors = 10
tools = pens + pencils - erasors

print "\nI have %d pens, %d pencils and %d erasors, and a total of %d tools.\n" % (pens, pencils, erasors, tools)

name = "Paul"
age = 50
eyes = "brown"
tall = "6'11\""

print "This is %s, he is %d years old, has %s eyes and is %r tall." % (name, age, eyes, tall)

hilarious = False
mark = "Is Mark the same person as Paul? %s"

print mark % hilarious

print "How old are you?"
raw_input()
print "How old are you?",
age2 = raw_input(">")
print raw_input("How old are you? : --> ")

from sys import argv

script, first, second, third = argv

print "The variables of script %s are: %s, %s and %s." % (script, first, second, third)

print """\nAnd this is
how you write
a line over several other lines."""

txt = open(first)

print "This are the contents of %s: \n" % first
print txt.read()

data = txt.read()
print "Size of file is: %r " % len(data)
txt_write = open(first, "a+")
txt_write.write("This is line x\n")

print txt.read()


txt.close()
txt_write.close()

	


