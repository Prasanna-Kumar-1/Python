# To Extract the values from the dictionary.
# It is always efficient to extract the values using keys
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }
# To Display the keys of a Dictionary
print("-" * 50)
print("Keys of aus_cities dictionary are as below : ")
for key in aus_cities:
    print(key)

# To Display the values of a Dictionary
print("-" * 50)
print("Values of aus_cities dictionary are as below : ")
for val in aus_cities.values():
    print(val)

# Efficient Way : Another way to Display the values of a Dictionary
# Dictionary[iterable] produces the value of each key
print("-" * 50)
print("Values of aus_cities dictionary are as below : ")
for val in aus_cities:
    print(aus_cities[val])
print("-" * 50)

print(aus_cities.keys())
print(aus_cities.values())

