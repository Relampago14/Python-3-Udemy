try:
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é ímpar!')

except (ValueError, TypeError):
    print(f'Você não digitou um número inteiro.')
