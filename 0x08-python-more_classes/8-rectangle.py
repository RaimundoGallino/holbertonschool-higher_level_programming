#!/usr/bin/python3
'''file that defines the square class'''


class Rectangle:
    '''define the rectangle class'''

    __height = 0
    __width = 0
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''__init__ function'''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            therectboy += str(self.print_symbol)
            if (i + 1) == area:
                therectboy += ""
            elif (i + 1) % self.__width == 0:
                therectboy += "\n"
        return therectboy

    def __repr__(self):
        '''returns the string below'''
        return repr("Rectangle " + self.__width + "," + self.__height)

    def __del__(self):
        '''prints the string below when an instance is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        '''prints the string below when an instance is deleted'''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
