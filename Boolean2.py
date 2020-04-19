# Empty String evaluates to False. Python expects boolean after 'if'. So, it evalues 0 & Name as 'False' in the
# code below
if 0:
    print("True")
else:
    print("False")
# Empty String evaluates to False. Python expects boolean after 'if'. So, it evalues 0 & Name as 'False' in the
# code below
if 0:
    print("True")
else:
    print("False")

Name = input("Please Enter your name : ")
if Name:
    print("Hello {}".format(Name))
else:
    print("Looks like you don't have name")
