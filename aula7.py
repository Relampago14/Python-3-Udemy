nome = 'João Marcos'
idade = 17
altura = 1.80
maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{0} {0} tem {1} anos de idade e seu IMC é: {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é: {im:.2f}'.format(n=nome, i=idade, im=imc))
