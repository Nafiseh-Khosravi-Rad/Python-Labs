# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: EvaluateBookProject

# Input:
# book_Id, book_Author, book_Title, book_Price, book_Isbn, book_Type

# Constants:
# STATE_TAX = 7.5%
# LOCAL_TAX = 1%

# Processing:
# total_Price = book_Price + \
#               (book_Price * STATE_TAX) + \
#               (book_Price * LOCAL_TAX)

# Output:
# total_Price


def main():

    # Define constant tax rates
    STATE_TAX = 0.075
    LOCAL_TAX = 0.01

    # Display the program title
    print("\n\tBook Purchase Evaluation\n")

    # Get book information from the user
    book_Id = input("Enter the Book Id: ")
    book_Author = input("Enter the Book Author: ")
    book_Title = input("Enter the Book Title: ")
    book_Price = float(input("Enter the Book Price: "))
    book_Isbn = input("Enter the Book ISBN: ")
    book_Type = input("Enter the Book Type: ")

    # Calculate the total price
    total_Price = book_Price + \
                  (book_Price * STATE_TAX) + \
                  (book_Price * LOCAL_TAX)

    # Display total price by default
    print("\n\tThe Total price (display by default) for the Book",
          book_Title, "is", total_Price, "$")

    # Display total price with two decimal places
    print("\n\tThe Total price (display with precision) for the Book",
          book_Title, "is", format(total_Price, ".2f"), "$")


# Call the main function
main()