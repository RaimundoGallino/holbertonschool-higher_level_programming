#!/usr/bin/python3
'''file that defines the square class'''


class Square:

    '''define the square class'''
    def __init__(self, size=0, position=(0, 0)):
        '''__init__ function'''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = 0
        self.__size = size
        self.__position = 0
        self.__position = position

    def area(self):
        '''defines the area of the square'''
        return self.__size **2

    @property
    def size(self):
        '''gets the size of the square'''
        return self.__size
    @property
    def position(self):
        '''gets the position of the spaces in the square'''
        return self.position

    @position.setter
    def position(self, value):
        '''sets the position value'''
        if isinstance(value, tuple) is True:
            if len(value) != 2:
                if isinstance(value[0], value[1], int) is True:
                    if (value[1] > 0 and value[2] > 0):
                        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print()
