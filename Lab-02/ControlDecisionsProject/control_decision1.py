def main():
    str = 'Control Decision in Python'
    print(str)

    # Get three numbers from the user
    num1 = int(input("Enter a Number1: "))
    num2 = int(input("Enter a Number2: "))
    num3 = int(input("Enter a Number3: "))

    # Two-way selection
    if num1 == num2 and num3 > 0:
        print('Number ', num1, 'is equal to number ', num2)
        print('Number ', num3, 'is higher than 0')
    else:
        print('Number ', num1, 'is not equal to number ', num2)
        print('Number ', num3, 'is not higher than 0')


main()