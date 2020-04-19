# Different flavour of Tuple Un Packing
tuple1 = "Parramatta", 2150, "Sydney", "Australia", (("Cowper Street", 100), ("Cowper Street", 101), ("Cowper Street", 102))
suburb, postcode, city, country, address = tuple1

print(suburb)
print(postcode)
print(city)
print(country)
print(address)

# # Different flavour of Tuple Un Packing
tuple1 = "Parramatta", 2150, "Sydney", "Australia", ("Cowper Street", 100), ("Cowper Street", 101), ("Cowper Street", 102)
suburb, postcode, city, country, address1, address2, address3 = tuple1

print(suburb)
print(postcode)
print(city)
print(country)
print(address1)
print(address2)
print(address3)

# # Different flavour of Tuple Un Packing using for loops
tuple1 = "Parramatta", 2150, "Sydney", "Australia", (("Cowper Street", 100), ("Cowper Street", 101), ("Cowper Street", 102))
suburb, postcode, city, country, Address = tuple1

print(suburb)
print(postcode)
print(city)
print(country)
for property_address in Address:
    street, property_number = property_address
    print("\tStreet: {}, Property Address: {}".format(street, property_number))

# Implementing a list within a Tuple.
# Tuples are immutable meaning the contents of Tuple cannot be changed
# Tuples can contain Lists as elements and Lists themselves can be changed as List are mutuable.
tuple1 = "Parramatta", 2150, "Sydney", "Australia", [("Cowper Street", 100), ("Cowper Street", 101), ("Cowper Street", 102)]
suburb, postcode, city, country, Address = tuple1

print(suburb)
print(postcode)
print(city)
print(country)

# Here Address is now a list. We can now use append method to the list add couple of more elements
# which are actually Tuples
#
Address.append(("Cowper Street", 103))
Address.append(("Cowper Street", 104))

for property_address in Address:
    street, property_number = property_address
    print("\tStreet: {}, Property Address: {}".format(street, property_number))