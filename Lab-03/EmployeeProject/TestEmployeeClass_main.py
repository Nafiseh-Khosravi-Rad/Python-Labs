from employee_template import Employee, Executive, Manager


def main():

    # Create four Employee objects
    emp1 = Employee(5436, "Peterson Jeff", 20, 35000)
    emp2 = Employee(1983, "Khan Ali", 15, 50000)
    emp3 = Employee(2005, "Sandy Ana", 17, 60000)
    emp4 = Employee(3900, "Kimberly Sarah", 9, 450000)

    employees = [emp1, emp2, emp3, emp4]

    # Display information and bonus for emp1 to emp4
    for emp in employees:

        print("\nData attributes of employee:")
        emp.printEmployeeInfo()

        print(
            "The bonus of",
            emp.getEmpName(),
            "for",
            emp.getEmpExtradays(),
            "extra days is",
            emp.CalculateEmpBonus(),
            "$"
        )

    # Create emp5 from end-user input
    print("\nSet Data Attributes for emp5 Object")

    emp5 = Employee(0, "", 0, 0)

    emp_id = int(input("Please enter the Employee Id: "))
    emp_name = input("Please enter the Employee Name: ")
    emp_extra_days = int(
        input("Please enter the Employee Extra worked days: ")
    )
    emp_salary = float(
        input("Please enter the Employee Salary: ")
    )

    emp5.setEmpId(emp_id)
    emp5.setEmpName(emp_name)
    emp5.setEmpExtradays(emp_extra_days)
    emp5.setEmpSalary(emp_salary)

    print("\nData attributes of emp5 after entered by End user:")
    emp5.printEmployeeInfo()

    print(
        "The bonus of",
        emp5.getEmpName(),
        "for",
        emp5.getEmpExtradays(),
        "extra days is",
        emp5.CalculateEmpBonus(),
        "$"
    )

    # Create emp6Exe using values from Figure 3
    emp6Exe = Executive(
        5438,
        "Johnston Bob",
        15,
        89000,
        90.25
    )

    print("\nData attributes of emp6Exe object from Child class Executive:")
    print(
        emp6Exe.getEmpId(),
        "//",
        emp6Exe.getEmpName(),
        "//",
        emp6Exe.getEmpExtradays(),
        "//",
        emp6Exe.getEmpSalary(),
        "//",
        emp6Exe.getEmpExtraHours()
    )

    print(
        "The bonus of",
        emp6Exe.getEmpName(),
        "for",
        emp6Exe.getEmpExtradays(),
        "extra days and",
        emp6Exe.getEmpExtraHours(),
        "extra hours is",
        format(emp6Exe.CalculateEmpBonus(), ".2f"),
        "$"
    )

    # Create emp7Exe from end-user input
    print("\nSet Data Attributes for emp7Exe Object from Executive class")

    emp7_id = int(input("Please enter the Employee Id: "))
    emp7_name = input("Please enter the Employee Name: ")
    emp7_days = int(
        input("Please enter the Employee Extra worked days: ")
    )
    emp7_salary = float(
        input("Please enter the Employee Salary: ")
    )
    emp7_hours = float(
        input("Please enter the Employee Extra worked hours: ")
    )

    emp7Exe = Executive(
        emp7_id,
        emp7_name,
        emp7_days,
        emp7_salary,
        emp7_hours
    )

    print("\nData attributes of emp7Exe object from Child class Executive:")
    print(
        emp7Exe.getEmpId(),
        "//",
        emp7Exe.getEmpName(),
        "//",
        emp7Exe.getEmpExtradays(),
        "//",
        emp7Exe.getEmpSalary(),
        "//",
        emp7Exe.getEmpExtraHours()
    )

    print(
        "The bonus of",
        emp7Exe.getEmpName(),
        "for",
        emp7Exe.getEmpExtradays(),
        "extra days and",
        emp7Exe.getEmpExtraHours(),
        "extra hours is",
        format(emp7Exe.CalculateEmpBonus(), ".2f"),
        "$"
    )

    # Create emp8Man using values from Figure 5
    emp8Man = Manager(
        1298,
        "Pandar Raoul",
        10,
        71000,
        100.5
    )

    print("\nData attributes of emp8Man object from Child Manager class:")
    print(
        emp8Man.getEmpId(),
        "//",
        emp8Man.getEmpName(),
        "//",
        emp8Man.getEmpExtradays(),
        "//",
        emp8Man.getEmpSalary(),
        "//",
        emp8Man.getEmpExtraHours()
    )

    print(
        "The bonus of",
        emp8Man.getEmpName(),
        "for",
        emp8Man.getEmpExtradays(),
        "extra days and",
        emp8Man.getEmpExtraHours(),
        "extra hours is",
        format(emp8Man.CalculateEmpBonus(), ".2f"),
        "$"
    )

    # Create emp9Man from end-user input
    print("\nSet Data Attributes for emp9Man Object from Manager class")

    emp9_id = int(input("Please enter the Employee Id: "))
    emp9_name = input("Please enter the Employee Name: ")
    emp9_days = int(
        input("Please enter the Employee Extra worked days: ")
    )
    emp9_salary = float(
        input("Please enter the Employee Salary: ")
    )
    emp9_hours = float(
        input("Please enter the Employee Extra worked hours: ")
    )

    emp9Man = Manager(
        emp9_id,
        emp9_name,
        emp9_days,
        emp9_salary,
        emp9_hours
    )

    print("\nData attributes of emp9Man object from Child Manager class:")
    print(
        emp9Man.getEmpId(),
        "//",
        emp9Man.getEmpName(),
        "//",
        emp9Man.getEmpExtradays(),
        "//",
        emp9Man.getEmpSalary(),
        "//",
        emp9Man.getEmpExtraHours()
    )

    print(
        "The bonus of",
        emp9Man.getEmpName(),
        "for",
        emp9Man.getEmpExtradays(),
        "extra days and",
        emp9Man.getEmpExtraHours(),
        "extra hours is",
        format(emp9Man.CalculateEmpBonus(), ".2f"),
        "$"
    )

    # Save Executive and Manager data in Employee.txt
    emp_file = open("EmployeeProject/Employee.txt", "w")

    emp_file.write(
        str(emp6Exe.getEmpId()) + "\t" +
        emp6Exe.getEmpName() + "\t" +
        str(emp6Exe.getEmpExtradays()) + "\t" +
        str(emp6Exe.getEmpSalary()) + "\t" +
        str(emp6Exe.getEmpExtraHours()) + "\n"
    )

    emp_file.write(
        str(emp7Exe.getEmpId()) + "\t" +
        emp7Exe.getEmpName() + "\t" +
        str(emp7Exe.getEmpExtradays()) + "\t" +
        str(emp7Exe.getEmpSalary()) + "\t" +
        str(emp7Exe.getEmpExtraHours()) + "\n"
    )

    emp_file.write(
        str(emp8Man.getEmpId()) + "\t" +
        emp8Man.getEmpName() + "\t" +
        str(emp8Man.getEmpExtradays()) + "\t" +
        str(emp8Man.getEmpSalary()) + "\t" +
        str(emp8Man.getEmpExtraHours()) + "\n"
    )

    emp_file.write(
        str(emp9Man.getEmpId()) + "\t" +
        emp9Man.getEmpName() + "\t" +
        str(emp9Man.getEmpExtradays()) + "\t" +
        str(emp9Man.getEmpSalary()) + "\t" +
        str(emp9Man.getEmpExtraHours()) + "\n"
    )

    emp_file.close()

    print("\nEmployee data saved in Employee.txt")


main()