#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not isinstance(value, int):
            raise ValueError
    except ValueError:
        return False
    else:
        print("{:}".format(value))
        return True
