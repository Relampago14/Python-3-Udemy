"""str = 'O brasil é o país do futebol, e só o Brasil é penta'

lista1 = str.split(' ')
lista2 = str.split(',')

for v in lista1:
    print(f'A palavra {v} apareceu {lista1.count(v)} vezes')
    """

"""str = 'O brasil é o o o o o  país do futebol, e só o Brasil é penta'

lista1 = str.split(' ')
lista2 = str.split(',')

palavra = ''
contagem = 0

for v in lista1:
    qtd = lista1.count(v)

    if qtd > contagem:
        contagem = qtd
        palavra = v

print(f'A palavra que apareceu mais vezes foi "{palavra}" {contagem} vezes')"""

"""str = 'O brasil é o o o o o  país do futebol, e só o Brasil é penta'

lista1 = str.split(' ')
lista2 = str.split(',')


for v in lista2:
    print(v.strip().capitalize())
"""

"""str = 'O Brasil é penta'
lista = str.split(' ')
str2 = ' '.join(lista)

print(str)
print(lista)
print(str2)
"""

"""str = 'O Brasil é penta'
lista = str.split(' ')

for pos, v in enumerate(lista):
    print(pos, v, lista[pos])"""

"""lista = [[0, 'João'], [1, 'Marcos'], [2, 'Moreira']]

for pos, v in lista:
    print(pos, v)"""

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista
print(n1, n2, n3)
