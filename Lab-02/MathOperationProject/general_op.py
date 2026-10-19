import MathCalculation


def display_message():
    print("Creating Non-Returning Function")


def display_logo():
    print("Display Logo")
    print("From Vanier College")


def evaluate_exp(x, y):
    print("Evaluating Exp")
    result = 5 * x - 10 * y
    return result


def main():
    print("Using Hierarchy Chart")

    display_message()
    display_logo()

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    res = evaluate_exp(num1, num2)

    print(
        "Calling evaluate_exp with two arguments",
        num1,
        "and",
        num2,
        "and return",
        res
    )

    myCalcObj = MathCalculation.Calculation()

    print("\nData attributes of object myCalcObj")
    myCalcObj.printCalculation()

    print(myCalcObj.do_Addition())
    print(myCalcObj.do_Subtraction())
    print(myCalcObj.do_Multiplication())
    print(myCalcObj.do_Division())

    print("\nChange data attributes of object myCalcObj")

    myCalcObj.x = 5
    myCalcObj.y = 10

    myCalcObj.printCalculation()


main()