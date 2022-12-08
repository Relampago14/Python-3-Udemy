# Considerando duas listas de inteiros ou floats (lista A e B) some os valores nas listas retornando uma nova lista com
# os valores somados. Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

# Minha resposta 'pythonica'

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

soma = zip(lista_a, lista_b)

for numero in soma:
    numero = list(numero)
    print(f'A soma de {numero[0]} + {numero[1]} = {sum(numero)}')

# Resposta usando list comprehension

print('-=' * 10)

soma2 = zip(lista_a, lista_b)

total = [(n1 + n2) for n1, n2 in soma2]

print(total)  # Fica sem a formatação, mas é mais simples

# Resposta mais 'genérica'

print('-=' * 10)

soma1 = []
for i in range(len(lista_b)):
    soma1.append(lista_a[i] + lista_b[i])
    print(f'A soma de {lista_a[i]} + {lista_b[i]} = {soma1[i]}')

