#!/usr/bin/python3
"""write_file: function to write to a file"""


def write_file(filename="", text=""):
    """write_file: Function to write a content to a file

    Args:
        filename (txt): File to write the content.

    Return:
        (int): The number of characters read
    """
    with open(filename, 'w', encoding="utf-8") as file:
        number_of_characters = file.write(text)
        return number_of_characters
