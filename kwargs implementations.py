# This is a demonstration of *kwargs
# *kwargs returns a dictionary

def myfun1(**kwargs):
    print(kwargs)
    if 'City' in kwargs:
        print('I stay in {}'.format(kwargs['City']))
    else:
        print("I don't stay in any Australian city")

myfun1(City='Brisbane')
