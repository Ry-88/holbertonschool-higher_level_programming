#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """
    defines a class Square
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size

        Args:
            size: The size of the square's
        """
        self.__size = size

    @property
    def size(self):
        """access a method like it's a regular variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """acsses to __size and check
        set a value to __size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
