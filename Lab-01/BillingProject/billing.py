# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: BillingProject

# Input:
# Prd_Price, Prd_Qty

# Constants:
# STATE_TAX = 6.875%
# LOCAL_TAX = 1.0%

# Processing:
# tot_Bill = (Prd_Price * Prd_Qty) \
#            + (Prd_Price * Prd_Qty) * STATE_TAX \
#            + (Prd_Price * Prd_Qty) * LOCAL_TAX

# Output:
# tot_Bill


def main():

    # Define constant tax rates
    STATE_TAX = 0.06875
    LOCAL_TAX = 0.01

    # Display the program title
    print("\n\tThe Billing System\n")

    # Get product price and quantity from the user
    Prd_Price = float(input("Enter your Product's Price: "))
    Prd_Qty = int(input("Enter your Product's Quantity: "))

    # Calculate the total bill including state and local taxes
    tot_Bill = (Prd_Price * Prd_Qty) + \
               (Prd_Price * Prd_Qty) * STATE_TAX + \
               (Prd_Price * Prd_Qty) * LOCAL_TAX

    # Display the total bill using default formatting
    print("\n\tThe Total of Billing (Display By default) is",
          tot_Bill, "$")

    # Display the total bill with two decimal places
    print("\n\tThe Total of Billing (Display By specifying the precision) is",
          format(tot_Bill, ".2f"), "$")


# Call the main function
main()