#!/usr/bin/python3

"""
Module for a function that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ?, and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    split_1 = text.split(".")
    split_1 = [sent.strip()+"." if sent != split_1[-1] else sent.strip()
               for sent in split_1]

    split_2 = [sent.strip().split("?") for sent in split_1]
    split_2 = [sent.strip()+"?" if sent != lst[-1] else sent.strip()
               for lst in split_2 for sent in lst]

    split_3 = [sent.strip().split(":") for sent in split_2]
    split_3 = [sent.strip()+":" if sent != lst[-1] else sent.strip()
               for lst in split_3 for sent in lst]

    for line in split_3:
        if line != split_3[-1]:
            print(line)
            print("")
        else:
            print(line, end="")
