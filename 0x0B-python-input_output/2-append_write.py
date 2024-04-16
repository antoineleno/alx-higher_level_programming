#!/usr/bin/python3
"""function to append a content to a file"""


def append_write(filename="", text=""):
    """append_write: Function to append a content to a file

    Args:
        filename (txt): File to write the content.
        text (str): text to append to a file

    Return:
        (int): The number of characters append
    """
    with open(filename, 'a', encoding="utf-8") as file:
        number_of_characters = file.write(text)
        return number_of_characters
