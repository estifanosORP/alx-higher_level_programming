#!/usr/bin/python3

def uppercase(str):
    changed = ""
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            changed = changed + chr(ord(letter) - 32)
        else:
            changed = changed + letter
    print("{}".format(changed))
