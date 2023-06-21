#!/usr/bin/python3
# function that adds 2 integers
"""
    Define 'add_integer' function.
"""

def add_integer(a, b=98):
    """Adds two numbers
    Args:
        a - first number input
        b - second number input

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
