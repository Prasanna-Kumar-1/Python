# Using for loops

list1 = []
for i in range(10):
    list1.append(i * i)

print(list1)

# List comprehensions
# new_list = [expression for member in iterable]
# expression :  expression can be
#               (1) member itself,
#               (2) a call to a method, or any
#               (3) other valid expression that returns a value.
#
#               In the example above, the expression i * i is the square of the member value
# In the below example, the expression is i * i

squares = [i * i for i in range(10)]
print("List Comprehension Demo - Squares are: " + str(squares))