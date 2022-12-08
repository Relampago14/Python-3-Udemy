# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as erro1:
#         print('Log:', erro1)
#         raise
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as erro2:
#     print(erro2)

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print('Você não pode efetuar uma divisão por 0.')
    print('Log:', error)
