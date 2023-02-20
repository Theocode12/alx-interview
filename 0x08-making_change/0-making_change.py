#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins: list, total: int) -> int:
    """
    Determine the fewest number of coins
    needed to meet a given amount total

    Args ->
        coins: list of coins to meet a given amount total
        total: maximum amount to reach

    Returns ->
        fewest number of coins needed
    """

    current_total = 0
    if total:
        num_of_coins = 0
        while coins:
            max_coin = max(coins)
            min_coin = min(coins)
            if current_total == total:
                return num_of_coins
            elif (max_coin + current_total > total) and (
                min_coin + current_total > total
            ):
                return -1
            elif max_coin + current_total > total:
                coins.pop(coins.index(max_coin))
            else:
                num_of_coins += 1
                current_total += max_coin

        if num_of_coins > 0:
            return -1
    return current_total
