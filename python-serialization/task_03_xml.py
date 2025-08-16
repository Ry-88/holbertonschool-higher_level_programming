#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML from a file into a Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            text = child.text

            if text is None:
                dictionary[child.tag] = None
            elif text.isdigit():
                dictionary[child.tag] = int(text)
            elif text.lower() == "true":
                dictionary[child.tag] = True
            elif text.lower() == "false":
                dictionary[child.tag] = False
            else:
                dictionary[child.tag] = text

        return dictionary
    except Exception:
        return None
