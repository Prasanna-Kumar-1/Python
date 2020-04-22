aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }

aus_suburbs = {"Chatswood": "Chatswood",
               "Parramatta": "Parramatta"}

aus_cities.update(aus_suburbs)
print(aus_cities)

print("-" * 60)
print("Copying one dictionary to another dictionary")
aus_places = aus_cities.copy()
aus_places.update(aus_suburbs)
print(aus_places)
