from classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do saque precisa ser númerico.')
        if self.saldo < valor:
            print(f'Você não tem saldo suficiente.')
            return
        self.saldo -= valor
        self.detalhes()

