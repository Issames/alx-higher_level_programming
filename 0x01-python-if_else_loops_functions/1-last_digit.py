#!/usr/bin/python3
import random

def get_randn():
    num = random.randint(-10000,10000)
    return num

def get_last_digit(num):
    if num >= 0:
        return num % 10
    else:
        if (num % 10) != 0:
            return -10 + (num % 10)
        else:
            return 0



def print_last_digit(num):
    print('Last digit of {:d} is {:d}'.format(number, last_digit), end=" ")
    if last_digit > 5:
        print('{}'.format('and is greater than 5'))
    elif last_digit == 0:
        print('{}'.format('and is 0'))
    elif last_digit < 6 and last_digit != 0:
        print('{}'.format('and is less than 6 and not 0'))


if __name__ = '__main__':
    num = get_randn()
    last_digit = get_last_digit(num)
    print_last_digit(last_digit)
