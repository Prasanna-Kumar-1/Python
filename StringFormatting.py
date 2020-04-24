#  String formatting using .format() method and f-string(formatted string literals)
#  {} acts as a place holder
print("I am currently staying in {}".format("Australia"))

print("Popular cities in Australia are : {} {} {} ".format("Sydney", "Melbourne", "Brisbane"))

# Another way of implementing

print("Popular cities in Australia are : {1} {0} {2} ".format("Sydney", "Melbourne", "Brisbane"))

print("Popular cities in Australia are : {0} {0} {0} ".format("Sydney", "Melbourne", "Brisbane"))

#  String formatting using f-string(formatted string literals)
name = "Prasanna"
print(f'My Name is {name}')

name = "Prasanna"
country_live_in = "Australia"
print(f'My name is {name} and i live in {country_live_in}')
