from pessoas.pessoa import Cliente


class Conta(Cliente):
    def __init__(self, nome, idade, agencia, n_conta, saldo):
        super().__init__(nome, idade, agencia, n_conta)
        self.saldo = saldo

    def depositar(self, clientes):
        try:
            valor = float(input('Digite o valor do depósito: '))
            self.saldo += valor
            for cliente in clientes:
                if cliente[3] == self.n_conta:
                    cliente.pop(4)
                    cliente.insert(4, self.saldo)
            return self.detalhes()
        except ValueError:
            print('Digite corretamente o valor a ser depositado.')

    def detalhes(self):
        print(f'Nome: {self.nome} \n'
              f'Idade: {self.idade} \n'
              f'Agência: {self.agencia} \n'
              f'Nº conta: {self.n_conta} \n'
              f'Saldo: {self.saldo:.2f} \n')
