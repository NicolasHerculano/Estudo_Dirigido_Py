c = 0
p = 0

def soma_imposto(custo, porcentagem):

    imposto = (custo * porcentagem) / 100
    soma_final = imposto + custo

    return print('Valor final: R$ ', soma_final)

opcao = 0
while opcao != 3:
    opcao = int(input('\nEscolha uma opção:. '
                      '\n1 - Atribuir/Alterar Valores'
                      '\n2 - Calcular imposto'
                      '\n3 - Sair\n'))
    match opcao:
        case 1:
            c = float(input('\nDigite o custo do produto: '))
            p = float(input('\nDigite a porcentagem imposta: '))
        case 2:
            soma_imposto(c, p)
        case 3:
            exit()
