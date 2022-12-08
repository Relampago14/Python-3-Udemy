from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

clientes = list()


def criar_conta():
    try:
        nome = input('Digite o seu nome: ')
        idade = int(input('Digite sua idade: '))

        print()

        print('1 - Conta corrente \n'
              '2 - Conta poupança \n'
              '3 - Cancelar operação \n')

        pergunta = input('Digite a sua opção: ')
        if '1' == pergunta:
            criar_conta_corrente(nome, idade)
        elif '2' == pergunta:
            criar_conta_poupanca(nome, idade)
        else:
            print('\n Por favor, digite uma das opções corretamente. \n')
    except (ValueError, TypeError):
        print('\n Por favor, digite corretamente a sua idade. \n')


def criar_conta_corrente(nome, idade):
    nova_agencia = ContaCorrente.criar_agencia()
    novo_numero = ContaCorrente.criar_numero()
    saldo = 0
    limite = 100
    novo_cliente = [nome, idade, nova_agencia, novo_numero, saldo, limite, 1]
    clientes.append(novo_cliente)
    print(f'\n Parabéns {nome}! Aqui está seu novo número de agência "{nova_agencia}" '
          f'e o novo número de conta "{novo_numero}"  \n')


def criar_conta_poupanca(nome, idade):
    nova_agencia = ContaPoupanca.criar_agencia()
    novo_numero = ContaPoupanca.criar_numero()
    saldo = 0
    novo_cliente = [nome, idade, nova_agencia, novo_numero, saldo, 2]
    clientes.append(novo_cliente)
    print(f'\n Parabéns {nome}! Aqui está seu novo número de agência "{nova_agencia}" '
          f'e o novo número de conta "{novo_numero}"  \n')


def fazer_login():
    try:
        agencia = int(input('Digite a sua agência: '))
        n_conta = int(input('Digite o número da sua conta: '))

        for pos, cliente in enumerate(clientes):
            if agencia == cliente[2] and n_conta == cliente[3]:
                if cliente[5] == 2:
                    nome = cliente[0]
                    idade = cliente[1]
                    saldo = cliente[4]
                    usuario = ContaPoupanca(nome, idade, agencia, n_conta, saldo)
                    usuario.detalhes()

                    opcoes_conta_poupanca(usuario)

                elif cliente[6] == 1:
                    nome = cliente[0]
                    idade = cliente[1]
                    saldo = cliente[4]
                    limite = cliente[5]
                    usuario = ContaCorrente(nome, idade, agencia, n_conta, saldo, limite)
                    usuario.detalhes()
                    opcoes_conta_corrente(usuario, agencia)
    except (ValueError, TypeError):
        print('Por favor, digite corretamente a agência e o número da conta')


def opcoes_conta_corrente(usuario, agencia):
    while True:
        print('1 - Fazer um depósito \n'
              '2 - Sacar um valor \n'
              '3 - Alterar o limite \n'
              '4 - Cancelar essa operação \n')

        opcao = input('Digite a sua opção: ')
        print()

        if '1' == opcao:
            usuario.depositar(clientes)
        elif '2' == opcao:
            usuario.sacar(clientes)
        elif '3' == opcao:
            usuario.alterar_limite(usuario, clientes)
        elif '4' == opcao:
            break
        else:
            print('Por favor, digite uma das opções corretamente. \n')


def opcoes_conta_poupanca(usuario):
    while True:
        print('1 - Fazer um depósito \n'
              '2 - Sacar um valor \n'
              '3 - Cancelar essa operação \n')

        opcao = input('Digite a sua opção: ')
        print()

        if '1' == opcao:
            usuario.depositar(clientes)
        elif '2' == opcao:
            usuario.sacar(clientes)
        elif '3' == opcao:
            break
        else:
            print('Por favor, digite uma das opções corretamente. \n')
