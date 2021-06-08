#!/usr/bin/python3
'''file that defines the Rectangle class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """define Square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """define Square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        '''gets the width of the square'''

        return self.width

    @size.setter
    def size(self, value):
        '''sets the x'''

        self.width = value

    def update(self, *args, **kwargs):
        '''sets the x'''

        lenght_a = len(args)

        if args is not None and lenght_a != 0:

            if lenght_a >= 1:
                self.id = args[0]
            if lenght_a >= 2:
                self.size = args[1]
            if lenght_a >= 3:
                self.x = args[2]
            if lenght_a == 4:
                self.y = args[3]

        elif kwargs is not None and lenght_a == 0:

            for key, value in kwargs.items():

                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''updates the values of the updates'''
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
