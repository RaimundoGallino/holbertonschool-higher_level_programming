#!/usr/bin/python3
'''file that defines the Base class'''

import json

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
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """define integer_validator method"""

        name = str(cls.__name__) + ".json"
        list = []

        with open(name, "w", encoding="utf-8") as f:
            if list_objs is not None:
                for i in list_objs:
                    list.append(cls.to_json_string(i))
                f.write(cls.to_json_string(list))
            else:
                f.write(cls.to_json_string(list))

    # @staticmethod
    # def from_json_string(json_string):

