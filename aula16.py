"""n1 = 10
n2 = 3
divisao = n1 / n2

print(f'{divisao:.2f}')"""

"""nome = 'João Marcos'

print(f'{nome:0<20}')
"""
"""n1 = 20000000000
print(f'{n1:^50.2f}')"""

"""nome = 'João Marcos'
print((50-len(nome)) / 2)

print(f'{nome:#^50}')
"""

"""nome = 'João Marcos'
nome_formatado = '{:@^15}'.format(nome)

print(nome_formatado)
"""

nome = 'João Marcos'
nome = nome.rjust(20, 'u')
print(nome)
