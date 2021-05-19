#!/usr/bin/python3
'''file that defines the square class'''


class Square:
    '''define the square class'''
    def __init__(self, size=0):
        '''__init__ function'''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
