from contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, nome, idade, agencia, n_conta, saldo, limite):
        super().__init__(nome, idade, agencia, n_conta, saldo)
        self.limite = limite

    def detalhes(self):
        print()
        print(f'Nome: {self.nome} \n'
              f'Idade: {self.idade} \n'
              f'Agência: {self.agencia} \n'
              f'Nº conta: {self.n_conta} \n'
              f'Saldo: {self.saldo:.2f} \n'
              f'Limite atual: {self.limite:.2f} \n')

    def alterar_limite(self, usuario, clientes):
        try:
            novo_limite = float(input('Digite o seu novo limite: '))
            for cliente in clientes:
                if cliente[3] == self.n_conta:
                    cliente.pop(5)
                    cliente.insert(5, novo_limite)
            self.limite = novo_limite
            print()
            usuario.detalhes()
            print()
        except (ValueError, TypeError):
            print('Por favor, insira um valor correto.')

    def sacar(self, clientes):
        try:
            valor = float(input('Digite o valor a ser sacado: '))
            if (self.saldo + self.limite) < valor:
                print('Você não pode realizar esse saque. Valor do Saque maior que o limite. \n'
                      f'Saque: {valor:.2f} \n'
                      f'Saldo: {self.saldo:.2f} \n'
                      f'Limite: {self.limite:.2f} \n')
                return
            self.saldo -= valor
            for cliente in clientes:
                if cliente[3] == self.n_conta:
                    cliente.pop(4)
                    cliente.insert(4, self.saldo)
            return self.detalhes()
        except (TypeError, ValueError):
            print('Digite corretamente o valor a ser sacado. \n')
