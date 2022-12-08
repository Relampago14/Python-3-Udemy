class A:
    vc = 123  # Variável de classe

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()

print(a1.vc)  # Instância
print(a2.vc)  # Instância
print(A.vc)

# Utilizar uma variável de classe com uma instância pode causar confusões
