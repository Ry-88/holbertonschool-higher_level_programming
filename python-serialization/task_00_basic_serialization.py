#!/usr/bin/env python3
"""Basic Serialization"""
import json


def serialize_and_save_to_file(data, filename):
     """
    Serializes Python object to JSON and saves it into a file.
    """
     with open(filename, "w", encoding="utf-8") as file:
          json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads JSON from file and deserializes it back to a Python object.
    """
    with open(filename, "r", encoding="utf-8") as file:
         return json.load(file)
