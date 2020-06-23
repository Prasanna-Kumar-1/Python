# Implementation of Zip() function
a = [5, 10, 15, 20, 25, 30]
b = [10, 20, 30, 40, 50, 30]

# The zip() function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc

for i, j in zip(a, b):
    print(i, j)

for i, j in zip(a, b):
    print(i, j, i is j)