# Implementation of Object Oriented Programming concepts

# __init__  :   constructor of the class
# self      :   reference to the instance of the class

class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # method
    def get_circumference(self):
        return self.radius * self.pi * 2


# print class object attribute
# IMP : Class object attribute can be referenced by 'Classname.classattribute' - Circle.pi
print(Circle.pi)

# default   :   radius=1
my_circle = Circle()
print(my_circle.get_circumference())

# radius = 2
my_circle = Circle(radius=2)
print(my_circle.get_circumference())
