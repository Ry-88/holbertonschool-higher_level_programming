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
    if (not isinstance(a, (int, float)) or
        (isinstance(a, float) and
         (a != a or a == float('inf') or a == float('-inf')))):
        raise TypeError("a must be an integer")

    if (not isinstance(b, (int, float)) or
        (isinstance(b, float) and
         (b != b or b == float('inf') or b == float('-inf')))):
        raise TypeError("b must be an integer")

    try:
        a_int = int(a)
    except OverflowError:
        raise TypeError("a must be an integer")
    try:
        b_int = int(b)
    except OverflowError:
        raise TypeError("b must be an integer")

    return a_int + b_int
