# Python's f-strings with Python version >= 3.6) lets us embed variables and even expressions

for i in range(3):
    print(f'{i} Apple')

print("_" * 40)

for i in range(3):
    print(f'{i} Apple{"s" if i == 2 else ""}')