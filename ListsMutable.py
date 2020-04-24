# Lists are mutable. We can change the items in the List
my_list1 = ["one", "two", "three"]
my_list2 = ["four", "five", "six"]
my_list3 = ["seven", "eight", "nine"]

# Try changing the item in the list
my_list1[0] = "ONE ALL IN CAPS"
print(my_list1)

# Various methods Lists
# Append to a list
my_list1.append("zero")
print(my_list1)

# Removing from a list
my_list1.pop(3)
print(my_list1)

# Sort a list
new_char_list = ['b', 'a', 'e', 'c', 'd']
new_num_list = [3, 2, 4, 1, 5]

# new new_char_list.sort() returns none.
# So, the following statement returns none
print(new_char_list.sort())
print(new_num_list.sort())

# Ideal way of sorting a list
new_num_list.sort()
print(new_num_list)

new_char_list.sort()
print(new_char_list)

# Reversing a list
new_num_list.reverse()
print(new_num_list)

new_char_list.reverse()
print(new_char_list)
