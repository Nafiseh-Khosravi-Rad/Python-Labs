from pathlib import Path

import math_calculation
from StatisticCalculation import Statistic, ProbabilityCalc


def main():

    print("Math Operation Project")

    # Create Calculation object
    myCalcObj = math_calculation.Calculation()

    print("\nInitial Calculation values:")
    myCalcObj.printCalculation()

    print("Addition =", myCalcObj.do_Add())
    print("Subtraction =", myCalcObj.do_Subtract())
    print("Multiplication =", myCalcObj.do_Multiply())
    print("Division =", myCalcObj.do_Divide())

    # Change Calculation object values
    myCalcObj.x = 5
    myCalcObj.y = 10

    print("\nUpdated Calculation values:")
    myCalcObj.printCalculation()

    print("Addition =", myCalcObj.do_Add())
    print("Subtraction =", myCalcObj.do_Subtract())
    print("Multiplication =", myCalcObj.do_Multiply())
    print("Division =", myCalcObj.do_Divide())

    # Create Statistic object
    myStatObj = Statistic(10, 20)

    print("\nStatistic Object:")
    print("A =", myStatObj.getA())
    print("B =", myStatObj.getB())
    print("Average =", myStatObj.calculateAverage())

    # Create ProbabilityCalc object
    myProbCalcObj = ProbabilityCalc(7, 3, 0.5)

    print("\nProbability Object:")
    print("A =", myProbCalcObj.getA())
    print("B =", myProbCalcObj.getB())
    print("Probability =", myProbCalcObj.getProb())
    print(
        "Probability Percentage =",
        myProbCalcObj.calculateProbability()
    )

    print(myProbCalcObj)

    # Get the current project folder
    project_folder = Path(__file__).parent

    # Store object data in calc.txt
    calc_file = open(project_folder / "calc.txt", "w")

    calc_file.write(
        str(myCalcObj.x) + "\t" +
        str(myCalcObj.y) + "\t" +
        str(myCalcObj.comment) + "\n"
    )

    calc_file.write(
        str(myStatObj.getA()) + "\t" +
        str(myStatObj.getB()) + "\n"
    )

    calc_file.write(
        str(myProbCalcObj.getA()) + "\t" +
        str(myProbCalcObj.getB()) + "\t" +
        str(myProbCalcObj.getProb()) + "\n"
    )

    calc_file.close()

    print("\nData saved in calc.txt")

    # Read data from stat.txt
    print("\nReading from stat.txt file")

    stat_file = open(project_folder / "stat.txt", "r")

    stat_lines = stat_file.readlines()

    for line in stat_lines:
        print(line.strip())

    stat_file.close()


main()