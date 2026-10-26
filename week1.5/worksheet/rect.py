# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if type(width) != int:
            raise TypeError("Width must be an integer")

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        if type(height) != int:
            raise TypeError("Height must be an integer")

        if height <= 0:
            raise ValueError("Height must be greater than 0")

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """returns true if rectangle is square or false if it isn't"""
        return self.width == self.height

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of rectangle"""
        return 2 * (self.width + self.height)
        
    # (See README.md for details of what they should do)
