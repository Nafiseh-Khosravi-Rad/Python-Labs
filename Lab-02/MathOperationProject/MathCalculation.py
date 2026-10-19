class Calculation:

    def __init__(self):
        self.x = 0
        self.y = 2
        self.comment = "Calculation"

    def do_Addition(self):
        return self.x + self.y

    def do_Subtraction(self):
        return self.x - self.y

    def do_Multiplication(self):
        return self.x * self.y

    def do_Division(self):
        return self.x / self.y

    def printCalculation(self):
        print(self.x, "//", self.y, "//", self.comment)