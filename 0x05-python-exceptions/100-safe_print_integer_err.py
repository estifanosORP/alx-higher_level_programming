#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    funtion that prints an integer
    """
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
