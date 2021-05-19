#!/usr/bin/python3
'''file that defines the square class'''


class Square:
    '''define the square class'''
    def __init__(self, size):
        '''__init__ function'''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
