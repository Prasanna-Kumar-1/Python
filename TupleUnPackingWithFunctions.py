employee_salary = [('Prasanna', 100), ('Neethi', 200), ('Yash', 300)]


def employee_salary_check(salary):
    highest_salary = 0
    highest_salaried_employee = ''

    for employee, salary in employee_salary:
        if salary > highest_salary:
            highest_salary = salary
            highest_salaried_employee = employee
        else:
            pass

    return employee, highest_salary


empl, highest_salary_of_employee = employee_salary_check(employee_salary)
print('Name of the highest salaried employee : ' + empl)
print('highest salary of the employee is : ' + str(highest_salary_of_employee))