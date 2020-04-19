#  Example to demonstrate if - elif concepts
Answer = 5

print("Guess a number between 1 and 10 : ")
Num = int(input())

if Num > 5:
    print("Wrong Guess, Guess a Lower Number")
    guess = int(input())
    if guess == Num:
        print("Well done, you have guessed it right")
    else:
        print("Sorry! You have guessed it incorrectly")
elif Num < 5:
    print("Wrong Guess, Guess a Higher Number ")
    guess = int(input())
    if guess == Num:
        print("Well done, you have guessed it right")
    else:
        print("Sorry! You have guessed it incorrectly")
else:
    print("You guessed it correctly")