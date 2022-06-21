#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    function that prints x number of elements of a list
    """
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")

        except IndexError:
            break
    print("")
    return (idx + 1)
