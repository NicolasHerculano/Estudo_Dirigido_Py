import numpy as np

diagonalSecundaria = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
matriz = np.diag(diagonalSecundaria, 0)

matrizInvertida = np.flipud(matriz)
print(matrizInvertida)