# Verificador de CPF

cpf = input('Insira um CPF: ').replace('.', '').replace('-', '')
digitos = list()
soma = list()

# Consulta apenas os 9 primeiros dígitos do input

for l in cpf[0:9]:
    try:
        l = int(l)
        digitos.append(l)
    except ValueError:
        print()

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

# Confere se o CPF é válido

trava = False
sequencia = False

for pos, digito in enumerate(digitos):
    try:
        if str(digito) == cpf[pos]:
            if str(digito) * 11 == cpf:
                sequencia = True
                print('Erro! CPF é uma sequência.')
                break
            continue
        else:
            print('Erro! CPF inválido.')
            trava = True
            break
    except IndexError:
        print('Erro! Digite um CPF válido.')
        trava = True
        break

if not trava and not sequencia:
    print('Parabéns! CPF válido')
