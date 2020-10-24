# Method name like __init__ can be pronounced as "Underscore underscore init underscore underscore" sounds horrible
# and is almost a tongue twister. "Double underscore init double underscore" is a lot better, but the ideal way is
# "dunder init dunder" That's why magic methods methods are sometimes called dunder methods!

# So what's magic about the __init__ method?
# The answer is, you don't have to invoke it directly.
# The invocation is realized behind the scenes.
#
# When you create an instance x of a class A with the statement "x = A()", Python will do the necessary calls to
# __new__ and __init__.


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


# Object Initialization: __init__

# To construct "Book" objects from the "Books" class, I need a constructor which in Python is the __init__ dunder:

book = Book("Python", "Guido van Rossum", 200)
print(book)


# The above print will give us the result where the object is actually stored. Not the representation of the object
# Result could be something like this
# Result    :   <__main__.Book object at 0x00000201ED87A430>


# -----------------------------------------------------------------------------------------------------------------
# STRING REPRESENTATION OF THE CLASS
# -----------------------------------------------------------------------------------------------------------------
# Object Representation: __str__, __repr__ 1. It’s common practice in Python to provide a string representation of
# your object for the consumer of your class (a bit like API documentation.)
# 2. There are two ways to do this using # dunder methods:

# __repr__: The “official” string representation of an object. This is how you would make an object of the class.
#           The goal of __repr__ is to be unambiguous.

# __str__: The “informal” or nicely printable string representation of an object. This is for the enduser.

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.title!r}, {self.author!r}, {self.pages!r})")

    def __str__(self):
        return f"{self.title} By {self.author} : {self.pages}"


# __repr__  :   The “official” string representation of an object
book = Book("Python", "Guido van Rossum", 200)
print(repr(book))

# __str__   :   “informal” or nicely printable string representation of an object
print(str(book))
