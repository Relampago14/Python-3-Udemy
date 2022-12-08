"""class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo o arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando o arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo')
        self.arquivo.close()
        return True


with Arquivo('arquivo.txt', 'w') as arquivo:
    arquivo.write('Ola')
"""

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo')
        yield arquivo
    finally:
        print('Fechando o arquivo')
        arquivo.close()


with abrir('arquivo.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
