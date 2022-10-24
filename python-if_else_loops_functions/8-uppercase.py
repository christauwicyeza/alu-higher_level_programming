#!/usr/bin/python3
le = -32


def uppercase(stru):
    i = 0
    while i < len(stru):
        if islower(stru[i]):
            la = ord(stru[i]) + offset
            li = chr(la)
        else:
            li = stru[i]
        print("{}".format(li), end='')
        i = i + 1
    print("")


def islower(strs):
    value = ord(strs)
    if value >= 97 and value <= 122:
        return True
    else:
        return False
        