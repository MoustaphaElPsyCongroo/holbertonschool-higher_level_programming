#!/usr/bin/python3
def print_last_digit(number):
    "Prints the last digit of a number"
    if number < 0:
        lastdigit = (number * -1) % 10
    else:
        lastdigit = number % 10

    print(lastdigit, end='')

    return lastdigit