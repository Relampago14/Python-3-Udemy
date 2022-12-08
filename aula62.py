class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * (percentual / 100))

    # getter

    @property
    def preço(self):
        return self._preço

    @property
    def nome(self):
        return self._nome

    # setter

    @preço.setter  # Decorador
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '').replace(',', '.'))
        self._preço = valor

    @nome.setter  # Decorador
    def nome(self, letras):
        letras = str(letras).replace('a', '4').replace('e', '3')
        self._nome = letras

# uso o setter para configurar um valor e o getter para obter e retornar o mesmo


p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preço)
print(p1.nome)

print()

p2 = Produto('Caneca', 'R$15,0')
p2.desconto(10)
print(p2.nome)
print(p2.preço)
