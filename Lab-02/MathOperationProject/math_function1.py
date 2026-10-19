def do_Add(num1, num2):
    return num1 + num2


def do_Subtract(num1, num2):
    return num1 - num2


def do_Product(num1, num2):
    return num1 * num2


def do_Divide(num1, num2):
    return num1 / num2


def main():
    print("The variable declaration and assignment")

    number1 = int(input("Enter the value of variable Number 1: "))
    number2 = int(input("Enter the value of variable Number 2: "))

    sum_result = do_Add(number1, number2)
    subtract_result = do_Subtract(number1, number2)
    product_result = do_Product(number1, number2)
    division_result = do_Divide(number1, number2)

    print("The sum of", number1, "and", number2, "is", sum_result)
    print("The subtract of", number1, "and", number2, "is", subtract_result)
    print("The product of", number1, "and", number2, "is", product_result)
    print("The division of", number1, "by", number2, "is", division_result)


main()