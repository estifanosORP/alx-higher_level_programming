#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers
    """
    tot = 0
    for ind in range(x):
        try:
            print("{:d}".format(my_list[ind]), end="")
            tot += 1
        except (TypeError, ValueError):
            continue
    print("")
    return tot
