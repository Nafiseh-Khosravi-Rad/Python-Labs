def main():

    print("Use Python data structures")

    allCalc = [14.98, 98, 100, 1, 9.99]

    allCalcOp = [
        "addition",
        "subtraction",
        "multiplication",
        "division",
        "modulus"
    ]

    allCalc_hashMap = {
        "add": "This is addition operation",
        "sub": "This is subtraction operation",
        "mul": "This is multiplication operation"
    }

    print("\nPrint all elements of allCalc:")

    for i in range(len(allCalc)):
        print(
            "allCalc element",
            allCalc[i],
            allCalcOp[i],
            "at index",
            i
        )

        print(
            "Double value:",
            allCalc[i] * 2
        )

    print("\nPrint all operation names:")

    for i in range(len(allCalcOp)):
        print(
            "Operation:",
            allCalcOp[i],
            "at index",
            i
        )

    print("\nAdd a new value to allCalc")

    new_value = input("Enter new value: ")

    allCalc.append(new_value)

    print("Updated allCalc:", allCalc)

    print("\nHashMap contents:")
    print(allCalc_hashMap)

    print("\nAddition description:")
    print(allCalc_hashMap["add"])

    allCalc_hashMap["div"] = "This is division operation"

    print("\nUpdated HashMap:")
    print(allCalc_hashMap)


main()