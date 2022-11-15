#!/usr/bin/python3
"""
Module 2-append_write.py
"""


def append_write(filename="", text=""):
    """write a string to text file, return the number of char"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
