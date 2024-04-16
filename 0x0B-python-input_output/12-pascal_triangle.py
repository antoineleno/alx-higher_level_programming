#!/usr/bin/python3
"""12-pascal_triangle"""
def pascal_triangle(n):
    """pascall_tringle

    Args:
        n (int): number of lines

    Returns:
        The matrix representation
    """
    my_triangle = [[]]
    if n <= 0:
        return my_triangle
    else:
        created_list = []
        my_list = [1]
        antoine = []
        for i in range(n):
            if i == 0:
                my_triangle.append([1])
            else:
                if i == 1:
                    created_list = create_list(my_list)
                    my_triangle.append(created_list)
                else:
                    my_list = created_list
                    antoine = create_list(my_list)
                    my_triangle.append(antoine)
                    created_list = antoine
        del my_triangle[0]
        return my_triangle
    


def create_list(my_list):
    """create_list - function to return a new_list

    Args:
        my_list (list): list to create its new copy 

    Returns:
        new list
    """
    my_new_list = []

    for i in range(len(my_list) + 1):
        if i == 0:
            my_new_list.append(1)
        elif i == len(my_list):
            my_new_list.append(1)
        else:
            m = my_list[i] + my_list[i - 1]
            my_new_list.append(m)
    
    return my_new_list

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/12-pascal_triangle.txt')
    