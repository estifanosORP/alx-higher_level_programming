#!/usr/bin/python3

def safe_function(fct, *args):
    """
    function that excutes another function safely
    """
    import sys
    try:
        return fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
