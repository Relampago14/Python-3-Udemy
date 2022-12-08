from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.detalhes()
print()
cp.depositar(10)
print()
cp.sacar(5)
print()
cp.sacar(5)
print()
cp.sacar(5)

cc = ContaCorrente(3333, 4444, 0)
print()
cc.detalhes()
print()
cc.depositar(110)
print()
cc.sacar(210)
print()
cc.sacar(220)

cc2 = ContaCorrente(3333, 4444, 0, 500)
print()
cc2.detalhes()
print()
cc2.depositar(110)
print()
cc2.sacar(210)
print()
cc2.sacar(400)
print()
cc2.sacar(1)

# conta = Conta(3333, 4444, 0)  # Não posso iniciar a classe pois a mesma é abstrata
# conta.detalhes()

# print()
# cp.depositar('2')  # Levanta o ValueError personalizado

# print()
# cp.sacar('5')  # Levanta o ValueError personalizado
