class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

animal = Animal()
print(animal)
print(animal.eat())
print(animal.who_am_i())

print("-" * 50)

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def eat(self):
        print("I am a dog and I am eating")

    def bark(self):
        print("I am a Dog and I Bark")

dog = Dog()
print(dog)
print(dog.who_am_i())
print(dog.eat())
print(dog.bark())