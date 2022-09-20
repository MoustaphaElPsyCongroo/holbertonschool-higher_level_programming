#!/usr/bin/python3
"""Defines a Square class with private attributes"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Square constructor"""
        self.size = size

    def area(self):
        """Gets the current square area"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for j in range(self.__size):
            for i in range(self.__size):
                if i == self.__size - 1:
                    print("#")
                else:
                    print("#", end="")

    @property
    def size(self):
        """Getter for the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
