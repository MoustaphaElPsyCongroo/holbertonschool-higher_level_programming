#!/usr/bin/python3
"Rectangle class, that inherits from Base"
from models.base import Base


class Rectangle(Base):
    "Rectangle class, subclass of Base"

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    @property
    def width(self):
        "Getter/setter for width"
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "Getter/setter for height"
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "Getter/setter for x"
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "Getter/setter for y"
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "Gets a Rectangle instance's area"
        return self.__width * self.__height

    def display(self):
        "Prints a Rectangle instance"
        if self.area() == 0:
            print("")
        else:
            for a in range(self.__y):
                print("")
            for i in range(self.__height):
                for k in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    if j < self.__width - 1:
                        print("#", end="")
                    else:
                        print("#")

    def update(self, *args, **kwargs):
        "Updates a Rectangle instance"
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    super().__init__(arg)
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif kwargs is not None:
            if "id" in kwargs:
                super().__init__(kwargs["id"])
            for key, value in kwargs.items():
                if key != "id":
                    setattr(self, key, value)

    def to_dictionary(self):
        "Gets the dictionary representation of a Rectangle instance"
        return {key.replace("_Rectangle__", ""): value
                for key, value in self.__dict__.items()}
