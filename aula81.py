from enum import Enum, auto


class Direcoes(Enum):
    direita = auto()
    esquerda = auto()
    cima = auto()
    baixo = auto()


def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Você não pode se mover para essa direção.')

    return f'Movendo para {direcao.name}'


if __name__ == '__main__':
    print(mover(Direcoes.direita))
    print(mover(Direcoes.esquerda))
    print(mover(Direcoes.cima))
    print(mover(Direcoes.baixo))

    print()

    for direcao in Direcoes:
        print(f'{direcao} - {direcao.value} - {direcao.name}')
