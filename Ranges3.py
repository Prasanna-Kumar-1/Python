# Implementation of ranges concept 3
range_numbers = range(0, 100)
print(range_numbers)

new_range = range_numbers[50:100:5]
print(new_range)

for i in new_range:
    print(i)

print("*" * 40)

for i in range(0, 100, 5):
    print(i)