#!/usr/bin/python
def uniq_add(my_list=[]):
    new_list = []
    [new_list.append(x) for x in my_list if x not in new_list]
    result = 0
    for j in range(len(new_list)):
        result += new_list[j]
    return (result)
