# Lab 3: OOP Classes and Inheritance in Python
# Author: Nafiseh Khosravi Rad
# Project: ShapeProject

from rectangle_shape import Rectangle
from box_shape import Box


def main():

    length_list = []
    width_list = []
    height_list = []

    do_repeat = "y"

    shape_file = open("shape.txt", "w")

    while do_repeat == "y":

        length = float(input("\nEnter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))

        rectangle = Rectangle(length, width)
        box = Box(length, width, height)

        # Apply Polymorphism
        shapes = [rectangle, box]

        print("\nArea using Polymorphism:")

        for shape in shapes:
            print(
                type(shape).__name__,
                "Area =",
                shape.calcArea()
            )

        print("\nRectangle Perimeter =",
              rectangle.calcPerimeter())

        print("Box Volume =",
              box.calcVolume())

        length_list.append(length)
        width_list.append(width)
        height_list.append(height)

        shape_file.write(
            str(length) + "\t" +
            str(width) + "\t" +
            str(height) + "\n"
        )

        do_repeat = input(
            "\nDo you want to enter another shape? (y/n): "
        )

    shape_file.close()

    print("\nLength List:", length_list)
    print("Width List:", width_list)
    print("Height List:", height_list)


main()