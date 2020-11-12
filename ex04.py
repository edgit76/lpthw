# Underneath are the various variables referencing:
# numbers, numbers with floating points, variables and variables operations.
# Note that when the variable are words, these have to be connected with an underscore '_'.
cars = 100 #State the number that is going to be associated to "cars".
space_in_a_car = 4.0 #State the number of passengers each car can have.
drivers = 30 #State the number of drivers.
passengers = 90 #State the total number of passengers.
cars_not_driven = cars - drivers #Tells how to find out the number of cars not driven.
cars_driven = drivers #State that the number of cars driven equals the number of drivers available.
carpool_capacity = cars_driven * space_in_a_car #State the maximum number of passenger that can take a ride.
average_passengers_per_car = passengers / cars_driven #Tells the average number of passengers per car.

# You can print several strings separated by variants.
# Variants have to be separated from strings with commas "string, x, string".
print "There are", cars, "cars available." 
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."