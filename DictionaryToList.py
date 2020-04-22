# To display the items in a dictionary in an order, it is better to convert a Dictionary to a List
# Sort the list and display the list
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }
ordered_states = list(aus_cities.keys())
ordered_states.sort()
# We can also achieve the soring using the below commands
# ordered_states = sorted(list(aus_cities.keys()))
for state in ordered_states:
    print(state + " = " + aus_cities[state])
