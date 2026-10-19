# Lab 3: OOP Classes and Inheritance in Python
# Author: Nafiseh Khosravi Rad
# Project: ShapeProject

# Input:
# length, width

# Processing:
# perimeter = (length + width) * 2
# area = length * width

# Output:
# perimeter, area


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width

    def calcPerimeter(self):
        return (self.__length + self.__width) * 2

    def calcArea(self):
        return self.__length * self.__width