#!/usr/bin/python3
"""
This module demonstrates Abstract Base Classes (ABCs) and duck typing in Python.
"""

from abc import ABCMeta, abstractmethod
import math


class Shape(object):
    """
    Abstract base class for all shapes.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class that implements the Shape interface.
    """

    def __init__(self, radius):
        """
        Initialize the Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class that implements the Shape interface.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape-like object.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    circle = Circle(5)
    shape_info(circle)

    rectangle = Rectangle(4, 6)
    shape_info(rectangle)
