#!/usr/bin/python
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    tuple_result = 1
    diviser = 0

    for i in range(len(my_list)):
        a = len(my_list[i]) - 1
        for j in range(0, len(my_list[i])):
            tuple_result *= my_list[i][j]
        diviser += my_list[i][a]
        total += tuple_result
        tuple_result = 1
    return total / diviser
