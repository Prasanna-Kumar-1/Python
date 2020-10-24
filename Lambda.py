# This is to demonstrate use of Lambda functions
# lambda arguments: expression

double = lambda x: x * 2
print(double(5))

# NOTE : Lambda functions are used along with built-in functions like filter(), map() etc.

# Lambda with filter()
# ---------------------

# The filter() function in Python takes in a function and a list as arguments.
# 1st Argument : Function
# 2nd Argument : list as argument

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

# Lambda with map()
# ---------------------

# The map() function in Python takes in a function and a list.
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
