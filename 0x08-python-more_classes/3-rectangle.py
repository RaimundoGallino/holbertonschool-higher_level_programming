#!/usr/bin/python3
'''file that defines the square class'''


class Rectangle:
    '''define the rectangle class'''

    __height = 0
    __width = 0

    def __init__(self, width=0, height=0):
        '''__init__ function'''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''defines the width of the rectangle'''
        return self.__width

    @property
    def height(self):
        '''defines the height of the rectangle'''
        return self.__height

    @width.setter
    def width(self, value):
        '''sets the height of the rectangle'''
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''sets the height of the rectangle'''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        '''returns the perimeter of the rectangle'''
        area = self.__width * self.__height
        therectboy = ""
        for i in range(area):
            therectboy += "#"
            if (i + 1) == area:
                therectboy += ""
            elif (i + 1) % self.__width == 0:
                therectboy += "\n"
        return therectboy
