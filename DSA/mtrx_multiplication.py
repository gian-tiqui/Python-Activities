import numpy as np


def multiply():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])

    C = np.array([[], []])

    temp_a = []
    temp_b = []

    for i in range(3):
        temp_a.append(A[0][i])
        temp_b.append(A[1][i])

    print(temp_a)
    print(temp_b)
