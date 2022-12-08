# file = open('arquivo.txt', 'w+')
#
# file.write('Linha1\n')
# file.write('Linha2\n')
# file.write('Linha3\n')
#
# file.seek(0)
# print(file.read())
# print('-=' * 5)
#
# file.seek(0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
#
# print('-=' * 5)
#
# file.seek(0)
# for l in file.readlines():
#     print(l, end='')
#
# file.close()

# try:
#     file = open('arquivo.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     open('arquivo.txt').close()

# with open('arquivo.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())

# with open('arquivo.txt', 'r') as file:
#
#     print(file.read())

# with open('arquivo.txt', 'a+') as file:
#     file.write('Linha 4\n')
#     file.write('Linha 5\n')
#     file.write('Linha 6\n')
#
#     file.seek(0)
#     print(file.read())

# import os
# os.remove('arquivo.txt')

import json

d1 = {
    'Pessoa 1': {
        'nome': 'João',
        'idade': 17,
    },
    'Pessoa 2': {
        'nome': 'Marcos',
        'idade': 18,
    },
    'Pessoa 3': {
        'nome': 'Moreira',
        'idade': 19,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('arquivo.json', 'w+') as file:
    file.write(d1_json)

