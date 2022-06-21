#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element 2 lists
    """
    division = []

    for i in range(list_length):
        try:
            quotient = my_list_1[i]/my_list_2[i]
            continue
        except TypeError:
            quotient = 0
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
            continue
        except IndexError:
            print("out of range")
            quotient = 0
            continue
        finally:
            division.append(quotient)
    return division
