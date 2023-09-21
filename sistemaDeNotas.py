matriz = []
opcao = 0

for linha in range(11):
    matriz = matriz + [[0] * 11]

linha = 0
coluna = 0
while linha < 11:

    coluna = 0
    while coluna < 5:

        print(format(matriz[linha][coluna]), end = '    ')
        coluna += 1

    print()
    linha += 1

while opcao != 4:

    if opcao < 1 or opcao > 4:

        opcao = int(input('Digite apenas valores permitidos!\n'))

    opcao = int(input('1 - Inserir nota\n'
                      '2 - Imprimir tabela\n'
                      '3 - Mudar estado do aluno\n'
                      '4 - Sair\n'))
    if opcao == 1:
        linha = int(input('Digite o Aluno que deseja avaliar (1 - 10): '))
        coluna = int(input('Digite o valor obtido na avaliação (1 - 3): '))

        if linha > 10 or linha < 1 or coluna < 1 or coluna > 3:
            print('Digite apenas valores permitidos!\n')
            linha = int(input('Digite o Aluno que deseja avaliar (1 - 10): '))
            coluna = int(input('Digite o valor obtido na avaliação (1 - 3): '))

        matriz[linha][coluna] = float(input('Digite a nota do aluno: '))
