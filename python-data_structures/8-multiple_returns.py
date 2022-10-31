#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    li = sentence[0] if le > 0 else None
    return (le, li)
