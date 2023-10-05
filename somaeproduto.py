numeros = []

def soma():
    s = 0
    for qtd in range(len(numeros)):
        s = s + numeros[qtd]

    print('Soma = ', s)

def produto():
    p = 1
    for qtd in range(len(numeros)):
        p = p * numeros[qtd]

    print('Produto = ', p)

opcao = 0
while opcao != 6:

    opcao = int(input('Escolha o que deseja fazer:. '
                      '\n1 - Inserir números'
                      '\n2 - Mostrar lista'
                      '\n3 - Excluir lista'
                      '\n4 - Somar'
                      '\n5 - Multiplicar'
                      '\n6 - Sair\n'))
    match opcao:
        case 1:
            tamanho = int(input('Com quantos números deseja trabalhar?\n'))

            for q in range(tamanho):
                n = int(input('Digite os números:.\n'))
                numeros.append(n)
        case 2:
            print(numeros)
        case 3:
            numeros = []
        case 4:
            soma()
        case 5:
            produto()
        case 6:
            exit()