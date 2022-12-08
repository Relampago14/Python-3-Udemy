from datetime import datetime

nome = 'João Marcos'
idade = 17
altura = 1.80
peso = float(80)
ano_atual = datetime.today().year
nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'Luiz nasceu em {nasc}')