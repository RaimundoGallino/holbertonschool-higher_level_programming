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
        self.__size = 0
        self.__size = size

    def area(self):
        '''defines the area of the square'''
        return self.__size**2

    @property
    def size(self):
        '''gets the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the value'''
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''prints a square of the size'''
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end='')
                print()
