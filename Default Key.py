# Adding a default value of key if the key is not present
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }
while True:
    input_state = input("Please enter state name for which you want to find capital city : ")
    if input_state == "quit":
        break
    city_value = aus_cities.get(input_state, "We don't have any such {} state ".format(input_state))
    print(city_value)
if input_state in aus_cities:
    city_value = aus_cities.get(input_state)
    print(city_value)
else:
    print("There is no state named {} in the list of aus_cities ".format(input_state))