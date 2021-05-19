#!/usr/bin/python3
'''file that defines the square class'''


class Square:
    '''define the square class'''
    def __init__(self, size):
        '''__init__ function'''
        if (size < 0):
            raise ValueError("size must be >= 0")
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        self.__size = 0
        self.__size = size
