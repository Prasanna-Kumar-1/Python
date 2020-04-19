# Refining the Loops using != Operator
Answer = 5

print("Guess a number between 1 and 10 : ")
Num = int(input())

if Num != Answer:
    if Num < Answer:
        print("Please guess a higher number")
    else:
        print("Please guess a lower number")
    Num = int(input())
    if Num == Answer:
        print("Well done! you guessed it right")
    else:
        print("Sorry, you have guessed it wrong")
else:
    print("You have guessed it correctly in the first go")