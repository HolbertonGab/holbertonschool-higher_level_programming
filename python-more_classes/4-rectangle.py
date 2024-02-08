#!/usr/bin/python3
"""This module defines a class named Rectangle.

"""


class Rectangle:
    """This class represent a rectangle by: (based on 3-rectangle.py)

    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with width and height."""
        self.height = height
        self.width = width

    def __str__(self):
        """
        print the Rectangle with the character #

        Returns: a string containing the Rectangle with the character #
        """
        str_rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for y in range(self.__height):
            for x in range(self.__width):
                str_rectangle += '#'
            if y < self.__height - 1:
                str_rectangle += '\n'

        return str_rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle

        Returns: string representation of the rectangle
        """
        repr_rectangle = "Rectangle({:d}, {:d})".format(self.__width,
                                                        self.__height)

        return repr_rectangle

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2
