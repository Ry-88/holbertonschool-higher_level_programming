#!/usr/bin/python3
"""defain a class"""


class BaseGeometry():
    """defain a Public instance method"""

    def area(self):
        """raise an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
