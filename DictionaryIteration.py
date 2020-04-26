# Implementation of Dictionary iteration

dict1 = {'k1':1, 'k2':2, 'k3': 3}

# Iterating through dictionary
for item in dict1:
    print(item)

# Iterating through items of a Dictionary
for item in dict1.items():
    print(item)

# Iterating through key, value pairs of a Dictionary - Tuple Unpacking
for key, value in dict1.items():
    print(key)
    print(value)