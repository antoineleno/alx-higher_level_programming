#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary.items())
    for key, value in new_dic:
        print("{}: {}".format(key, value))
