# Implementation of lambda with string functions

names = ['Prasanna', 'Neethi', 'Yash']
first_letter = list(map(lambda x: x[0], names))

print(first_letter)

# Reversing string using lambda

revers = list(map(lambda x:x[::-1], names))
print(revers)

