#!/usr/bin/python3
"""This module defines a class named Square.

"""


class Square:
    """This class represent a square by: (based on 3-square.py)

    """
    def __init__(self, size=0):
        """Initialize the Square instance with a size."""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method to set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
