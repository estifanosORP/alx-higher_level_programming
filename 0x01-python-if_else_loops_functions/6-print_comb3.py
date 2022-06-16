#!/usr/bin/python3

if __name__ == '__main__':
    for num1 in range(0, 10):
        for num2 in range(num1+1, 10):
            if (num1 != num2) and not(num1 == 8 and num2 == 9):
                print('{}{}'.format(num1, num2), end=', ')
            elif (num1 == 8 and num2 == 9):
                print('{}{}'.format(num1, num2))
