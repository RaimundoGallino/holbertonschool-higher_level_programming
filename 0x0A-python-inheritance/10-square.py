#!/usr/bin/python3
"""
class BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)
