# Creating a Set
aus_cities = {"Sydney", "Melbourne", "Adelaide", "Brisbane"}
print(aus_cities)

for cities in aus_cities:
    print(cities)

# Converting a List into a set using set constructor
print("-" * 60)
aus_suburbs = set(["Parramatta", "Chatswood", "WestMead", "Toongabie"])
print(aus_suburbs)

for suburbs in aus_suburbs:
    print(suburbs)

# Converting a range into a set using set constructor
print("-" * 60)
even = set(range(0, 100, 2))
print(even)

# Converting a tuple into a set using set constructor
print("-" * 60)
squares_tuple = (4, 9, 16, 25)
squares_set = set(squares_tuple)
print(squares_set)

# Demonstration of union on Set
print("-" * 60)
even = set(range(0, 20, 2))
print(len(even))
print("Printing the even set : ")
print(even)

# Combining two sets using Union Operator
print("-" * 60)
squares_tuple = (4, 9, 16, 25)
squares_set = set(squares_tuple)
print(len(squares_set))
print("Printing the squares set : ")
print(squares_set)

print("-" * 60)
print("Printing the union of even & squares set")
print(even.union(squares_set))
print(len(even.union(squares_set)))

# Intersection of two sets
print("-" * 60)
print("Printing the intersection of even & squares set")
print(even.intersection(squares_set))
print(even & squares_set)