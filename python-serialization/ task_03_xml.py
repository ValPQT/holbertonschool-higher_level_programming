#!/usr/bin/python3
"""Module for XML manipulation"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Function to serialize dictionary into XML"""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Function to deserialize XML file into dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}

    for child in root:
        data[child.tag] = child.text
    return data
