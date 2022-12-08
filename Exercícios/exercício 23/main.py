from funcoes.funcoes import *

print('Bem Vindo ao Banco do Bananil!')
while True:
    print('1 - Criar Conta \n'
          '2 - Já tem uma conta? Faça o login \n'
          '3 - Sair do sistema \n')

    opcao = input('Digite a sua opção: ')
    print()

    if '1' == opcao:
        criar_conta()
    elif '2' == opcao:
        fazer_login()
    elif '3' == opcao:
        print('Volte sempre!')
        break
    else:
        print('\n Por favor, digite uma das opções corretamente. \n')
