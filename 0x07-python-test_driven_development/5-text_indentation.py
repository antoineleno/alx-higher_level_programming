#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """
    text_indentation: Function that prints a text
        Args:
            text (string): text to be printed
        Raises:
            TypeError: if text not a string
        Return:
            No value to be returned
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    punctuation = {'.', '?', ':'}

    for char in text:
        result += char
        if char in punctuation:
            result += '\n\n'

    lines = result.split('\n')
    lines = [line.strip() for line in lines]
    print('\n'.join(lines))
