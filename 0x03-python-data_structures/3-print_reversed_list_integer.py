#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    i = len(my_list) - 1
    while (i > -1):
        print("{}".format(my_list[i]))
        i -= 1
