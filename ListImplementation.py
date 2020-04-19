# Implementation of List concepts
australian_city_list = ["Sydney", "Melbourne", "Brisbane", "Perth"]

for city in australian_city_list:
    print("{} is a part of australian_city_list ".format(city))

# Appending an item to a List
australian_city_list.append("Adelide")
print(australian_city_list)

# Concatenating the lists
even_number_list = [2, 4, 6, 8]
odd_number_list = [1, 3, 5, 7]

number_list = even_number_list + odd_number_list
number_list.sort()
print(number_list)
#