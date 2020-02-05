"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS.: raise não é uma função, mas uma palavra reservada, assim como def, for entre outras.

raise é usado para criar exceções e mensagens de erro personalizadas para um código.

Sintaxe:

raise TipoDoErro("Mensagem de erro")

Assim como reutrn, raise encerra uma função.
"""


def colore(_texto, _cor):
    cores = ("roxo", "branco", "preto", "verde", "azul", "amarelo", "laranja", "vermelho")

    if type(_texto) is not str:
        raise TypeError(f"Argumento _texto deve ser do tipo string. Recebido tipo {type(_texto).__name__}")
    if type(_cor) is not str:
        raise TypeError(f"Argumento _cor deve ser do tipo string. Recebido tipo {type(_cor).__name__}")
    if _cor not in cores:
        raise ValueError(f"A cor inserida precisa ser uma das seguintes:\n{cores}")
    print(f"O texto {_texto} será da cor {_cor}.")


colore("Nepu", "roxo")
# colore("Nepu", 6)
# colore(6, "roxo")
# colore(6, 6)
colore("Nepu", "azul calcinha")