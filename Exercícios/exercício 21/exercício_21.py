from funcoes import *

novo_cnpj = input('Digite o seu CNPJ: ').replace('.', '').replace('/', '').replace('-', '')
verifica_cnpj(novo_cnpj)
