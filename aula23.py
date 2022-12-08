var = ['João', 'Marcos', 'Moreira']

comeca_com_j = False

for v in var:
    if v.lower().startswith('j'):
        continue
    print(v)
else:
    print('Não existe uma palavra que começa com "J"')
