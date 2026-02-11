import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        # Store the original data type in an attribute for reconstruction
        child.set('type', type(value).__name__)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Data successfully serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs the Python dictionary with proper types.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        reconstructed_dict = {}

        for child in root:
            value = child.text
            data_type = child.get('type')

            # Handle type conversion based on the stored attribute
            if data_type == 'int':
                reconstructed_dict[child.tag] = int(value)
            elif data_type == 'float':
                reconstructed_dict[child.tag] = float(value)
            elif data_type == 'bool':
                reconstructed_dict[child.tag] = value == 'True'
            else:
                reconstructed_dict[child.tag] = value

        return reconstructed_dict
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
