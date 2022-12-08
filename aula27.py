"""login = True

msg = 'Usuário logado.' if (login) else 'Usuário precisa logar'

print(msg)"""

"""idade = 16

if idade >= 18:
    print('Pode acessar!')
else:
    print('Não Pode acessar')"""

"""idade = 18
maior = (idade >= 18)
msg = 'Pode acessar' if maior else 'Não pode acessar'

print(msg)
"""

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números.')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode acessar' if maior else 'Não pode acessar'

print(msg)
