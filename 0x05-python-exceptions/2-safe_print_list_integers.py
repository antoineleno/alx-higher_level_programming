#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                number_printed += 1
        print()
    except ValueError:
        pass
    return number_printed
