#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    tot = len(sys.argv) - 1
    if (tot == 0):
        print("0 arguments.")
    elif (tot == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(tot))
    for x in range(tot):
        print("{}: {}".format(x+1, sys.argv[x+1]))
