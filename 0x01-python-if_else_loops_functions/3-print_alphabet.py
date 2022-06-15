#!/usr/bin/python3

if __name__ == "__main__":
    for ch in range(ord('a'), ord('z')+1):
        if chr(ch) not in ['q', 'e']:
            print("{:c}".format(ch), end='')
