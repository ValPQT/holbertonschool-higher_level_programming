#!/usr/bin/python3
"""Module containing basic serialization"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python object and save it to a file using pickle.

    This function converts the given Python data structure into a
    binary format using the pickle module and writes it to a file.

    Args:
        data: The Python object to serialize (list, dict, custom object, etc.).
        filename (str): The name of the file where the serialized
                        data will be stored.

    Note:
        The file is opened in binary write mode ('wb').
    """
    with open("filename.pkl", mode="wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a Python object from a pickle file.

    This function reads binary data from a file and reconstructs
    the original Python object using the pickle module.

    Args:
        filename (str): The name of the file containing the
                        serialized data.

    Returns:
        The deserialized Python object.

    Note:
        The file is opened in binary read mode ('rb').
    """
    with open("filename.pkl", mode="rb") as f:
        return pickle.load(f)
