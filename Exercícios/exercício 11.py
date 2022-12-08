def soma(a=0, b=0, c=0):
    conta = a + b + c
    print(conta)


try:
    soma(float(input('Digite um número: ')), float(input('Digite um número: ')), float(input('Digite um número: ')))
except ValueError:
    print('Por favor digite um número válido')
