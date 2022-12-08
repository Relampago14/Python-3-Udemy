nome = str(input('Digite o seu nome: '))

if len(nome) <= 4:
    print(f'O nome {nome} é curto')
elif len(nome) <= 5:
    print(f'O nome {nome} é normal')
elif len(nome) > 5:
    print(f'O nome {nome} é grande')
