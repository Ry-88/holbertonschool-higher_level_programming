#!/usr/bin/python3
"""
This module defines the Rectangle class with width and height,
and includes methods for calculating area and perimeter,
as well as printing the rectangle using `#`.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.
        Args:
            value (int): New width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.
        Args:
            value (int): New height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        using '#' characters.
        Returns:
            str: The visual rectangle, or an empty string if
            width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""

        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a reproducible string representation of the rectangle.

        Returns:
            str: A string like Rectangle(width, height)
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when the instance is deleted.

        Prints a goodbye message.
        """
        print("Bye rectangle...")
