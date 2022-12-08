from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Machado')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta  # Enviou uma classe inteira para o objeto 'ferramenta'
escritor.ferramenta.escrever()  # Executou um método por 'fora'

del escritor
print(caneta.marca)
maquina.escrever()

# Na associação, uma classe não depende da outra para funcionar e nem existir
