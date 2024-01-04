#!/usr/bin/python3
"""
This module allows us to validate UTF-8 encoded character values.
"""


def validUTF8(data):
    """
    Check the validity of data as a UTF-8 encoded character value.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        if num_bytes == 0:
            while mask1 & byte:
                num_bytes += 1
                byte <<= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

            num_bytes -= 1

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

            num_bytes -= 1

    return num_bytes == 0
