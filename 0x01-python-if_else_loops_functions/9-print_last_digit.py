#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ca = number % 10
    else:
        ca = number % -10
        ca *= -1

    print("{:d}".format(ca), end='')
    return (ca)
