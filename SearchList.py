# Searching a list and implement break
shopping_list = ["Milk", "Rice", "Eggs", "Oats", "Spam", "Bread"]
item_to_buy = "Moron"
found_at = None
for index in range (len(shopping_list)):
    if shopping_list[index] == item_to_buy:
        found_at = index
        break

if found_at is not None:
    print("Item {} is found at the position {} in the shopping list ".format(item_to_buy, found_at))
else:
    print("Item {} not found ".format(item_to_buy))