from random import randint


def gera_cnpj():
    digitos = list()
    soma = list()
    for num in range(12):
        digitos.append(randint(0, 9))

    for c in range(0, 2):
        fator_1 = 5
        fator_2 = 9
        if c == 1:
            fator_1 += 1
            for pos, digito in enumerate(digitos):
                if pos + 1 < 6:
                    mult = fator_1 * digito
                    fator_1 -= 1
                    soma.append(mult)
                if pos + 1 >= 6:
                    mult = fator_2 * digito
                    soma.append(mult)
                    fator_2 -= 1
        else:
            for pos, digito in enumerate(digitos):
                if pos + 1 < 5:
                    mult = fator_1 * digito
                    fator_1 -= 1
                    soma.append(mult)
                if pos + 1 >= 5:
                    mult = fator_2 * digito
                    soma.append(mult)
                    fator_2 -= 1

        digito_novo = 11 - (sum(soma) % 11)
        gera_digito_verificador(digitos, digito_novo, soma)
    for pos, digito in enumerate(digitos):
        print(digito, end='')
        if pos == 1 or pos == 4:
            print('.', end='')
        if pos == 7:
            print('/', end='')
        if pos == 11:
            print('-', end='')


def gera_digito_verificador(digitos_lista, digito, soma_lista):
    if digito > 9:
        digito = 0
    digitos_lista.append(digito)
    soma_lista.clear()
