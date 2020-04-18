# Implementation of basic For Loop
Number = "1,123;456#789:"
Seperator = ""

for char in Number:
    if not char.isnumeric():
        Seperator = Seperator + char

print(Seperator)