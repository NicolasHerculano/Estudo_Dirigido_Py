import numpy as numpy

matriz = numpy.empty([2, 2])

linha = 0
coluna = 0

print('Empresa:.')
for linha in range(0, 2):
    for coluna in range(0, 2):
        matriz[linha][coluna] = input("\nInsira o salário do Funcionário: ")

for linha in range(0, 2):
    for coluna in range(0, 2):
        print('\nEmpresa', linha + 1, ':\nFuncionário', coluna + 1, ':  R$ ', matriz[linha][coluna])
