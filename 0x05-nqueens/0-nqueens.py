#!/usr/bin/python3
"""A module that solves the N-queens Problem"""

from typing import List
import sys


def build_array(n: int) -> List[List[int]]:
    """Builds an array from a given number"""
    array = []
    if n >= 4:
        row = []
        for _ in range(n):
            row.append(0)

        for _ in range(n):
            array.append(row.copy())
    return array


def is_safe(array: List[List[int]], row: int, col: int) -> bool:
    """Checks if a spot on the chessboard is safe"""
    
    # check if the current column doesn't contain any queens
    vert_row = row
    while vert_row >= 0:
        if array[vert_row][col]: return False
        vert_row -= 1
        
    # check if the diagonal to the left contains any queens
    diag_row = row
    diag_col = col
    while diag_row >= 0 and diag_col >= 0:
        if array[diag_row][diag_col]: return False
        diag_row -= 1
        diag_col -= 1
        
    # check if the diagonal to the right contains any queen
    diag_row = row
    diag_col = col
    while diag_row >= 0 and diag_col >= 0 and diag_col <= len(array) - 1:
        if array[diag_row][diag_col]: return False
        diag_row -= 1
        diag_col += 1
        
    return True


def check_solution(array: List[List[int]], row, col):
    """Tries to place the queens where they won't conflict"""
    if row < 4:
        if not array[0][col]:
            array[0][col] = 1
        
        for e_col in range(len(array)):
            # print("Before is safe:", array)
            if is_safe(array, row, e_col):
                array[row][e_col] = 1
                # print("After is safe:", array)
                
                check_solution(array, row + 1, col)
                # print("current_row : {}, About to switch to {}".format(row, row + 1))
                if row == 3:
                    print(array)
    return 'No solution found'


def search_Nqueens(array: List[List[int]], col: int):
    """search for solutions starting from the first column"""
    if col < 4:
        pass
    search_Nqueens(array, col + 1)
    