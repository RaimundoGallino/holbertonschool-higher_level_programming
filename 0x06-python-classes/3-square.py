#!/usr/bin/python3
'''file that defines the square class'''


class Square:
    '''define the square class'''
    def __init__(self, size=0):
        '''__init__ function'''
        self.__size = 0
        self.__size = size
        if (size < 0):
            raise ValueError("size must be >= 0")
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")

    def area(self):
        '''defines the area of the square'''
        return self.__size **2
