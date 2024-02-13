#!/usr/bin/python3
"""
Module to calculate the winners for each game in a set of
prime games.
"""


def isPrime(num):
    """
    Determines whether or not a number is prime
    """
    if num < 2:
        return False
    else:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                return False
    return True


def isWinner(x, nums):
    """
    Iterate through nums array to determine who the winner
    of each game will be.
    """
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes_count = sum( 1 for i in range(1, num + 1) if isPrime(i))

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
