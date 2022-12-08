def verifica_cnpj(cnpj):
    digitos = list()
    soma = list()
    try:
        for pos, num in enumerate(cnpj[0:12]):
            num = int(num)
            digitos.append(num)

        for c in range(0, 2):
            fator_1 = 5
            fator_2 = 9
            if c == 1:
                fator_1 += 1
                for pos, digito in enumerate(digitos):
                    if pos+1 < 6:
                        mult = fator_1 * digito
                        fator_1 -= 1
                        soma.append(mult)
                    if pos+1 >= 6:
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
            verifica_digito(digitos, digito_novo, soma)

        trava = False
        sequencia = False

        for pos, digito in enumerate(digitos):
            if str(digito) == cnpj[pos]:

                if str(digito) * 14 == cnpj:
                    sequencia = True
                    print('Erro! CNPJ é uma sequência.')
                    break

                continue
            print('Erro! seu CNPJ é inválido.')

            trava = True
            break
        if not trava and not sequencia:
            print('CNPJ válido.')

    except (ValueError, TypeError, IndexError):
        print('Por favor, digite um CNPJ válido.')


def verifica_digito(digitos_lista, digito, soma_lista):
    if digito > 9:
        digito = 0
    digitos_lista.append(digito)
    soma_lista.clear()
