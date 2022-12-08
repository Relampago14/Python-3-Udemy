from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do saque precisa ser númerico.')
        if (self.saldo + self.limite) < valor:
            print(f'Limite de R$ {self._limite} estourado.')
            return
        self.saldo -= valor
        self.detalhes()

