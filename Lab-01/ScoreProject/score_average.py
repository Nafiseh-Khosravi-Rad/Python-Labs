# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: ScoreProject

# Input:
# Test_Score1, Test_Score2, Test_Score3

# Processing:
# Average_Score = (Test_Score1 + Test_Score2 + Test_Score3) / 3

# Output:
# Test_Score1, Test_Score2, Test_Score3, Average_Score


def main():

    # Display the program title
    print("\n\tThe Test Score\n")

    # Get three test scores from the user
    Test_Score1 = float(input("Enter your First Test Score: "))
    Test_Score2 = float(input("Enter your Second Test Score: "))
    Test_Score3 = float(input("Enter your Third Test Score: "))

    # Calculate the average score
    Average_Score = (Test_Score1 + Test_Score2 + Test_Score3) / 3

    # Display the average using default formatting
    print("\n\tThe Corresponding Average Test Score (By default) is",
          Average_Score)

    print("\tTest Score 1 =", Test_Score1)
    print("\tTest Score 2 =", Test_Score2)
    print("\tTest Score 3 =", Test_Score3)

    # Display the average with two decimal places
    print("\n\tThe Corresponding Average Test Score (with precision) is",
          format(Average_Score, ".2f"))

    print("\tTest Score 1 =", Test_Score1)
    print("\tTest Score 2 =", Test_Score2)
    print("\tTest Score 3 =", Test_Score3)


# Call the main function
main()