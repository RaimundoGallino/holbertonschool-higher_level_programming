#!/usr/bin/python3
'''file that defines the Base class'''


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

