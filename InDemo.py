# Demonstration of 'in'

Name = "Prasanna Kumar"

Letter = input("Enter a letter, you wish to check : ")

if Letter in Name:
    print("{} is present in {}".format(Letter, Name))
else:
    print("{} is NOT present in {}".format(Letter, Name))