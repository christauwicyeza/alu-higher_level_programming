#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    le = len(tuple_a)
    li = len(tuple_b)
    sum1 = (tuple_a[0] if le > 0 else 0) + (tuple_b[0] if li > 0 else 0)
    sum2 = (tuple_a[1] if le > 1 else 0) + (tuple_b[1] if li > 1 else 0)
    return (sum1, sum2)
