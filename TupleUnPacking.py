my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Tuple Unpacking
for item in my_list:
    first_num, second_num = item
    print(first_num)
    print(second_num)
    print('-' * 40)

# Another way of implementing Tuple Unpacking

print('*' * 40)
for first_num, second_num in my_list:
    print(first_num)