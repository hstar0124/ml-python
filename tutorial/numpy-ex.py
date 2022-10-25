import numpy as np

matrix_a = np.asarray([[4, 5, 2],
                       [5, 2, 6],
                       [6, 1, -2]])

matrix_b = np.asarray([[5, 9, 2],
                       [2, 0, 3],
                       [1, -4, 5]])

matrix_c = matrix_a + matrix_b
print(matrix_c)
