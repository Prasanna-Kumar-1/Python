# Iterating over a dictionary
aus_cities = {"NSW": "Sydney",
              "Victoria": "Melbourne",
              "Queensland": "Brisbane",
              "WA": "Perth",
              "ACT": "Canberra"
              }
for i in range(10):
    for city in aus_cities:
        print(aus_cities[city])
    print("-" * 40)