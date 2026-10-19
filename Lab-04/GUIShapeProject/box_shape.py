# Lab 4: GUI Shape Project
# Author: Nafiseh Khosravi Rad
# Project: GUIShapeProject

from rectangle_shape import Rectangle


class Box(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.__height = height

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def calcArea(self):
        length = self.getLength()
        width = self.getWidth()
        height = self.__height

        return (
            2 * (length * width)
            + 2 * (length * height)
            + 2 * (width * height)
        )

    def calcVolume(self):
        return (
            self.getLength()
            * self.getWidth()
            * self.__height
        )