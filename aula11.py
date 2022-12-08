nome = str(input('Qual seu nome: '))
idade = int(input('Qual a sua idade: '))

maior = 18
velho = 65

if idade >= 65:
    print(f'{nome} não pode pegar o empréstimo pois é idoso.')
elif idade >= 18:
    print(f'{nome} pode pegar o empréstimo sem problemas!')
else:
    print(f'{nome} é muito novo para pegar um empréstimo.')
