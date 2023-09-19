def inserir():
    n1 = int(input('Adicione um número à pilha: '))
    return lista01.append(n1)

def excluir():
    return lista01.pop()

def mostrar():
    return print(lista01)


lista01 = []
opcao = 0

while opcao != 4:
    opcao = int(input('O que gostaria de fazer?\n'
                      '1 - Adicionar à pilha\n'
                      '2 - Excluir da pilha\n'
                      '3 - Ver pilha\n\n'
                      '4 - Encerrar\n'))
    match opcao:
        case 1:
            inserir()
        case 2:
            seguraca = int(input('Tem certeza?\n'
                                 '1 = Sim / 2 = Não\n'))
            if seguraca != 1 or 2:
                while seguraca > 2 or seguraca < 1:
                    seguraca = int(input('Tem certeza? DIGITE APENAS 1 OU 2\n'
                                         '1 = Sim / 2 = Não\n'))
                if seguraca == 1:
                    excluir()
                elif seguraca == 2:
                    continue
        case 3:
            mostrar()
