# Nicolas Herculano Ariston Rodirgues da Silva      Matrícula: 23207279

import math as m

x = 0
y = 0

def soma():
    s = x + y
    return s

def produto():
    p = x * y
    return p

def sencos():
    sc = m.sin(m.radians(x)) + m.cos(m.radians(y))
    return sc

def tg():
    ctg = m.tan(m.radians(x)) + (m.sin(m.radians(y))/m.cos(m.radians(y)))
    return ctg

def raiz():
    r = m.sqrt(x) - m.sqrt(y)
    return r

def impar():
    return [i for i in range(1, x, 2)]

def par():
    return [i for i in range(2, y, 2)]

def hipotenusa():
    soma_catetos = x**2 + y**2
    h = m.sqrt(soma_catetos)
    return h

def potenciacao():
    pot = x ** y
    return pot

opcao = 0
while opcao != 10:
    opcao = int(input('\nCalculadora K3500:.\n\n'
                    '1 - Somar Números\n'
                    '2 - Multiplicar Números\n'
                    '3 - Seno (x) + Cosseno (y)\n'
                    '4 - Tangente (x) + Cotangente (y)\n'
                    '5 - Raiz quadrada de x - Raiz quadrada de y\n'
                    '6 - Números ímpares de 1 a x\n'
                    '7 - Números pares de 2 a y\n'
                    '8 - Hipotenusa, considerando X e Y como catetos de um triângulo retângulo\n'
                    '9 - X elevado a Y\n'
                    '10 - Sair\n'))

    match opcao:
        case 1:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', soma())
        case 2:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', produto())
        case 3:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', sencos())
        case 4:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', tg())
        case 5:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            if x < 0:
                print('x é negativo – não há raiz quadrada de um número negativo sem o uso de números complexos!')
            else:
                print('Resultado: ', raiz())
        case 6:
            x = int(input('Dê um valor a x: '))

            print('Resultado: ', impar())
        case 7:
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', par())
        case 8:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', hipotenusa())
        case 9:
            x = int(input('Dê um valor a x: '))
            y = int(input('Dê um valor a y: '))

            print('Resultado: ', potenciacao())
        case 10:
            exit()