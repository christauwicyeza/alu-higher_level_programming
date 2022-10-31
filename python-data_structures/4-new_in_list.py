#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cp = [item for item in my_list]
    if idx < 0 or idx >= len(my_list):
        return my_list_cp
    my_list_cp[idx] = element
    return my_list_cp
