"""
Arquivo pra testar print.

Lista de cores completa: https://pypi.org/project/colored/
"""

from colored import *

texto = "%s Isso é um texto! %s" % (fg(208), attr(0))

print(texto)


def soma(_a, _b):
    return _a + _b


resultado = f"%s {soma(6, 4)} %s" % (fg(196), attr(0))

print(resultado)


def desenha_tabuleiro(_linhas, _colunas):
    _tabuleiro = []
    _branco = "%s   %s" % (bg(255), attr(0))  # Para o terminal, usar 255 para a cor branca.
    _preto = "%s   %s" % (bg(232), attr(0))  # Preto pode ser obtido com 0 ou 232.

    for lin in range(_linhas):
        _tabuleiro.append([])

        for col in range(_colunas):
            if lin % 2 == 0:
                if col % 2 == 0:
                    _tabuleiro[lin].append(_branco)
                else:
                    _tabuleiro[lin].append(_preto)
            else:
                if col % 2 == 0:
                    _tabuleiro[lin].append(_preto)
                else:
                    _tabuleiro[lin].append(_branco)
    return _tabuleiro


tabuleiro = desenha_tabuleiro(8, 8)


# para imprimir textos coloridos em listas, é preciso que cada impressão seja feita individualmente.
for linha in range(len(tabuleiro)):
    for coluna in tabuleiro[linha]:
        print(coluna, end='')
    print()
