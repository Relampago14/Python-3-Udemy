from dataclasses import dataclass


@dataclass(eq=True, repr=True, order=True, frozen=True, init=True)
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('João', 'Marcos')

print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)
