#!/usr/bin/python3
# Muhammed Riad

def print_last_digit(number):
    if number < 0:
        final = ((number * -1) % 10)
    elif number > 0:
        final = number % 10
    else:
        final = number
    print("{:d}".format(final), end="")
    return final
