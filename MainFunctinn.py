# Knowing the value of the __name__ variable is important to write code that serves the dual purpose of (1)
# executable script and (2) importable module.

# __name__ takes on different values depending on how you executed your Python file. __name__ will be equal to:

# (1) "__main__" when the file is executed from the command line or with python -m (to execute a package’s __main__.py file)
# (2) The name of the module, if the module is being imported

# Example of having main() execute other functions
from time import sleep

print("This is my file to demonstrate best practices.")


def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data


def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data


def write_data_to_database(data):
    print("Writing data to a database")
    print(data)


def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)


if __name__ == "__main__":
    main()
