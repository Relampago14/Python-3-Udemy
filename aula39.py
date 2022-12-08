# lista = [('chave1', 'valor1'), ('chave2', 'valor2')]
#
# d1 = {x: y.upper() for x, y in lista}
#
# print(d1)

# d1 = {x: y for x, y in enumerate(range(5))}
#
# print(d1)

# d1 = {x for x in range(5)}
#
# print(d1, type(set))

d1 = {f'chave_{x}': x**2 for x in range(5)}

print(d1)
