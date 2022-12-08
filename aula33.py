# def func(arg, arg1):
#     return arg * arg1
#
#
# var = func(2, 2)

# a = lambda x, y: x * y
# print(a(2, 2))

# lista = [['P1', 14], ['P2', 15], ['P3', 13]]
#
# lista.sort(key=lambda item: item[1], reverse=False)
# print(sorted(lista[1]))

lista = [['P1', 14], ['P2', 15], ['P3', 13]]

print(sorted(lista, key=lambda i: i[0], reverse=True))
