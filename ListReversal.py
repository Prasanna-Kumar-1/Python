#  Demonstration of different ways of list reversal

numbers1 = [1, 2, 3, 4, 5]
numbers1.reverse()
print(numbers1)

numbers2 = [7, 8, 9, 10, 11]
result2 = list(reversed(numbers2))
print(result2)

numbers4 = [100, 99, 98, 97, 96]
result4 = numbers4[::-1]
print(result4)


