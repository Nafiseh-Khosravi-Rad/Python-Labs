import math


def evaluate_f1(x):
    return 3 * x


def evaluate_f2(x, z):
    return x * math.sqrt(z)


def evaluate_f3(z, t):
    return 5 * z * t


def evaluate_f4(y, t):
    return math.pow(10, y) / t


def main():
    print("The variable declaration and assignment")

    number1X = int(input("Enter the value of variable Number 1 X: "))
    number2Y = int(input("Enter the value of variable Number 2 Y: "))
    number3Z = int(input("Enter the value of variable Number 3 Z: "))
    number4T = int(input("Enter the value of variable Number 4 T: "))

    result_f1 = evaluate_f1(number1X)
    result_f2 = evaluate_f2(number1X, number3Z)
    result_f3 = evaluate_f3(number3Z, number4T)
    result_f4 = evaluate_f4(number2Y, number4T)

    print("The result of evaluate_f1 is", result_f1)
    print("The result of evaluate_f2 is", result_f2)
    print("The result of evaluate_f3 is", result_f3)
    print("The result of evaluate_f4 is", result_f4)


main()