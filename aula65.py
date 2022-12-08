# O getter pega um atributo da classe, e caso haja um setter ele vai retornar o mesmo decorado

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return 'Sei lá'

    @nome.setter
    def nome(self, nome):
        print('SETTER')
        nome += ' Moreira Laudares'
        self._nome = nome


p1 = Pessoa('João marcos')
print(p1.nome)
print(p1.sobrenome)
