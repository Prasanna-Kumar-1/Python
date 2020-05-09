# Demonstration of using args and kwargs together

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[2], kwargs['Junk']))


myfunc(10, 20, 30, fruit='oranges', food='eggs', Junk='Pizzas')

