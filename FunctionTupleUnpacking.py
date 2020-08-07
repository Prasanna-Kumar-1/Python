# Implementation of return functionality with Tuple Unpacking

work_hours = [('Prasanna', 1000), ('Sam', 200), ('Peter', 300)]


def check_employee(work_hours):
    # Place holders
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)


emp, work_hours = check_employee(work_hours)
print(emp)
