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
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                return False
    return True


def primeSieve(upperLim):
    """
    Helper to pre-calculate all primes up to the max number in an array
    """
    primes = [num for num in range(2, upperLim + 1) if isPrime(num)]
    return primes


def isWinner(x, nums):
    """
    Iterate through nums array to determine who the winner
    of each game will be.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(min(x, len(nums))):
        primes = primeSieve(nums[i])
        moves = len(primes)

        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
