#!/usr/bin/python3
"""open and read the content of tile"""


def read_file(filename=""):
    """function to read a file"""

    with open("my_file_0.txt", "r") as file:
        content = file.read()
        print(content)
