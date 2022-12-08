def saudacao(cump='Olá', nome=''):
    if nome == '':
        nome = '<desconhecido>'
    print(cump, nome)


saudacao(nome=input('Qual o seu nome? '))
