# This script demonstrates that Given an integer, return the integer with reversed digits.
# Integer can be either positive or negative

# Convert the input number into a string array
def reverse_number(x):
    string = str(x)

# Validate whether the first character of string is a negative number.
# If so, separate the '-' symbol, reverse the rest of the number and append the '-' symbol back
# Use string slicing to reverse the string

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


print(reverse_number(-123))
print(reverse_number(456))