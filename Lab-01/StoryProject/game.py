# Lab 1: Introduction to Programming in Python
# Author: Nafiseh Khosravi Rad
# Project: StoryProject

# Input:
# Name, Forest, City, DogName, Adventure, Princess

# Processing:
# Insert the user's input into the story

# Output:
# Display the completed story


def main():

    # Display the program title
    print("\n\tThe Great Story Ever\n")

    # Get information from the user
    Name = input("Enter your Name: ")
    Forest = input("Enter the name of the Forest: ")
    City = input("Enter the name of your City: ")
    DogName = input("Enter the name of the dog: ")
    Adventure = input("Enter your Type of Adventure: ")
    Princess = input("Enter the name of Princess: ")

    # Display the completed story
    print("\n\tThere once was a person named", Name, "who lived in", City + ".")
    print(Name, "went to explore the", Forest, "in", City + ".")
    print(Name, "who loves", Adventure, "adventure was accompanied")
    print("with his beloved dog", DogName, "and went to rescue the", Princess,
          "who ventured into the", Forest, "without her guards.")
    print(Name, "risked his life as he faced pirates who imprisoned the", Princess + ".")
    print("Then,", Name, "rescued her after long fight against the pirates.")
    print(Name, "married the", Princess + ".")
    print("They both lived happily ever after!")


# Call the main function
main()