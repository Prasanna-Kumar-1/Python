# Given a string, return a string where for every character in the original there are three characters
def paperdoll(text):
    result = ''
    for char in text:
        result += char+char+char
    print(result)

paperdoll('prasanna')