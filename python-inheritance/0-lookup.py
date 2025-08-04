#!/usr/bin/python3
"""this function will returns the list of available attributes and methods of an object"""


def lookup(obj):
    """returns a list of obj"""
    return dir(obj)
