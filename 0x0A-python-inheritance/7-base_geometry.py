#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """define BaseGeometry class"""

    def area(self):
        """define area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define integer_validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) != str:
            raise TypeError("name must be a string")
        self.value = value
        self.name = name
