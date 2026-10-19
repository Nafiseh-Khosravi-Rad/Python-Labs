class Statistic:

    def __init__(self, valueA, valueB):
        self.__a = valueA
        self.__b = valueB

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def setA(self, valueA):
        self.__a = valueA

    def setB(self, valueB):
        self.__b = valueB

    def calculateAverage(self):
        return (self.getA() + self.getB()) / 2

    def __str__(self):
        return (
            f"The data attributes of the object are: "
            f"{self.getA()} // {self.getB()}"
        )


class ProbabilityCalc(Statistic):

    def __init__(self, valueA, valueB, valueProb):
        super().__init__(valueA, valueB)
        self.__prob = valueProb

    def setProb(self, valueProb):
        self.__prob = valueProb

    def getProb(self):
        return self.__prob

    def calculateProbability(self):
        return self.__prob * 100

    def __str__(self):
        return (
            f"The data attributes of the object are: "
            f"{self.getA()} // {self.getB()} // {self.getProb()}"
        )