#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defain a class and inherit"""

    def __init__(self, size):
        """Instantiation size"""

        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """return a value of full rectangle"""

        return self.__size * self.__size

    def __str__(self):
        """print description"""

        return (f"[Square] {self.__size}/{self.__size}")
