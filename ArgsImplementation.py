# *args allows us to use arbitrary number of arguments, instead of using fixed number of positional parameters
def myfunc(*args):
    return sum(args) * 0.10


print(myfunc(60, 40))
print(myfunc(60, 40, 50, 50))

# args are passed as Tuples
# Result of the below code is : (10, 20, 30)
def myfunc1(*args):
    print(args)


myfunc1(10, 20, 30)


def myfunc2(*args):
    for item in args:
        print(item)


myfunc2(10, 20, 30)

