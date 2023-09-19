import numpy as np

matriz = np.empty([2, 10], dtype=str)

nome = input('Escreva o seu nome: ')
sobrenome = input('Escreva o seu sobrenome: ')

lista01 = list(nome)
lista02 = list(sobrenome)

for i in range(0, len(lista01)):
    matriz[0][i] = lista01[i]

for j in range(0, len(lista02)):
    matriz[1][j] = lista02[j]

for linha in range(0, 2):
    for coluna in range(0, 10):
        print(matriz[linha][coluna], end='')
    print()
