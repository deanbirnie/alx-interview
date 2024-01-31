#!/usr/bin/python3
"""
module used to determine fewest number of coins needed to meet
a given amount.
"""


def makeChange(coins, total):
    """
    Method to determine the fewest coins needed to make up the
    value of total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_used = 0

    for coin in coins:
        while total != 0 and total > 0:
            total -= coin
            coins_used += 1
        if total < 0:
            total += coin
            coins_used -= 1
        else:
            return coins_used

    return -1
