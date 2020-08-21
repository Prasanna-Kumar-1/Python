# Implementation of Object Oriented Programming concepts

# class Sample():
#     pass
#
# # Creating an Instance of the class
# my_sample = Sample()
# print(type(my_sample))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Prasanna', 40)

print(p1.name)
print(p1.age)
