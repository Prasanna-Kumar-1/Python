def ask_for_int():
    try:
        result = int(input("Please Enter any number: "))
    except:
        print("Whoops! That is not a number")
    else:
        print("You have correctly entered number. Thank you")
    finally:
        print("End of try/except/finally block")
        print("I always run at the end")


ask_for_int()
