import math

pi = math.pi


def dobra_lista(l):
    return [x * 2 for x in l]


def multiplica(l):
    r = 1
    for num in l:
        r *= num
    return r


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]

    print(dobra_lista(lista))
    print(multiplica(lista))
    print(f'{pi}')
