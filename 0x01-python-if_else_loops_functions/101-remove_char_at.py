#!/usr/bin/python3

def remove_char_at(str, n):
    cpy = ""
    loc = 0
    for ch in str:
        if loc != n:
            cpy = cpy + ch
        loc += 1

    return (cpy)
