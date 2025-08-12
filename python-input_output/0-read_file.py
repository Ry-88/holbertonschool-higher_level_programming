#!/usr/bin/python3
"""open and read the content of tile"""


def read_file(filename=""):
    """function to read a file"""

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
