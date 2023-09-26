matriz = []
opcao = 0

for linha in range(11):
    matriz = matriz + [[0.0] * 11]

matriz[0][0] = 'ALUNO'
matriz[1][0] = 'Vitor'
matriz[2][0] = 'Nicko'
matriz[3][0] = 'Vinni'
matriz[4][0] = 'Frodo'
matriz[5][0] = 'Marco'
matriz[6][0] = 'Júlia'
matriz[7][0] = 'Pedro'
matriz[8][0] = 'Maria'
matriz[9][0] = 'Rambo'
matriz[10][0] = 'Paola'

matriz[0][1] = 'Aval1'
matriz[0][2] = 'Aval2'
matriz[0][3] = 'Aval3'
matriz[0][4] = 'Média'

linha = 0
coluna = 0
while linha < 11:

    coluna = 0
    while coluna < 5:

        print(format(matriz[linha][coluna]), end = '    ')
        coluna += 1

    print()
    linha += 1

while opcao != 3:

    if opcao < 1 and opcao != 0 or opcao > 3:

        opcao = int(input('Digite apenas valores permitidos!\n'))

    opcao = int(input('\n\n'
                      '1 - Inserir nota\n'
                      '2 - Imprimir tabela\n'
                      '3 - Sair\n'))
    if opcao == 1:
        linha = int(input('Digite o Aluno que deseja avaliar (1 - 10): '))
        coluna = int(input('Digite o valor obtido na avaliação (1 - 3): '))

        if linha > 10 or linha < 1 or coluna < 1 or coluna > 3:
            print('Digite apenas valores permitidos!\n')
            linha = int(input('Digite o Aluno que deseja avaliar (1 - 10): '))
            coluna = int(input('Digite qual avaliação será lançada (1 - 3): '))

        if matriz[linha][coluna] != 0.0:
            seguranca = input('Tem certeza que deseja sobreescrever a nota anterior?\n'
                              'S/N: ')
            if seguranca == 'S' or seguranca == 's':
                matriz[linha][coluna] = round(float(input('Digite a nota do aluno: ')), 1)
            elif seguranca == 'N' or 'n':
                opcao = 2
            else:
                seguranca = input('Escreva apenas S ou N!\n'
                                  'S/N: ')
        else:
            matriz[linha][coluna] = round(float(input('Digite a nota do aluno: ')), 1)

    if opcao == 2:

        linha = 0
        coluna = 0
        while linha < 11:

            coluna = 0
            while coluna < 5:
                print(format(matriz[linha][coluna]), end='      ')
                coluna += 1

            print()
            linha += 1

    for linha in range(1, 11):
        matriz[linha][4] = (matriz[linha][1] + matriz[linha][2] + matriz[linha][3]) / 3
