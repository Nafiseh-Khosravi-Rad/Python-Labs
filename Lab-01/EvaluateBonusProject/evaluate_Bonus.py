# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: EvaluateBonusProject

# Input:
# salary, rate

# Processing:
# total_Bonus = salary * rate

# Output:
# salary, rate, total_Bonus


def main():

    # Display the program title
    print("\n\tEvaluate Bonus\n")

    # Get salary and bonus rate from the user
    salary = float(input("Enter your salary: "))
    rate = float(input("Enter your bonus rate: "))

    # Calculate the total bonus
    total_Bonus = salary * rate

    # Display the results
    print("\n\tSalary =", format(salary, ".2f"))
    print("\tRate =", format(rate, ".4f"))
    print("\tTotal Bonus =", format(total_Bonus, ".2f"))


# Call the main function
main()