#!/usr/bin/python3
"""
Module 11-square.py
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """inherits from class Rectangle"""

    def __init__(self, size):
        """initialization"""

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """implements area method and return area"""
        return self.__size ** 2

    def __str__(self):
        """return square description: [Square] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(type(self).__name__,
                                         self.__size, self.__size)
