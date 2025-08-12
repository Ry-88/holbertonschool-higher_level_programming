#!/usr/bin/python3
"""defain a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """return the number of characters written"""

    with open(filename, "w") as file:
        file.write(text)

    return len(text)
