#!/usr/bin/python
def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary.items())
    for key, value in new_dic:
        print(key, ":", value)
