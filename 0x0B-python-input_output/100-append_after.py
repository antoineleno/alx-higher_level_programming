#!/usr/bin/python3
"""100-append_after"""
def append_after(filename="", search_string="", new_string=""):
    """append_after

    Args:
        filename (file): file to append a content to it.
        search_string (str): substring to search in file.
        new_string (str):  sbustring to append if we find substring
    """
    with open(filename, "r", encoding="utf-8") as file:
        text = ""
        while True:
            line = file.readline()
            if not line:
                break
            if line.find(search_string) != -1:
                text += line
                text += new_string
            else:
                text += line
    with open(filename, "w", encoding="utf-8") as new_file:
        new_file.write(text)
    
