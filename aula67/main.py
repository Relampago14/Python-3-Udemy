from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa', 25.9)
p2 = Produto('iphone', 10000)
p3 = Produto('Caneco', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())

# Na agregação, um existe sem o outro porém um vai apresentar mal funcionamento
