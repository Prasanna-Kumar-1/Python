# Implementation of Ranges Concept 2
small_d = range(1, 10)
print(small_d)

print(small_d[1])
print(small_d.index(2))

fives = range(0, 1000, 5)
print(fives)

input_number = int(input("Please enter a number : "))
if input_number in fives:
    print('{} is divisible by 5'.format(input_number))