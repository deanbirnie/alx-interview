#!/usr/bin/python3
"""
This module contains a function that calculates the minimum operations
(either `copy all` or `paste`) it would take to print n H where H is a
character typed into a text editor and n is the number of times we're
attempting to input H in the text editor.
"""


def minOperations(n):
    """
    This function calculates the fewest operations required to find n H's.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
