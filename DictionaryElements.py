# Dictionary can have list as well as another dictionary as elements
# To Extract a value from a dictionary, always use dict['key'].
# Key has to be enclosed in single quotes within []
my_dictionary = {'k1': 100, 'k2': [0, 1, 2], 'k3': {'Inside_Key': 999}, 'k4': ['prasanna', 'kumar']}
print(my_dictionary['k2'])

# Extracting element from a list, which is an element of the Dictionary
# To extract the element at index 1 from the list, which is an element of dictionary
# Result is 1
print(my_dictionary['k2'][1])

# Extracting element from a Dictionary, which is an element of the Dictionary
# To extract the value of the key of a dictionary, which is an element of outer dictionary
# Result is 1
print(my_dictionary['k3']['Inside_Key'])

print(my_dictionary['k4'][0].upper())

# Adding a new element to a dictionary
# Result should be : {'k1': 100, 'k2': [0, 1, 2], 'k3': {'Inside_Key': 999}, 'k4': ['prasanna', 'kumar'], 'k5': 100}
my_dictionary['k5'] = 100
print(my_dictionary)

# Replacing an element in a Dictionary
# Dictionaries are mutable
# Replacing the value of K5 with 'NEW VALUE'
# Result should be : {'k1': 100, 'k2': [0, 1, 2], 'k3': {'Inside_Key': 999}, 'k4': ['prasanna', 'kumar'], 'k5': 'NEW VALUE'}

my_dictionary['k5'] = 'NEW VALUE'
print(my_dictionary)

# To get all the keys of a Dictionary
print(my_dictionary.keys())

# To get all the values of a Dictionary
print(my_dictionary.values())

# To get all the items of a Dictionary
# Items are returned as Tuples
print(my_dictionary.items())
