"""
Em um módulo Python, não se deve deixar prints soltos.
Para isso, é feita uma verificação, que permite que os prints executem APENAS
se o módulo em execução for o principal (__main__)
"""

from random import randint


def gera_matriz(_linhas=2, _colunas=2, _min=0, _max=100):
    _matriz = []

    for lin in range(_linhas):
        _matriz.append([])

        for col in range(_colunas):
            _matriz[lin].append(randint(_min, _max))

    return _matriz


def calcula_transposta(_matriz):
    _transposta = []

    for lin in range(len(_matriz[0])):
        _transposta.append([])

        for col in range(len(_matriz)):
            _transposta[lin].append(_matriz[col][lin])

    return _transposta


def imprime_matriz(_matriz):
    for linha in _matriz:
        print(linha)


if __name__ == "__main__":
    matriz = gera_matriz()
    nova = calcula_transposta(matriz)

    imprime_matriz(matriz)
    imprime_matriz(nova)

    print("matrizes.py está sendo executadoi diretamente.")
else:
    print(f"matrizes.py foi importado com o nome {__name__}.")
