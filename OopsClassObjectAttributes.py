# Implementation of Object Oriented Programming concepts

# __init__  :   constructor of the class
# self      :   reference to the instance of the class

class Dog():
    # Class Object Attributes   :   Attributes at the class level
    #                               Same for any instance of the class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #       Attributes
        #       We take in the arguments and assign them using 'self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    # Operations - methods
    def bark(self):
        print('whoof')


my_dog = Dog(breed='Lab', name='sweety', spots=False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

# type
print(type(my_dog))

# Class attribute
print(my_dog.species)

# use of method
my_dog.bark()