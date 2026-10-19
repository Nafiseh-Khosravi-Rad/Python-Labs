# Lab 3: OOP Classes and Inheritance in Python
# Author: Nafiseh Khosravi Rad
# Project: MathOperationProject


class Calculation:

    def __init__(self):
        self.x = 0
        self.y = 2
        self.comment = "Calculation"

    def do_Add(self):
        return self.x + self.y

    def do_Subtract(self):
        return self.x - self.y

    def do_Multiply(self):
        return self.x * self.y

    def do_Divide(self):
        return self.x / self.y

    def printCalculation(self):
        print(
            self.x,
            "//",
            self.y,
            "//",
            self.comment
        )