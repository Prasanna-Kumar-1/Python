# # Implementation of break
shopping_list = ["Milk", "Rice", "Eggs", "Oats", "Spam", "Bread"]

for item in shopping_list:
    if item == "Spam":
        break
    print("Need to buy :  {}".format(item))