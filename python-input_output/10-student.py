"""
Ce module définit une classe Student qui permet de représenter
un étudiant avec des informations personnelles de base.
"""


class Student:
    """
    Cette classe représente un étudiant avec un prénom,
    un nom et un âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.

        Args:
            first_name (str): le prénom de l'étudiant
            last_name (str): le nom de famille de l'étudiant
            age (int): l'âge de l'étudiant
        """

        self.first_name = first_name

        self.last_name = last_name

        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'objet Student.

        Si attrs est une liste de chaînes de caractères,
        seuls les attributs présents dans cette liste
        seront inclus dans le dictionnaire retourné.
        """

        if isinstance(attrs, list):

            result = {}

            for attr in attrs:

                if hasattr(self, attr):

                    result[attr] = getattr(self, attr)

            return result

        return self.__dict__
