#!/usr/bin/python3
"""Solution for minimum operations"""


def minOperations(n: int) -> int:
    """Minimum number of operations needed to get n H characters"""

    if n <= 1:
        return 0

    len_text = 2
    prev = 1
    op = 2

    while True:
        if n % len_text == 0 and len_text != n:
            prev = len_text
            len_text = len_text * 2
            op += 2
        elif len_text == n:
            break
        else:
            len_text += prev
            op += 1
    return op
