# Testing a simple condition in Python
Name = input("Enter your Name : ")
Age = int(input("How old are you, {0} : ".format(Name)))
print("Age of {0} is {1}".format(Name, Age))

if Age < 18:
    print("{} is NOT eligible for voting ".format(Name))
elif Age == 200:
    print("Come on {}! Are you Joking that your age is 200 years".format(Name))
else:
    print("{} is eligible for voting".format(Name))