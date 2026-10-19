# Lab 3: OOP Classes and Inheritance in Python
# Author: Nafiseh Khosravi Rad
# Project: CourseProject


class Course:

    def __init__(self, course_no, course_name, max_enrl, credits):
        self.__course_no = course_no
        self.__course_name = course_name
        self.__max_enrl = max_enrl
        self.__credits = credits

    # Getter methods
    def getCourseNo(self):
        return self.__course_no

    def getCourseName(self):
        return self.__course_name

    def getMaxEnrl(self):
        return self.__max_enrl

    def getCredits(self):
        return self.__credits

    # Setter methods
    def setCourseNo(self, course_no):
        self.__course_no = course_no

    def setCourseName(self, course_name):
        self.__course_name = course_name

    def setMaxEnrl(self, max_enrl):
        self.__max_enrl = max_enrl

    def setCredits(self, credits):
        self.__credits = credits

    def CalculateTotalFees(self):
        return self.__max_enrl * 250

    def printCourseInfo(self):
        print(
            self.__course_no,
            "//",
            self.__course_name,
            "//",
            self.__credits,
            "//",
            self.__max_enrl
        )