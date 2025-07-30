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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
