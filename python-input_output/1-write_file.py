#!/usr/bin/python3
"""
Module 1-write_file.py
"""


def write_file(filename="", text=""):
    """writes string to text file, returns the number of char"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
