#!/usr/bin/python3
"""matrix_divided : function where a number divides all
    the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divied : matrix
        Args:
            matrix (int, float): matrix
            div (int, float)   : divisor

        Raises:
            TypeError: if an element of matrix is not int or float
                        or if rows are different size
                        or if div isn't an int or float
            Zero division error: if div is equal to zero
        Return:
            The matrix result after the division
    """
    for row in range(len(matrix)):
        for i in range(row):
            if not isinstance(matrix[row][i], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(matrix[row]) != len(matrix[row - 1]):
                raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [list(map(lambda x: round(x/div, 2), row)) for row in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')

