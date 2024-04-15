#!/usr/bin/python3
"""BaseGeometroy"""
class  BaseGeometry:
    """BaseGeometry: function that defien an empty class
    """
    def area(self):
        """area: Function to calculate the area

        Raises:
            Exception: exception with the message area() is not implemented
        """        
        raise Exception ("area() is not implemented")
    def integer_validator(self, name, value):
        """integer_validator

        Args:
            name (string): name of the integer
            value (int): value of the name

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to zero
        """        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
