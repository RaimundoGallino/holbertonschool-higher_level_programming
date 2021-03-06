#!/usr/bin/python3
'''file that defines the Base class'''

import json
from os import path


class Base:
    '''define the Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor'''

        Base.__nb_objects += 1

        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """define integer_validator method"""
        if type(name) != str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))
        elif value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """define integer_validator method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """define integer_validator method"""

        name = str(cls.__name__) + ".json"
        list_j = []

        with open(name, "w", encoding="utf-8") as f:
            if list_objs is not None:
                for i in list_objs:
                    list_j.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(list_j))
            else:
                f.write(cls.to_json_string(list_j))

    @staticmethod
    def from_json_string(json_string):
        """define integer_validator method"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a dummy instance"""
        dummy = cls(3, 4) if cls.__name__ == "Rectangle" else cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """create a dummy instance"""
        name = str(cls.__name__) + ".json"
        list_j = []

        if path.exists(name):
            with open(name, 'r', encoding='utf-8') as f:
                content = cls.from_json_string(f.read())
                for obj in content:
                    list_j.append(cls.create(**obj))
                return list_j
        else:
            return list_j
