def porcent(a, b):
    aumento = a + (a * (b / 100))
    return aumento


preço = float(input('Digite um valor: '))
porcento = float(input('Digite a porcentagem: '))

novo_preço = porcent(preço, porcento)
print(f'O preço R$ {preço:.2f} teve um aumento de {porcento}% e agora vale R$ {novo_preço:.2f}.')
