#!/usr/bin/python3
import hidden_4
lst = dir(hidden_4)

for module in lst:
    if module[:2] != '__':
        print(module)
