#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """
    defines a class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size

        Args:
            size: The size of the square's
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """access a method like it's a regular variable"""
        return self.__position

    @position.setter
    def position(self, value):
        """acsses and check on __position"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
