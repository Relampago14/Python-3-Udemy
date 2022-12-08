"""frase = 'João Marcos'
tam = len(frase)
cont = 0

while cont < tam:
    print(frase[cont], cont)
    cont += 1

print()
print('Fim')
"""

frase = 'João Marcos'
tam = len(frase)
cont = 0
nova_str = ''

input_usuario = input('Qual a letra você quer que seja maiúscula? ')

while cont < tam:
    letra = frase[cont]

    if letra == input_usuario:
        nova_str += input_usuario.upper()
    else:
        nova_str += letra

    print(nova_str)
    cont += 1

print()
print(nova_str)
