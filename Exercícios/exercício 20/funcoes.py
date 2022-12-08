def adicionar_tarefas(lista, tarefa):
    """
    Adiciona uma tarefa à lista 'tarefas'.
    :param lista: recebe a lista 'tarefas'
    :param tarefa: recebe o input 'nova_tarefa'
    :return:
    """
    print(f'{tarefa} adicionada à lista de afazeres.')
    lista.append(tarefa)


def listar_tarefas(lista):
    """
    Lista as tarefas presentes na lista 'tarefas'
    :param lista: recebe a lista 'tarefas'
    :return:
    """
    print()
    if len(lista) == 0:
        print('Não há tarefas cadastradas.')
    else:
        for pos, tarefa in enumerate(lista):
            print(f'{pos+1} - {tarefa}')
    print()


def desfazer_tarefa(lista, tarefa, tarefa_deletada):
    """
    Busca uma tarefa a ser retirada da lista 'tarefas', remove a mesma e ao mesmo tempo adiciona a uma outra
    lista 'tarefa_apagada' para que possa ser refeita no futuro.
    :param lista: recebe a lista 'tarefas'
    :param tarefa: recebe a tarefa indesejada do input 'tarefa_selecionada'
    :param tarefa_deletada: recebe a lista 'tarefa_apagada'
    :return:
    """
    print()
    print(f'\033[1;33m{tarefa} apagado.\033[0;0m')
    print()
    tarefa_deletada.clear()
    tarefa_deletada.append(tarefa)
    for pos, t in enumerate(lista):
        if t == tarefa:
            lista.pop(pos)


def refazer_tarefa(tarefa_deletada, lista):
    """
    Refaz a tarefa presente em 'tarefa_apagada' e adiciona ao final da lista 'tarefas'
    :param tarefa_deletada: recebe a lista 'tarefa_apagada'
    :param lista: recebe a lista 'tarefas'
    :return:
    """
    print()
    print(f'\033[1;32m{tarefa_deletada[0]} refeito.\033[0;0m')
    print()
    lista.append(tarefa_deletada[0])
