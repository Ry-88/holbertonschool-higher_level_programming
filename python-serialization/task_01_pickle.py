#!/usr/bin/env python3
"""Pickling Custom Classes"""
import json
import pickle


class CustomObject:
    """Class Assignment"""
    def __init__(self, name, age, is_student):
        """create attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print the attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file using pickle.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle and return the instance.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
