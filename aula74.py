class MeuError(Exception):
    pass


def testar():
    raise MeuError('Meu Erro')


try:
    testar()
except MeuError as error:
    print(f'Erro! {error}')
