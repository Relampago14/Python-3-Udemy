try:
    horas = float(input('Digite as horas atuais: '))

    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 11 < horas <= 17:
        print('Boa tarde')
    elif 17 < horas <= 23:
        print('Boa noite')
except (ValueError, TypeError):
    print('Você não informou um horário correto.')
