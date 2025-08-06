#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defain a class"""

    def __init__(self, width, height):
        """Instantiation width and height"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
