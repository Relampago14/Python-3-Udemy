from dados import produtos, pessoas, lista

# nova_lista1 = map(lambda num: num * 2, lista)
# nova_lista2 = [num * 2 for num in lista]
# print(list(nova_lista1))
# print(list(nova_lista2))


# def aumento(prod):
#     prod['preço'] = prod['preço'] * 1.05
#     return prod
#
#
# precos = map(aumento, produtos)
# print(produtos)
# for preco in precos:
#     print(preco)


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
