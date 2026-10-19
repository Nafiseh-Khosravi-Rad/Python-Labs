# Lab 2: Decision Structures, Looping, Functions
# Author: Nafiseh Khosravi Rad
# Project: CurrencyConversionProject

# Input:
# us_Cur

# Processing:
# can_Cur = us_Cur * 1.30
# eur_Cur = us_Cur * 0.86
# yen_Cur = us_Cur * 111.23

# Output:
# can_Cur, eur_Cur, yen_Cur


def calculate_canAmount(us_Cur):
    return us_Cur * 1.30


def calculate_eurAmount(us_Cur):
    return us_Cur * 0.86


def calculate_yenAmount(us_Cur):
    return us_Cur * 111.23


def main():
    print("\nThe Currency Conversion")

    us_Cur = float(input("Enter your amount in US Currency: $US "))

    can_Cur = calculate_canAmount(us_Cur)
    eur_Cur = calculate_eurAmount(us_Cur)
    yen_Cur = calculate_yenAmount(us_Cur)

    print("\nCanadian Dollar =", format(can_Cur, ".2f"), "$CAN")
    print("Euro =", format(eur_Cur, ".2f"), "EURO")
    print("Japanese Yen =", format(yen_Cur, ".2f"), "YEN")


main()