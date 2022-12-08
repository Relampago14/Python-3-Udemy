from time import sleep

"""while True:
    nome = input('Digite o seu nome: ')
    print(f'Oi {nome}')

print('Não será executada')
"""

"""x = 0

while x < 10:
    x = x + 1
    print(x)
    sleep(1)

print('Fim')"""

"""x = 0

while x < 10:
    if x == 3:
        x = x + 1
        continue

    x = x + 1
    print(x)
    sleep(1)

print('Fim')"""

"""x = 0

while x < 10:
    if x == 3:
        x += 1
        break

    x = x + 1
    print(x)
    sleep(1)

print('Fim')"""

"""x = 0  # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'{x}, {y}')
        y += 1

    x += 1

print('fim')"""

while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    p = input('Quer continuar? S/N ')

    if p in 'Nn':
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print('Erro! Você não digitou um número. ')
        continue

    n1 = float(n1)
    n2 = float(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '/':
        print(n1 / n2)
    elif operador == '*':
        print(n1 * n2)
    else:
        print('Operador inválido! Tente novamente.')
