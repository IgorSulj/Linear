import numpy as np


def solve(x, y) -> tuple[int, int]:
    A = np.array([
        [np.sum(x * x), np.sum(x)],
        [np.sum(x), x.size], 
    ], dtype=np.double)

    b_vector = np.array([np.sum(x * y), np.sum(y)])

    a, b = np.linalg.matrix_power(A, -1) @ b_vector
    return a, b

x = np.array([
    2.32, 2.33, 2.38, 2.41, 2.44, 2.48, 2.51, 2.55, 2.58, 2.6
])
y = np.array([
    427., 430., 440., 444., 448., 455., 460., 462., 465., 466.
])

a, b = solve(x, y)
