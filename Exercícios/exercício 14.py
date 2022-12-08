# Não entendi bem o comando do exercício e fiquei meio perdido...

# Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada.

def func(f):
    return saudacao()


def saudacao():
    return 'Bom dia!'


saud = func(saudacao)
print(saud)
