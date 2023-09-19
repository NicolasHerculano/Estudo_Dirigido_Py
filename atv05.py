import numpy as np
matriz = np.full([10, 10], 1)
matrizSuperior = np.triu(matriz, k=0)
print(matrizSuperior)