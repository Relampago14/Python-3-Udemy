def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte(input('Digite um número: ').replace(',', '.').strip().lower())

    if numero is None:
        print('Erro! Você não digitou um número válido.')
    else:
        print(str(numero * 5).replace('.', ','))
