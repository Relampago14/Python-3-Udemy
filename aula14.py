"""n1 = str(input('Digite um número: '))
n2 = str(input('Digite um número: '))

if n1.isnumeric() and n2.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
else:
    print('Não foi possível converter os números!')
"""

n1 = str(input('Digite um número: '))
n2 = str(input('Digite um número: '))

try:
    n1 = float(n1)
    n2 = float(n2)

    print(n1 + n2)
except:
    print('Errou')
