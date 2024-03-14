#!/usr/bin/python3
# Import the file
import hidden_4
"""
print_hidden_name - Function to print all the hidden module

Args:
Doest not take any arguments

Return:
No value to be return
"""


def print_hidden_name():
    module_names = dir(hidden_4)
    fi_nam = sorted(name for name in module_names if not name.startswith('__'))

    for name in fi_nam:
        print(name)


if __name__ == "__main__":
    print_hidden_name()
