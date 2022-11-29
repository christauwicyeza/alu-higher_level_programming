#!/usr/bin/python3
"""matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """multiply two matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    elif len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    elif len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
    for i in m_a:
        if len(i) < 1:
            raise ValueError("m_a can't be empty")
    for i in m_a:
        for el in i:
            if type(el) != int and type(el) != float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for j in m_b:
        if type(j) != list:
            raise TypeError("m_b must be a list of lists")
    for j in m_b:
        if len(j) < 1:
            raise ValueError("m_b can't be empty")
    for j in m_b:
        for el_2 in j:
            if type(el_2) != int and type(el_2) != float:
                raise TypeError("m_b should contain only integers or floats")
    for j in m_b:
        if len(j) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for n in m_a:
        temp_res = []
        for i in range(len(m_b[0])):
            temp = [j[i] for j in m_b]
            addition = 0
            for k, l in zip(n, temp):
                addition += k * l
            temp_res.append(addition)
        result.append(temp_res)
    return result
