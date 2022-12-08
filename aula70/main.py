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
print()

cliente2 = ClienteVIP('Valter', 35, 'Rodrigo')
print(cliente2.nome)
cliente2.falar()
