# Implementation of Tuples Concept
# Tuples are order collection of items
# Tuples are immutable, meaning you cannot modify the items within Tuples

my_tuple = "Sydney", "is", "beautiful", "city", "to live", 2150
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])

# Try modifying the item within the Tuples
my_tuple[0] = "Melbourne"

# Work around to change the contents of the Tuple.
# Create another Tuple and point the variable to reference it

my_updated_tuple = "Melbourne", my_tuple[1], my_tuple[2], my_tuple[3], my_tuple[4], my_tuple[5]
print(my_updated_tuple)