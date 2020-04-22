# To Extract Items from the Dictionary
# Items are Tuples which have key, value pairs
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }
# Convert the Dictionary to Tuple using tuple
# Iterating through a Tuple
print("_" * 60)
print("Iterating through a Tuple : ")
print()
aus_cities_tuple = tuple(aus_cities.items())

for item in aus_cities_tuple:
    state, capital_city = item
    print(state + " : " + capital_city)

# Convert the Tuple to Dictionary using Dict() constructor
#  Iterating through a Tuple

aus_cities_dict = dict(aus_cities_tuple)
print(aus_cities_dict)  