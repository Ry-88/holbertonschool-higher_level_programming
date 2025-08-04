#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """inherit from list"""

    def print_sorted(self):
        """prints the list on ascending sort"""
        print(sorted(self))

    def __str__(self):
        """Customize print behavior of your object"""
        return super().__str__()
