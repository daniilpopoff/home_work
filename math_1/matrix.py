# import numpy as np 
# A = np.matrix('100 2; 45 1')
# A_inv = np.linalg.inv(A)
# print(adj(A))

import numpy as np

# Определите матрицу A
# A = np.array([[2, 3], [1, 4]])

# Вычислите присоединенную матрицу adj(A)
def adjoint(matrix):
    n = matrix.shape[0]  # Размерность квадратной матрицы (число строк)
    adj_matrix = np.zeros_like(matrix)

    for i in range(n):
        for j in range(n):
            # Вычислите кофактор для элемента A[i][j]
            minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * np.linalg.det(minor_matrix)
            adj_matrix[i][j] = cofactor

    return adj_matrix

adj_A = adjoint(A)

print("Присоединенная матрица adj(A):")
print(adj_A)
