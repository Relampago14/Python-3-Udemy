class A:
    def __new__(cls):
        print('Eu sou "new"')
        cls.nome = 'João'
        return object.__new__(cls)

    def __init__(self):
        print('Eu sou INIT')


a = A()
print(a.nome)
