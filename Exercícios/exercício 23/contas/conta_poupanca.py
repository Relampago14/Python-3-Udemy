from contas.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, clientes):
        try:
            valor = float(input('Digite o valor a ser sacado: '))
            if valor > self.saldo:
                print('Você não pode realizar esse saque. Valor do Saque maior que o saldo \n'
                      f'Saque: {valor:.2f} \n'
                      f'Saldo: {self.saldo:.2f}')
                return
            self.saldo -= valor
            for cliente in clientes:
                if cliente[3] == self.n_conta:
                    cliente.pop(4)
                    cliente.insert(4, self.saldo)
            return self.detalhes()
        except (ValueError, TypeError):
            print('Digite corretamente o valor a ser sacado. \n')
