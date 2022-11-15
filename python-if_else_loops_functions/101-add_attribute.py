#!/usr/bin/python3
""" new attribute """


def add_attribute(obj, name, value):
    """ can't add new attribute """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
