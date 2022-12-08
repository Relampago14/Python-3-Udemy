# try:
#     a = 1/0
# except NameError as erro:
#     print('Erro!', erro)
# except IndexError:
#     print('Erro de índice.')
# except KeyError:
#     print('Erro de chave')
# except Exception as erro:
#     print('Ocorreu um erro.')
# else:
#     print('Sucesso')
#     print(a)
# finally:
#     print('Finalmente')
#
# print('Continue')

try:
    a = 1/0
except NameError as erro:
    print('Erro!', erro)
except IndexError:
    print('Erro de índice.')
except KeyError:
    print('Erro de chave')
except Exception as erro:
    print('Ocorreu um erro.')
else:
   pass
finally:
    a = None
    pass

print(a)
