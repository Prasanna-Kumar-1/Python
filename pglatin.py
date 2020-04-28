# Implementation of PIG LATIN
# if a word starts with a vowel, add 'ay to end
# if a word does not start with a vowel, put first letter at the end, then add 'ay'
# For example, word -- > ordway
#              apple --> appleay
def pig_latin(word):
    first_letter = word[0]
    #   check if vowel
    if first_letter in 'aeiou':
        pig_latin_word = word + 'ay'
    else:
        pig_latin_word = word[1:] + first_letter + 'ay'
    return pig_latin_word


result = pig_latin("amir")
print(result)
