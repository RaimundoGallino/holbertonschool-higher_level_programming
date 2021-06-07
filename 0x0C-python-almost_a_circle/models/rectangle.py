#!/usr/bin/python3
'''file that defines the Rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''define the Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("x", x)
        self.__x = x
        self.integer_validator("y", y)
        self.__y = y

        self.id = id

        super().__init__(id)

    @property
    def x(self):
        '''gets the width of the square'''

        return self.__x

    @x.setter
    def x(self, x):
        '''sets the x'''
        self.integer_validator("x", x)

        self.__x = x

    @property
    def y(self):
        '''gets the width of the square'''

        return self.__y

    @y.setter
    def y(self, y):
        '''sets the x'''
        self.integer_validator("y", y)

        self.__y = y

    @property
    def width(self):
        '''gets the width of the square'''

        return self.__width

    @width.setter
    def width(self, x):
        '''sets the width'''
        self.integer_validator("width", x)

        self.__width = x

    @property
    def height(self):
        '''gets the width of the square'''

        return self.__height

    @height.setter
    def height(self, y):
        '''sets the y'''
        self.integer_validator("height", y)

        self.__height = y

    def __str__(self):
        '''returns the string below'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
         self.__x, self.__y, self.__height, self.__width)

    def area(self):
        '''retunrs the area value'''
        return self.__height * self.__width

    def display(self):
        '''displays the rectangle'''

        print("\n" * self.__y)
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width, end='')
            print()

        """
        area = Rectangle.area(self)
        rect = ""
        if self.__y != 0:
            rect = "\n" * self.__y
        for i in range(area):
            if (i + 1) % self.__width == 0:
                x_value = self.__x
                if self.__x != 0:
                    rect += " " * x_value
                    x_value = 0
                rect += "#" * self.__width
            if (i + 1) == area:
                rect += ""
            elif (i + 1) % self.__width == 0:
                rect += "\n"

        print(rect)
        """

