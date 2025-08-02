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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        line = str(self.print_symbol) * self.width
        return "\n".join([line for _ in range(self.height)])

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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.
        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        Returns:
            Rectangle: The bigger rectangle, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
