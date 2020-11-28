string_set = {"enjoying", "learning", "programming"}

new_set = set()

for str1 in string_set:
    new_string = str1.replace("ing", "")
    new_set.add(new_string)

print(new_set)

