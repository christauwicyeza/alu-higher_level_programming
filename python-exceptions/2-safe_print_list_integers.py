#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z_item = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            z_item += 1
        except(TypeError, ValueError):
            continue
    print()
    return z_item
