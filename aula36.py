# Não é um exercício proposto, mas gostei muito do script e a forma com a qual ele funciona me agradou

perguntas = {'Pergunta 1': {
                'pergunta': 'Quanto é 2+2? ',
                'respostas': {'a)': '3', 'b)': '7', 'c)': '6', 'd)': '4'},
                'resposta_certa': 'd)',
    },
            'Pergunta 2': {
                'pergunta': 'Quanto é 4+4? ',
                'respostas': {'a)': '8', 'b)': '2', 'c)': '0', 'd)': '6'},
                'resposta_certa': 'a)',
    },
            'Pergunta 3': {
                'pergunta': 'Quanto é 3x2? ',
                'respostas': {'a)': '9', 'b)': '5', 'c)': '2', 'd)': '6'},
                'resposta_certa': 'd)',
    },
            'Pergunta 4': {
                'pergunta': 'Quanto é 6+6/2? ',
                'respostas': {'a)': '6', 'b)': '12', 'c)': '9', 'd)': '3'},
                'resposta_certa': 'c)',
    },
            'Pergunta 5': {
                'pergunta': 'Quanto é (4+4)x2? ',
                'respostas': {'a)': '2', 'b)': '8', 'c)': '16', 'd)': '12'},
                'resposta_certa': 'c)',
    },
}
print()

cont = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Alternativas: ')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}: {rv}')

    resposta_usuario = str(input('Responda: '))
    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns! Você acertou.')
        cont += 1
    else:
        print(f'Que pena. A reposta certa era {pv["resposta_certa"]}.')
    print()

if cont > 1:
    print(f'Você acertou {cont} respostas!')
elif cont == 1:
    print(f'Você acertou {cont} uma resposta.')
else:
    print(f'Que pena, você não acertou nenhuma :(')
