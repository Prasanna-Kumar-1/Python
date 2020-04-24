my_string = "Yash"

# Strings are immutable - Try changing first character of the above string, you will get an error
# ERROR DISPLAYED : TypeError: 'str' object does not support item assignment
# my_string[0] = "P"

# Way of changing the above string is
# 1. Slice it
# 2. Concatenate with the desired string/character. (String Concatenation Operator is +)

last_letters = my_string[1:]

full_name = "P" + last_letters

print(full_name)

# String functions

print(full_name.capitalize())

print(full_name.upper())

print(full_name.lower())

# String split by white space, default
my_name = "prasanna kumar"
print(my_name.split())

# Split by a
my_name = "prasanna kumar"
print(my_name.split('a'))

