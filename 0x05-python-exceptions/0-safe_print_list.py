#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    function that prints x number of elements of a list
    """
    try:
        for idx in range(x):
            if idx != x-1:
                print("{}".format(my_list[idx]), end="")
            else:
                print("{}".format(my_list[idx]))

    except IndexError:
        print("")
        return (idx)

    return (idx + 1)
