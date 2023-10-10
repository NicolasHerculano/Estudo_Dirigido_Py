import math
n = 0
def fatorial (n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
    return n * fatorial(n - 1)

def fatorial_for(n):
    fat = 1
    for i in range(1, n):
        fat = fat * i

    return fat * n

def fatorial_while(n):
    i = 1
    fat = 1
    while i < n:
        fat = fat * i
        i += 1
    return fat * n

opcao = 0
while opcao != 5:
    opcao = int(input('\n1 - Calcular fatorial (Função Predefinida)'
                      '\n2 - Calcular fatorial (Função Recursiva)'
                      '\n3 - Calcular fatorial (For in range)'
                      '\n4 - Calcular fatorial (While)'
                      '\n5 - Sair\n'))

    match opcao:
        case 1:
            n = int(input('Digite um número: '))
            print(math.factorial(n))
        case 2:
            print(fatorial(n = int(input('Digite um número: '))))
        case 3:
            print(fatorial_for(n = int(input('Digite um número: '))))
        case 4:
            print(fatorial_while(n = int(input('Digite um número: '))))
        case 5:
            exit()
        case _:
            opcao = int(input('\n1 - Calcular fatorial (Função Predefinida)'
                              '\n2 - Calcular fatorial (Função Recursiva)'
                              '\n3 - Calcular fatorial (For in range)'
                              '\n4 - Calcular fatorial (While)'
                              '\n5 - Sair\n'))