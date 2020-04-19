# Implementation of Dictionaries Concept
cities = {
    1: 'Sydney',
    2: 'Melbourne',
    3: 'Brisbane',
    4: 'Adelide'
}
print(cities[1])
print(cities[4])

aus_cities = {"NSW": "Sydney", "Victoria": "Melbourne", "Queensland": "Brisbane", "WA": "Perth"}
print(aus_cities["NSW"])
print(aus_cities["Victoria"])

# Adding a new element to a dictionary.
# When you are referring an individual item of a dictionary, always use [] - Square Brackets
# there is no append() method like we have in lists.
# We need to supply value for the key as shown below

print("*" * 40)
aus_cities["ACT"] = "Canberra"
print(aus_cities)

# Dictionaries - If the Key/Values are repeated, then the last one in the dictionary will be taken
# For example, the key "NSW" is repeated with 2 values. Then the last value will be taken in this case
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "NSW": "Parramatta"
              }
print(aus_cities["NSW"])

# Removing from the Dictionary
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }

# print(aus_cities)
del aus_cities["ACT"]
# If you don't specify the key,it will delete the entire dictionary.
# so,  be careful.  For example, below command will delete entire
# dictionary
del aus_cities
print(aus_cities)

# If you want to delete all the entries of the dictionary,
# but if you want to retain the dictionary skeleton, you can do this by below command

aus_cities.clear()