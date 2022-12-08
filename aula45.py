# from itertools import groupby
#
# alunos = [
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Luiz', 'nota': 'C'},
#     {'nome': 'Fabrício', 'nota': 'F'},
#     {'nome': 'José', 'nota': 'B'},
#     {'nome': 'Ronaldo', 'nota': 'D'},
# ]
#
# alunos.sort(key=lambda item: item['nota'])
#
# for d in alunos:
#     print('-=' * 10)
#     for k, v in d.items():
#         print(f'{k} = {v}')
#
# print('-=' * 10)

# from itertools import groupby
#
# alunos = [
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Luiz', 'nota': 'F'},
#     {'nome': 'Fabrício', 'nota': 'F'},
#     {'nome': 'José', 'nota': 'F'},
#     {'nome': 'Ronaldo', 'nota': 'A'},
# ]
#
# ordena = lambda item: item['nota']
#
# alunos.sort(key=ordena)
# alunos_agrupados = groupby(alunos, ordena)
#
# print('-=' * 10)
#
# for grupo, alunos in alunos_agrupados:
#     print(f'Notas: {grupo}')
#     for aluno in alunos:
#         print(aluno['nome'])
#     print('-=' * 10)

from itertools import groupby, tee

alunos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'F'},
    {'nome': 'Fabrício', 'nota': 'F'},
    {'nome': 'José', 'nota': 'F'},
    {'nome': 'Ronaldo', 'nota': 'A'},
]

ordena = lambda item: item['nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for grupo, alunos in alunos_agrupados:
    novos_alunos1, novos_alunos2 = tee(alunos)

    print(f'Notas: {grupo}')

    for aluno in novos_alunos1:
        print(aluno['nome'])

    quantidade = len(list(novos_alunos2))

    print(f'{quantidade} alunos tiraram {grupo}')
    print()
