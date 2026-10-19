# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: StockProject

# Input:
# Product_Price

# Constants:
# DISCOUNT_RATE = 15%
# TAX_RATE = 6.75%

# Processing:
# Discount_Amount = Product_Price * DISCOUNT_RATE
# Price_After_Discount = Product_Price - Discount_Amount
# Tax_Amount = Price_After_Discount * TAX_RATE
# Total_Price = Price_After_Discount + Tax_Amount

# Output:
# Product_Price, Discount_Amount, Tax_Amount, Total_Price


def main():

    # Define constant rates
    DISCOUNT_RATE = 0.15
    TAX_RATE = 0.0675

    # Display the program title
    print("\n\tStock Product Bill\n")

    # Get the product price from the user
    Product_Price = float(input("Enter the product Price: "))

    # Calculate the discount amount
    Discount_Amount = Product_Price * DISCOUNT_RATE

    # Calculate the price after discount
    Price_After_Discount = Product_Price - Discount_Amount

    # Calculate the tax amount after discount
    Tax_Amount = Price_After_Discount * TAX_RATE

    # Calculate the total price
    Total_Price = Price_After_Discount + Tax_Amount

    # Display values using default formatting
    print("\n\tThe Total of due Payment of the product (By default) is",
          Total_Price, "$")

    print("\tProduct Price =", Product_Price, "$")
    print("\tDiscount Amount =", Discount_Amount, "$")
    print("\tTax Amount =", Tax_Amount, "$")

    # Display values with two decimal places
    print("\n\tThe Total of due Payment of the product (with precision) is",
          format(Total_Price, ".2f"), "$")

    print("\tProduct Price =", format(Product_Price, ".2f"), "$")
    print("\tDiscount Amount =", format(Discount_Amount, ".2f"), "$")
    print("\tTax Amount =", format(Tax_Amount, ".2f"), "$")

    print("\n\tThank you for Doing Business With Us!")


# Call the main function
main()