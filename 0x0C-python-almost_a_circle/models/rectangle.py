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
        self.__x, self.__y, self.__width, self.__height)

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

    def update(self, *args, **kwargs):
        '''updates the values of the updates'''
        lenght_a = len(args)

        if args is not None and lenght_a != 0:

            if lenght_a >= 1:
                self.id = args[0]
            if lenght_a >= 2:
                self.__width = args[1]
            if lenght_a >= 3:
                self.__height = args[2]
            if lenght_a >= 4:
                self.__x = args[3]
            if lenght_a == 5:
                self.__y = args[4]

        elif kwargs is not None and lenght_a == 0:

            for key, value in kwargs.items():

                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        '''updates the values of the updates'''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
         'height': self.__height, 'width': self.__width}
