#!/usr/bin/python3
"""This module provides a function to add two integers or floats.

The function ensures the inputs are integers or floats,
casts them to integers, and returns their sum.
"""

def add_integer(a, b=98):
    """Add two integers or floats (casted to integers).

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        int: The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
