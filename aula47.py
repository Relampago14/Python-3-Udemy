from dados import produtos, pessoas, lista

# nova_lista1 = filter(lambda num: num > 2, lista)
# nova_lista2 = [num for num in lista if num > 2]
#
# print(list(nova_lista1))
# print(nova_lista2)


# def filtro(prod):
#     if prod['preço'] > 40:
#         prod['caro'] = True
#     return True
#
#
# novos_produtos1 = filter(lambda p: p['preço'] > 16, produtos)
# novos_produtos2 = filter(filtro, produtos)
#
# for produto in novos_produtos1:
#     print(produto)
#
# print()
#
# for produto in novos_produtos2:
#     print(produto)


def filtro_idade(idade):
    if idade['idade'] >= 18:
        return True


novas_pessoas = filter(filtro_idade, pessoas)

for pessoa in novas_pessoas:
    print(pessoa)
