#  Float formatting : "{value:width.precision f}

result = 10/99
print("The result is : {}".format(result))

# Another way of implementing
print("The result is : {r}".format(r=result))

# Lets now implement actual - Float formatting : "{value:width.precision f}
# Width - Total width/length of the number

print("The result is : {r:1.3f}".format(r=result))
# Result of the above : The result is : 0.101

print("The result is : {r:10.3f}".format(r=result))
# Result of the above : The result is :      0.101

