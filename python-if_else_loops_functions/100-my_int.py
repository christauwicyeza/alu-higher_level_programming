#!/usr/bin/python3
"""Rebel Myint"""


class MyInt(int):
    """Rebel Myint class"""

    def __eq__(self, other):
        """not equal when =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """equal when !="""
        return super().__eq__(other)
