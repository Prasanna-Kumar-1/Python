# # Implementation of Continue
shopping_list = ["Milk", "Rice", "Eggs", "Oats", "Bread", "Spam"]

for item in shopping_list:
    if item == "Spam":
        continue
    print("Need to buy :  {}".format(item))