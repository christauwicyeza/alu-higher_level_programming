#!/usr/bin/python3
""" 7-add_item.py """


from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file') \
        .load_from_json_file

    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        data.append(sys.argv[idx])
    save_to_json_file(loadFile, "add_item.json")
 
