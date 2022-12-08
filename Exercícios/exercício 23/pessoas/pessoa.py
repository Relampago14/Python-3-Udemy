from random import randint


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def criar_agencia():
        digitos = ''
        while len(digitos) < 4:
            digitos += str(randint(0, 9))
        return int(digitos)

    @staticmethod
    def criar_numero():
        return randint(0, 9)


class Cliente(Pessoa):
    def __init__(self, nome, idade, angencia, n_conta):
        super().__init__(nome, idade)
        self.agencia = angencia
        self.n_conta = n_conta
