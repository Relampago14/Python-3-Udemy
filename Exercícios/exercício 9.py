# Farm de CPF automático kkkk

from random import randint

digitos = list()
soma = list()

# Consulta apenas os 9 primeiros dígitos do input

for num in range(0, 9):
    digitos.append(randint(0, 9))

# Faz a multiplicação dos 9 dígitos de 10 a 2 e depois de 10 dígitos de 11 a 2

for v in range(0, 2):

    tam = len(digitos)

    for pos, n in enumerate(digitos):
        mult = n * (tam + 1)
        tam -= 1
        soma.append(mult)

    digito_novo = 11 - (sum(soma) % 11)

    if digito_novo <= 9:
        digitos.append(digito_novo)
    else:
        digitos.append(0)
    soma.clear()


print('Seu CPF é: ', end='')
for pos, digito in enumerate(digitos):
    print(digito, end='')
    if pos == 2 or pos == 5:
        print('.', end='')
    if pos == 8:
        print('-', end='')
