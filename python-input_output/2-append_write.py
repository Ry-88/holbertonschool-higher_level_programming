#!/usr/bin/python3
"""defain a function that appends
a string at the end of a text file"""


def append_write(filename="", text=""):
    """return the number of characters written"""

    with open(filename, "a") as file:
        file.write(text)

    return len(text)
