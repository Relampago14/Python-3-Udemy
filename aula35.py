# d1 = {'chave1': 'valor1'}
# d1['chave2'] = 'valor2'
#
# print(d1['chave1'])

# d1 = dict(chave1='valor1', chave2='valor2')
# d1['chave3'] = 'valor3'
#
# print(d1)

# d1 = {'chave1': 'valor1', 'chave1': 'valor1', 'chave1': 'valor real'}
#
# print(d1)

# d1 = {'str': 'valor1', 123: 'valor2', (1, 2, 3): 'valor3'}
#
# print(d1)
# print(d1[1, 2, 3])
#
# d1['nao existe'] = 'valor4'
#
# if 'nao existe' in d1:
#     print(d1['nao existe'])
#
# print('Vasco')

# d1 = {'str': 'valor1', 123: 'valor2', (1, 2, 3): 'valor3'}
#
# d1['nomedachave'] = 'valor4'
#
# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))
#
# print('Vasco')

# d1 = {'str': 'valor1', 123: 'valor2', (1, 2, 3): 'valor3'}
#
# d1.update({'novachave': 'valor4'})
# del d1['str']
#
# print(d1)

# d1 = {'str': 'valor1', 123: 'valor2', (1, 2, 3): 'valor3'}
#
# print('str' in d1.keys())
# print('valor1' in d1.values())
# print(len(d1))

# d1 = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
#
# for k, v in d1.items():
#     print(k, v)

# clientes = {'cliente1': {'nome': 'João Marcos'}, 'cliente2': {'nome': 'Moreira Laudares'}}
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# d1 = {'valor1': 'a', 'valor2': 'b', 'valor3': 'c'}
# v = d1.copy()
# v['valor1'] = 'João'
#
# print(d1)
# print(v)

# import copy
#
# d1 = {'valor1': 'a', 'valor2': 'b', 'valor3': 'c', 'valor4': ['João', 'Marcos']}
# v = copy.deepcopy(d1)
#
# v['valor1'] = 'João'
# v['valor4'][0] = 'Joãozinho'
#
# print(d1)
# print(v)

lista = [['c1', 1], ['c2', 2], ['c3', 3]]

print(dict(lista))
