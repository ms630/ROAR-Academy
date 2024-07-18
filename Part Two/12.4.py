import numpy as np

def swap_Rows(M, a, b):
    if a >= M.shape[0] or b >= M.shape[0] or a < 0 or b < 0:
        raise IndexError
    M[[a,b], :] = M[[b, a], :]
    print(M)
def swap_Columns(M, a, b):
    if a >= M.shape[0] or b >= M.shape[0] or a < 0 or b < 0:
        raise IndexError
    temp = M[:, a].copy()
    M[:,a] = M[:,b]
    M[:,b] = temp
    M[:, [a, b]] = M[:, [b, a]]
    print(M)

M = np.array([
    [0, 1, 2, 3, 4, 5],
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55]
])

swap_Columns(M, 3, 5)