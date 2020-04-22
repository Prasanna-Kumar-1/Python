# To Extract Items from the Dictionary
# Items are Tuples which have key, value pairs
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }

print(aus_cities)
print("_" * 60)
print("Display dict_items object of the Dictionary : ")
print(aus_cities.items())

# converting a Dictionary to a Tuple
print("_" * 60)
print("Converting a Dictionary to a regular Tuple : ")
aus_cities_tuple = tuple(aus_cities.items())
print(aus_cities_tuple)

# Iterating through a Tuple
print("_" * 60)
print("Iterating through a Tuple : ")
print()
aus_cities_tuple = tuple(aus_cities.items())

for item in aus_cities_tuple:
    state, capital_city = item
    print(state + " : " + capital_city)
