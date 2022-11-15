#!/usr/bin/python3
"""This module defines a text file-reading function."""


def read_file(filename=""):
    """Print  contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
