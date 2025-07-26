#!/usr/bin/python3
"""This module provides a function to add two integers or floats.

The `add_integer` function takes two numbers (integers or floats),
casts them to integers, and returns their sum.
"""

def add_integer(a, b=98):
    """Add two integers or floats (casted to integers)."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
