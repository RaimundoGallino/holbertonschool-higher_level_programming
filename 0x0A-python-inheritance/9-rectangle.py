#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """define BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) != str:
            raise TypeError("name must be a string")
        self.value = value
        self.name = name


class Rectangle(BaseGeometry):
    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)
