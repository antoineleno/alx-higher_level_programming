#!/usr/bin/python
def multiply_by_2(a_dictionary):
    copy_of_dic = {}
    copy_of_dic = a_dictionary.copy()
    for key, value in copy_of_dic.items():
        copy_of_dic[key] = copy_of_dic[key] * 2
    return (copy_of_dic)
