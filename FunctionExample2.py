# Implementation of function
# Write a function takes a two-worded string and prints True if both words begin with same letter

def functionexample3(text):
    # Convert the string into a list
    wordlist = text.lower().split()
    print(wordlist)
    # Check if the first letter of each word is equal to each other after converting into lower
    if wordlist[0][0] == wordlist[1][0]:
        print("Two words begin with the same letter")
    else:
        print("Two words does not begin with the same letter")


functionexample3('Prasanna ceter')