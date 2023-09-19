import numpy as np
matriz = np.full([10, 10], 1)
matrizInferior = np.tril(matriz, k=0)
print(matrizInferior)