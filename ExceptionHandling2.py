def ask_for_int():
    while True:
        try:
            result = int(input("Please Enter any number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("You have correctly entered number. Thank you")
            break
        finally:
            print("End of try/except/finally block")
            print("I always run at the end")


if __name__ == "__main__":
    ask_for_int()
