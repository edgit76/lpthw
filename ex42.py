# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # class Dog has-a __init__ that takes self and name params
        self.name = name

# class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # class Cat has-a __init__ that takes self and name params 
        self.name = name

# class Person is-a object
class Person(object):

    def __init__(self, name):
        # class Person has-a __init__ that takes self and name params
        self.name = name
 
        # Person has-a pet of some kind
        self.pet = None

# class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # class Employee has-a __init__ that takes self, name and salary params
        # and calls the __init__ method of the Person class passing name as param
        super(Employee, self).__init__(name)
        # from self get the salary attribute and set it to salary
        self.salary = salary

# class Fish is-a object
class Fish(object):
    pass

# class Salmon is-a Fish
class Salmon(Fish):
    pass

# class Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a dog
#(set rover to an instance of class Dog with param "Rover" as an attribute)
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# frank is-a Employee
#(set frank to an instance of class Employee with params "Frank" and 120000 
# as attributes)
frank = Employee("Frank", 120000)

# from frank get the pet attribute and set it to rover
frank.pet = rover

# flipper is a Fish
# (se flipper to an instance of class Fish)
flipper = Fish()

# crouse is a Salmon
crouse = Salmon()

# set harry is a Halibut
harry = Hallibut()