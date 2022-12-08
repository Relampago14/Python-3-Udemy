from vendas.calc_preco import aumento, reducao

preco = 49.90
preco_aumento = aumento(preco, 15, True)
preco_reducao = reducao(preco, 15, True)

print(preco_aumento)
print(preco_reducao)
