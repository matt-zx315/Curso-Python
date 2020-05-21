import random
from typing import Dict, List, Tuple

from colored import bg, fg, stylize

NAIPES: List[str] = '♠ ♥ ♣ ♦'.split()
CARTAS: List[str] = '2 3 4 5 6 7 8 9 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]

print(NAIPES)
print(CARTAS)


def cria_baralho(_aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas."""
    _baralho: BARALHO = [(naipe, carta) for naipe in NAIPES for carta in CARTAS]

    if _aleatorio:
        random.shuffle(_baralho)

    return _baralho


def distribuir_cartas(_baralho: list) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return _baralho[0::4], _baralho[1::4], _baralho[2::4], _baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas pra 4 jogadores"""
    _cartas: BARALHO = cria_baralho(True)
    _jogadores: List[str] = 'P1 P2 P3 P4'.split()
    _maos: Dict[str, BARALHO] = {j: m for j, m in zip(_jogadores, distribuir_cartas(_cartas))}

    for jogador, cartas in _maos.items():
        carta: str = ' '.join(f"{j} {c}" for (j, c) in cartas)
        print(f"{jogador} {carta}")


if __name__ == "__main__":
    jogar()
