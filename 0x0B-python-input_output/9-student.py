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

    def to_json(self):
        """inicialization of the class"""
        return (self.__dict__)
