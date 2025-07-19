#!/usr/bin/python3
def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("Input must be a single character string")
    return 'a' <= c <= 'z'
