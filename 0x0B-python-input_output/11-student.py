#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


class Student:
    """class definition"""

    def __init__(self, first_name, last_name, age):
        """inicialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """definition to_json function"""
        newjson = {}
        if attrs is None:
            return (self.__dict__)
        else:
            for i in attrs:
                if i in self.__dict__:
                    newjson[i] = self.__dict__[i]
            return newjson

    def reload_from_json(self, json):
        """definition reload_from_json function"""
        for i in json:
            self.__dict__[i] = json[i]
