#!/usr/bin/python3
'''rotate 2d matrix'''


def rotate_2d_matrix(matrix):
    '''rotate matrix '''
    matrix[:] = [[matrix[x][n] for x in range(len(matrix) - 1, -1, -1)]
                 for n in range(len(matrix))]
