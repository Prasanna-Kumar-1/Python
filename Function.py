def fun_operations(first, second, **options):
    if options.get("action") == "add":
        result = first + second
        return result

    if options.get("action") == "sub":
        if first > second:
            result = first - second
        else:
            result = second - first
        return result

    if options.get("action") == "mul":
        result = first * second
        return result


final_result = fun_operations(3, 4, action="sub")
print(final_result)
