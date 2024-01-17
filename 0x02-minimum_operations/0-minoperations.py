#!/usr/bin/python3
"""Minimum Operations to print n times of a letter (H)"""

def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    current = 2

    while current * current <= n:
        while n % current == 0:
            n //= current
            operations += current
        current += 1

    return operations + n if n > 1 else operations
