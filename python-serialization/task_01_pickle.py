#!/usr/bin/python3
"""
Module that defines a CustomObject class
with serialization and deserialization capabilities
using the pickle module.
"""


class CustomObject:
    """
    A class representing a custom object with basic attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted manner.
        """
        print(
            f"Name : {self.name}\nAge:{self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.

        Args:
            filename (str): The name of the file where the object
                            will be saved.

        Returns:
            None: Returns None if the file cannot be found.
        """
        import pickle

        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object.
            None: If the file does not exist.
        """
        import pickle

        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
