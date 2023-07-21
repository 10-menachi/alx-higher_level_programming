#!/usr/bin/python3
"""
This module contains the class Base
"""

import json


class Base:
    """
    This is the base class of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor for the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string
        representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file.
        """
        file_name = cls.__name__ + ".txt"
        with open(file_name, "w") as file:
            for obj in list_objs:
                file.write(str(obj) + "\n")

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string representation
        json_string
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of list_objs
        to a file
        """

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                file.write(cls.to_json_string([obj.to_dictionary()
                                               for obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances
        """

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                return [cls.create(**obj) for obj in cls.from_json_string(
                    file.read())]
        except FileNotFoundError:
            return []
