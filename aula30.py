"""def funcao(var):
    return var


variavel = funcao('')

if variavel:
    print(variavel)
else:
    print('Nada')"""


"""def divisao(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 'Divisão por 0'


conta = divisao(8, 0)
print(conta)
"""


"""def dumb():
    return [1, 2, 3, 4, 5], True


var = dumb()
print(var, type(var))"""


def f(var):
    print(var)


def dumb():
    return f


variavel = dumb()
variavel('Impressão')
