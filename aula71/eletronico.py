class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            erro = f'{self._nome} já está ligado.'
            print(erro)
            self.log_erro(erro)
            return
        info = f'{self._nome} ligou-se.'
        print(info)
        self.log_info(info)
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            erro = f'{self._nome} já está desligado.'
            print(erro)
            self.log_erro(erro)
            return
        info = f'{self._nome} desligou-se.'
        print(info)
        self.log_info(info)
        self._ligado = False

