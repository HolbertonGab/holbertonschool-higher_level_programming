#!/usr/bin/python3
"""Square class file"""


class Square:
    """
    class Square that defines a square

    Attributes:
        __size: size of a side of the square
    """
    def __init__(self, size=0):
        """
        Init a square

        Args:
            size (int): size of the square

        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        square area

        Returns: the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print the Square in '#' on stdout

        Returns: the size of the Square
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """
        access to size

        Returns: the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        change the size

        args:
            value: value of the new size

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
