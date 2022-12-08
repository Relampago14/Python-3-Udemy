from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        Eletronico.__init__(self, nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            erro = f'{self._nome} não está ligado.'
            print(erro)
            self.log_erro(erro)
            return
        if self._conectado:
            erro = f'{self._nome} já está conectado'
            print(erro)
            self.log_erro(erro)
            return
        info = f'{self._nome} conectou-se.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            erro = f'{self._nome} não está ligado.'
            print(erro)
            self.log_erro(erro)
            return
        if not self._conectado:
            erro = f'{self._nome} já está desconectado'
            print(erro)
            self.log_erro(erro)
            return
        info = f'{self._nome} desconectou-se'
        print(info)
        self.log_info(info)
        self._conectado = False
