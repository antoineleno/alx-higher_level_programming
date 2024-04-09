#!/usr/bin/python3
"""100-matrix_mul"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul: Function to multiply two matrices

    Args:
        m_a: First matrix
        m_b: Second matrix

    Raises:
        TypeError:
            if m_a or m_b is not a list
            if m_a or m_b is not a list of lists
            if m_b or m_b content elements that are not integers or floats
            if m_a and m_b can't be multiplied
    Returns:
        The result of the multiplication of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError(" m_a must be a list of lists")
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError(" m_b must be a list of lists")   
    if len(m_a) == 0 and len(m_a[0]) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0 and len(m_b[0]) == 0:
        raise TypeError("m_b can't be empty")
    
    for i in range(len(m_a)):
        for j in range(len(m_a)):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
            
    for i in range(len(m_b)):
        for j in range(len(m_b)):
            if not isinstance(m_b[i][j], (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    for i in range(1, len(m_a)):
        if len(m_a[i - 1]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(1, len(m_b)):
        if len(m_b[i - 1]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
        
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            row.append(value)
        result.append(row)
    
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/100-matrix_mul.txt')