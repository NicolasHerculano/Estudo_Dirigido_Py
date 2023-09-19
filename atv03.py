import numpy as np

diagonal = np.array([])

tamanho = int(input('Qual tamanho de Matriz você deseja?\n'))

i = 0
while i < tamanho:
    diagonal = np.append(diagonal, 1)
    i += 1

matriz = np.diag(diagonal)
print(matriz)