# nome = 'João Marcos'
# iterador = iter(nome)
# gerador = (letra for letra in nome)
#
# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     # print(next(iterador))
#     # print(next(iterador))
#     # print(next(iterador))
# except:
#     pass
#
# print('Sumiu!')
#
# for v in iterador:
#     print(v)

nome = 'João Marcos'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print()
print('Veja bem')

for l in gerador:
    print(l)

print()
print('Veja mal')

for letra in gerador:
    print(letra)
