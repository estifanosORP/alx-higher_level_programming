#!/usr/bin/python3

if __name__ == "__main__":
    import random
    number = random.randint(-10000, 10000)

    lst = abs(number) % 10
    if lst > 5:
        print(f"Last digit of {number} is {lst} and is greater than 5")
    elif lst < 6 and lst > 0:
        print(f"Last digit of {number} is {lst} and is less than 6 and not 0")
    elif lst == 0:
        print(f"Last digit of {number} is {lst} and is 0")
