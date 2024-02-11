#!/usr/bin/python3
"""This module defines a class named Rectangle.

"""


class Rectangle:
    """This class represent a rectangle by: (based on 8-rectangle.py)

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with width and height."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                str_rectangle += str(self.print_symbol)
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

    def __del__(self):
        """
        delete the instance of Rectangle

        Returns: None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area

        Returns: the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size

        Returns: new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
