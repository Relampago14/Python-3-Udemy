from classes import *

cliente1 = Cliente('João', 17)
cliente1.insere_endereco('Mário Campos', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

del cliente1
print()

cliente2 = Cliente('Maria', 45)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio Branco', 'AC')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Alberto', 25)
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('-=' * 30)
print()

# Uma classe integra a outra, se um objeto é apagado, suas instâncias mesmo as pertencentes a outra classe será apagado.
