n = int(input("Enter the number of employees: "))
employees = {}

for i in range(n):
    name = input("Enter the name of the employee: ")
    salary = input("Enter the salary of the employee: ")
    emp_id = input("Enter the employee id of employee: ")
    address = input("Enter the address of employee: ")
    employees[name] = [emp_id, salary, address]

while True:
    print("####################################################################")
    name = input("Enter the employee name to be searched: ")
    info = employees.get(name, -1)

    if info == -1:
        print("Employee does not exist so insert his details")
        salary = input("Enter the salary of the employee: ")
        emp_id = input("Enter the employee id of employee: ")
        address = input("Enter the address of employee: ")

        employees[name] = [emp_id, salary, address]

    else:
        #print('Employee details are\n employee name: ', name, '\nemployee id: ', info[0], '\nEmployee salary: ', info[1], '\nEmployee address: ', info[2])
        print(f'Employee deatils are:\nemployee ID :{emp_id}\nemployee salary: {salary}\nemployee address: {address}')
    
    exit_choice = input("Do you want to exit? (Yes/No): ")

    if exit_choice.lower() == 'no':
        continue
    else:
        break

print(type(employees))
