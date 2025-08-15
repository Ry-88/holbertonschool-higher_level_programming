#!/usr/bin/python3
"""defain a class student"""


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""

        return self.__dict__
