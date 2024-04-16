#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """read_file: Function to read the content of a file

    Args:
        filename (txt): File to read its content.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.read()
        print(contents)
