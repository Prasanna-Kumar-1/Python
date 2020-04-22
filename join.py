myList = ["Sydney", "Melbourne", "Brisbane", "Perth"]

new_string = ""

for i in myList:
    new_string = ", ".join(myList)

print(new_string)

# Another way of Demonstrating join
cities = "Sydney, Melbourne, Brisbane, Perth, Darwin"
all_cities = ""
all_cities = all_cities.join(cities)
print("All Australian cities are : " + all_cities)