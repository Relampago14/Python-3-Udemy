from funcoes import *

tarefas = list()
tarefa_apagada = list()

while True:
    print('1 - Adicionar tarefas;'
          '\n2 - Listar tarefas;'
          '\n3 - Desfazer uma tarefa;'
          '\n4 - Refazer uma tarefa;'
          '\n5 - Encerrar o programa.')

    p = input('Sua opção: ').strip()

    try:

        p = int(p)

        if p == 1:
            print()
            nova_tarefa = input('Digite a sua tarefa: ')
            adicionar_tarefas(tarefas, nova_tarefa)
            print()
        elif p == 2:
            listar_tarefas(tarefas)
        elif p == 3:
            listar_tarefas(tarefas)
            if len(tarefas) > 0:
                tarefa_selecionada = input('Qual tarefa você deseja apagar? ')
                while True:
                    if tarefa_selecionada not in tarefas:
                        print('Você não digitou uma tarefa válida! tente novamente.')
                        break
                    desfazer_tarefa(tarefas, tarefa_selecionada, tarefa_apagada)
                    break
        elif p == 4:
            if len(tarefas) == 0:
                listar_tarefas(tarefas)
                continue
            refazer_tarefa(tarefa_apagada, tarefas)
        elif p == 5:
            print()
            print('Volte sempre!')
            break
        else:
            print()
            print('\033[1;31mPor favor, digite uma opção válida (1, 2, 3, 4 ou 5)\033[0;0m')
            print()

    except (ValueError, TypeError):
        print()
        print('\033[1;31mPor favor, digite uma opção válida (1, 2, 3, 4 ou 5)\033[0;0m')
        print()
