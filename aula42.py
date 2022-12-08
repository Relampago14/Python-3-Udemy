from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Mário Campos', 'Rio de Janeiro', 'Piracicaba']

estados = ['SP', 'MG', 'RJ']

cidades_estados = zip(indice, estados, cidades)

for indice, estados, cidades in cidades_estados:
    print(indice+1, estados, cidades)
