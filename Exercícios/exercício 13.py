def jogo(num=0):
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'fizz'
    if num % 5 == 0:
        return 'buzz'
    return num


número = jogo(float(input('Digite um número: ')))
print(número)
