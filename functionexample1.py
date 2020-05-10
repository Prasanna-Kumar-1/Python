# Demonstration of function implementation - Check if passed number is odd or even
# Since the *args passes a Tuple, first iterate through the Tuple and check if the number is odd or even

def myfunc(*args):
    for i in args:
        if i % 2 == 0:
            print(i)


myfunc(5, 6, 7, 8)
