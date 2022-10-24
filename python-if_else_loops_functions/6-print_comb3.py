#!/usr/bin/python3
for i in range(0, 10):
    for s in range(i+1, 10):
        if (i != 8) or (s != 9):
            print("{}{}, ".format(i, s), end='')
        else:
            print("{}{}".format(i, s))
