# lista1 = [0, 1, 2, 3, 4, 5]
# lista2 = '1234'
#
# print(hasattr(lista2, '__iter__'))

# lista1 = [0, 1, 2, 3, 4, 5]
#
# for v in lista1:
#     print(v)

# lista1 = [0, 1, 2, 3, 4, 5]
# lista1 = iter(lista1)
#
# print(next(lista1))
# print(next(lista1))
# print(next(lista1))
# print(next(lista1))
# print(next(lista1))
# print(next(lista1))
# print(hasattr(lista1, '__next__'))

# import sys
#
# lista = list(range(10))
#
# print(sys.getsizeof(lista))

# import sys
# from time import sleep
#
#
# def gera():
#     for n in range(100):
#         yield n
#         sleep(0.1)
#
#
# g = gera()
#
# print(next(g))


# def gera():
#     variavel = 'valor 1'
#     yield variavel
#     variavel = 'valor 2'
#     yield variavel
#     variavel = 'valor 3'
#     yield variavel
#
#
# g = gera()
#
# for v in g:
#     print(v)

# import sys
#
# l1 = [x for x in range(10000)]
# print(type(l1))
# print(sys.getsizeof(l1))
#
# l2 = (x for x in range(10000))
# print(type(l2))
# print(sys.getsizeof(l2))
