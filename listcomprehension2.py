# list comprehension using conditional logic
# new_list = [expression for member in iterable (if conditional)]

sentence = 'the rocket came back from mars'

vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

# what if you want to change a member value instead of filtering it out?
# In this case, it’s useful to place the conditional near the beginning of the expression:

# new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)