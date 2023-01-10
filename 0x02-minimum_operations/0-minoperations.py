#!/usr/bin/python3
"""Solution for minimum operations"""


def minOperations(n: int) -> int:
    """Minimum number of operations needed to get n H characters"""
    text = 'H'
    cp = ''
    pt = ''

    if n < 1:
        return 0

    if isPrime(n):
        return 0

    cp = copy(text)
    text = paste(cp, text)
    op = 2

    while True:
        if n % len(text) == 0 and len(text) != n:
            cp = copy(text)
            text = paste(cp, text)
            op += 2
        elif len(text) == n:
            break
        else:
            text = paste(cp, text)
            op += 1

    return op


def copy(text: str) -> str:
    cp = text[:]
    return cp


def paste(cp: str, text: str) -> str:
    text = text + cp
    return text


def isPrime(N):
    count = 2
    while count ** 2 <= N:
        if N % count == 0:
            return False
        count = count + 1
    return True
