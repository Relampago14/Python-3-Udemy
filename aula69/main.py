from classes import *

"""
Associação - Usa
Agregação - Tem
Composição - É Dono
Herença - É
"""

cliente1 = Cliente('João', 17)
print(cliente1.nome)
cliente1.falar()
cliente1.comprar()
print()

aluno1 = Aluno('Marcos', 18)
print(aluno1.nome)
aluno1.falar()
aluno1.estudar()
print()

pessoa1 = Pessoa('Barbosa', 64)
print(pessoa1.nome)
pessoa1.falar()
print()

# Na herança temos uma classe suprema, e abaixo dela subclasses
