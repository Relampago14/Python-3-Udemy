# Não entendi bem o comando do exercício e fiquei meio perdido...

# Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada.
# Faça a função1 executar daus funções que recebam um número diferente de argumentos

def func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def saudacao(nome):
    return f'Olá {nome}'


def cumprimento(nome, cump):
    return f'{cump} {nome}'


executando = func(saudacao, 'João marcos')
executando1 = func(cumprimento, 'João marcos', 'Bom dia')
print(executando)
print(executando1)
