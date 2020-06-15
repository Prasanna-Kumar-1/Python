# Implementation of print + join on a List

my_list = ["1", "Prasanna", "Python", "QA Analyst"]
print(','.join(str(x) for x in my_list))

# Unpack the list with * into positional arguments passed to the function(i.e print() function in this case)
print(*my_list, sep=" ")

#
my_list = ["1", "Prasanna", "Python", "QA Analyst"]
for x in my_list:
    print(str(x))