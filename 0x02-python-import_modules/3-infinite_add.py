#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    tot = len(argv)
    sum = 0
    for x in range(1, tot):
        sum += int(argv[x])
    print(sum)
