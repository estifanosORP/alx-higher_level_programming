#!/usr/bin/python3

if __name__ == '__main__':
    for num in range(0, 100):
        if num < 99:
            print("{:02d}".format(num), end=', ')
        elif num == 99:
            print(num)
