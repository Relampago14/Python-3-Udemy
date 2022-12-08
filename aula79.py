"""
Metaclasses - Classes que criam outras classes
"""


class MetaClasse(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método "b_fala" in {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'O método "b_fala" precisa ser um método, e não atributo em {name}')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=MetaClasse):
    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print('Oi')


b = B()
b.fala()
