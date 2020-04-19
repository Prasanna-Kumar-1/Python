# Implementing iterbales using Lists

list1 = ['Sydney', 'Melbourne', 'Adelide', 'Brisbane', 'Perth']

my_iterator = iter(list1)

for item in range(0,len(list1)):
    next_item = next(my_iterator)
    print(next_item)
