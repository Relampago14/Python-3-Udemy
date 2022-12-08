# Minha solução

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = []

cont1 = 0
cont2 = 10
tam = len(string) / 10
tam = int(tam)

for c in range(0, tam):  # Funciona, mas o do professor é mais otimizado
    lista.append(string[cont1:cont2])
    cont1 += 10
    cont2 += 10

print(lista)

for pos, v in enumerate(lista):  # Tbm funciona, porém poderia ter usado o join
    print(v, end='')
    if pos < 9:
        print('.', end='')
print()

# Solução do professor

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

n = 10
comp = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(comp)

print()
print(comp)
print(retorno)
