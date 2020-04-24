# Tuple unpacking operator (*)
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


final_result = my_sum(1, 2, 3)
print(final_result)


def my_sum(inte):
    result = 0
    # Iterating over the Python args tuple
    for x in inte:
        result += x
    return result


intge = [1, 2, 3]

print(my_sum(intge))
