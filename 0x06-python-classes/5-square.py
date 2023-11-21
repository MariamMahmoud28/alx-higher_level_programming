#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The size to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
