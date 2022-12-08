"""usuario = input('Digite o usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print(f'{usuario} menor que 6 digitos!')
else:
    print(f'Você foi cadastrado!')
"""

str1 = input('Digite algo: ')
str2 = input('Digite outro algo: ')

print(f'A quantidade total de caracteres digitados foi {len(str1) + len(str2)}')
print(str1.__len__())
