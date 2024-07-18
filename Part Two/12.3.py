import numpy as np

matrix = np.array([
    [0, 1, 2, 3, 4, 5],
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55]
])

subarray1 = matrix[:, 1]
print(subarray1)
subarray2 = matrix[2::2, ::2]
print(subarray2)
subarray3 = matrix[1, 2:4:1]
print(subarray3)
subarray4 = matrix[2:4:, 4::]
print(subarray4)