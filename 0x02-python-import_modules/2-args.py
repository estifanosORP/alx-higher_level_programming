#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    tot = len(sys.argv)
    if (tot == 2):
        print("{} argument:".format(tot-1))
    else:
        print("{} arguments:".format(tot-1))
    for x in range(tot-1):
        print("{}: {}".format(x+1, sys.argv[x+1]))
