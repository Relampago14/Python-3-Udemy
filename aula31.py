"""def func(*num):
    print(num)
    print(num[0])
    print(num[-1])
    print(len(num))


lista = [1, 2, 3]
func(*lista)"""


def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')
    print(idade)


lista = [1, 2, 3]
lista2 = [10, 20, 30]
func(*lista, *lista2, nome='João', idade='17')
