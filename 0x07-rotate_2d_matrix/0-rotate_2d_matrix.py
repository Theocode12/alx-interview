#!/usr/bin/python3
"""
A module that rotates a 2D nxn Matrix
"""


def rotate_column(matrix, i: int, j: int, ls_of_sizes) -> None:
    """Moves the column in a circle. More docs to come"""
    len_mat = len(matrix) - 1
    current_row = matrix[i][j]
    tmp_i, tmp_j = i, j

    for rot in range(4):
        if rot == 0:
            i = j
            next_row = matrix[i][ls_of_sizes[1]]
            matrix[i][ls_of_sizes[1]] = current_row
        elif rot == 1:
            j = len_mat - ls_of_sizes[0] - (j - ls_of_sizes[0])
            next_row = matrix[ls_of_sizes[2]][j]
            matrix[ls_of_sizes[2]][j] = current_row
        elif rot == 2:
            i = len_mat - ls_of_sizes[0] - (ls_of_sizes[1] - j)
            next_row = matrix[i][ls_of_sizes[3]]
            matrix[i][ls_of_sizes[3]] = current_row
        else:
            matrix[tmp_i][tmp_j] = current_row
        current_row = next_row


def rotate_full_row(matrix, i: int, j: int, ls_sizes) -> None:
    """Rotates a row 90 degs. More docs to come"""
    iteration = get_number_of_iterations(len(matrix), i)
    for row in range(iteration):
        rotate_column(matrix, i, j, ls_sizes)
        j += 1


def get_number_of_iterations(mat_len: int, i: int):
    """Returns the number of iterations for a given diagonal i"""
    return mat_len - i * 2 - 1


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D nxn Matrix in Place
    Returns:
        None
    """
    i = j = 0
    n = len(matrix)
    for diag in range(int(len(matrix) / 2)):
        rotate_full_row(matrix, i, j, [i, n - 1 - i, n - 1 - i, i])
        i += 1
        j += 1
