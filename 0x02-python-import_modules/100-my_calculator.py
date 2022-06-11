#!/usr/bin/python3

if __name__ == "__main__":
    from calculator import add, sub, mul, div
    from sys import argv, exit

    n_arg = len(argv) - 1
    operators = ['+', '-', '*', '/']

    if (n_arg != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        print("{} {} {} == {}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{} {} {} == {}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{} {} {} == {}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{} {} {} == {}".format(a, op, b, div(a, b)))
