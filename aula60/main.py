from datetime import datetime


class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


# p1 = Pessoa.por_ano_nasc('João', 2004)
p1 = Pessoa('João', 17)
print(p1)
print(p1.nome, p1.idade)
p1.ano_nasc()
