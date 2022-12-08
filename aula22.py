"""texto = 'João'
lista = [1, 2, 3, 4, texto, 'Vasco']

print(lista)
"""

"""lista = ['A', 'B', 'C', 'D', 'E']

lista[1] = 'BATATA'

print(lista[0:3])
"""

"""l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.insert(0, 'a')
l2.append('b')
l1.pop()

print(l2[3])
print(l1)
print(l2)"""

"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del(lista[3:5])

print(lista)
print(max(lista))
print(min(lista))
"""

"""lista = list(range(0, 10))
soma = 0

for v in lista:
    soma = soma + v

print(soma)"""

"""l2 = ['str', True, 10, -20.5]

for v in l2:
    print(f'{v} = {type(v)}')"""

secreta = 'bola'
digitadas = []
chances = 3

while True:
    if chances == 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite letra por letra.')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Você acertou! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Que pena! A letra "{letra}" não está na palavra secreta')
        chances -= 1
        digitadas.pop()

    secreta_temp = ''
    for l in secreta:
        if l in digitadas:
            secreta_temp += l
        else:
            secreta_temp += '*'

    if secreta_temp == secreta:
        print(f'Parabéns! Você ganhou, a palavra era "{secreta}"')
        break
    else:
        print(f'Seu progresso: {secreta_temp}')

    print(f'Ainda restam {chances} chances')
