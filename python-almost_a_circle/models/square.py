#!/usr/bin/python3
"Square class, subclass of Rectangle"
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square class, subclass of Rectangle"

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        "Getter/setter for size attribute"
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value