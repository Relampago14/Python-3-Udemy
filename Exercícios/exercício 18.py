# Crie um list comprehension que some os valores dos produtos

carrinho = [('Produto 1', 30), ('Produto 2', '20'), ('Produto 3', 10)]

# Não consegui pensar em uma lista comprehension que funcionasse

total1 = 0
for c in range(len(carrinho)):
    total1 += float(carrinho[c][1])

print(total1)

# Resposta do professor

total = sum([float(y) for x, y in carrinho])  # Interessante que o desempacotamento funcionou pedir o 'x'
print(total)
