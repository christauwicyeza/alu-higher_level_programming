#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z_item = 0
    while z_item < x:
        try:
            print("{}".format(my_list[z_item]), end='')
        except IndexError:
            break
        z_item += 1
    print()
    return z_item
