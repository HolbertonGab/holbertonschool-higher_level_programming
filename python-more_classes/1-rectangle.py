#!/usr/bin/python3
"""This module defines a class named Rectangle.

"""


class Rectangle:
    """This class represent a rectangle by: (based on 0-rectangle.py)

    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with width and height."""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method to set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method to set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
