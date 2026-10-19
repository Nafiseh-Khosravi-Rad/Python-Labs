# Lab 2: Decision Structures, Looping, Functions
# Author: Nafiseh Khosravi Rad
# Project: EvaluateBonusProject

# Input:
# salary, rate, number_Bonus, do_repeat

# Processing:
# total_Bonus = salary * rate
# Check performance level using if / elif / else
# Check promotion qualification using nested if / else
# Repeat the program while do_repeat == "y"

# Output:
# salary, rate, total_Bonus
# performance message
# promotion qualification

def main():

    print("\n\tEvaluate Bonus\n")

    do_repeat = "y"

    while do_repeat == "y":

        salary = float(input("Enter your salary: "))
        rate = float(input("Enter your bonus rate: "))

        total_Bonus = salary * rate

        print("\n\tSalary =", format(salary, ".2f"))
        print("\tRate =", format(rate, ".4f"))
        print("\tTotal Bonus =", format(total_Bonus, ".2f"))

        print("\n\tComment on Your Performance:")

        if total_Bonus < 500:
            print("\tLow Performance.")
            print("\tYou need to do more.")

        elif total_Bonus < 1000:
            print("\tAverage Performance.")
            print("\tYou can do better.")

        elif total_Bonus < 2000:
            print("\tGood Performance.")
            print("\tContinue your effort.")

        else:
            print("\tExcellent Performance.")
            print("\tWe appreciate your effort.")

        if total_Bonus >= 1000:

            print("\n\tYou qualify for promotion,")
            print("\tbut one more condition is required.")

            number_Bonus = int(
                input("Enter the number of bonuses received in the past: ")
            )

            if number_Bonus >= 3:
                print("\tYou are qualified for promotion.")
            else:
                print("\tYou need at least 3 previous bonuses.")

        else:
            print("\n\tYou need at least $1000 bonus")
            print("\tto qualify for promotion.")

        do_repeat = input("\nDo you want to enter new value y/n? ")


main()