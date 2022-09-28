#!/usr/bin/python3
"""
write to a text file
"""


def write_file(filename="", text=""):
    """
    function to write to a text file
    Return: number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
