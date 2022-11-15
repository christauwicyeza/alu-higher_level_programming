#!/usr/bin/python3
"""
Module 7-add_item.py
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    loadfile = load_from_json_file( add_item.json )
except FileNotFoundError:
    loadfile = []

save_to_json_file(loadfile + argv[1:], add_item.json )
