# def master():
#     def slave():
#         print('Oi')
#     slave()
#
#
# master()

# def master(funcao):
#     def slave():
#         print('Agora estou decorada.')
#         funcao()
#     return slave
#
#
# def fala_oi():
#     print('Oi')
#
#
# fala_oi = master(fala_oi)
# fala_oi()

# def master(funcao):
#     def slave(*args):
#         print('Agora estou decorada.')
#         funcao(*args)
#     return slave
#
#
# @master
# def fala_oi():
#     print('Oi')
#
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
#
# outra_funcao('Olá, eu sou João Marcos')
# fala_oi()

# from time import time
# from time import sleep
#
#
# def velocidade(funcao):
#     def interna(*args):
#         começo = time()
#         resultado = funcao(*args)
#         fim = time()
#         tempo = (fim - começo) * 1000
#         print(f'\nA função levou {tempo}ms para ser executada')
#         return resultado
#     return interna
#
#
# @velocidade
# def demora():
#     for n in range(500):
#         print(n, end='')
#
#
# demora()

"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
"""


def decorar(funcao):
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')

    return funcao_decorada


def printar():
    for i in range(3):
        print(i)


nova_printar = decorar(printar)

nova_printar()
# Saída:
# ############
# 0
# 1
# 2
# ############
#
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é X = decorador(X).
