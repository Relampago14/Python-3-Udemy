from dados import produtos, pessoas, lista
from functools import reduce

# soma_lista = reduce(lambda acumulador, num: num + acumulador, lista, 0)
#
# print(soma_lista)

# soma_precos = reduce(lambda acumulador, p: p['preço'] + acumulador, produtos, 0)
#
# print(soma_precos / len(produtos))

soma_idades = reduce(lambda acumulador, p: p['idade'] + acumulador, pessoas, 0)
média = soma_idades / len(pessoas)
print(média)
