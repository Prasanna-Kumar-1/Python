# Given two integers, print if the sum of the integers is 20 or
# if one of the integers is 20. If not, print message

def functionexample3(n1, n2):
    if n1 + n2 == 20:
        print("Sum of the numbers is 20")
    elif n1 == 20:
        print("First  Number is 20")
    elif n2 == 20:
        print("Second Number is 20")
    else:
        print("Neither sum is 20 nor any of the numbers is 20")


functionexample3(15, 50)
