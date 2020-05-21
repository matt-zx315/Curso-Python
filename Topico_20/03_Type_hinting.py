"""
Type hinting

Solução formal para indicar o tipo de dado de maneira
estática numa linguagem dinamicamente tipada, especificada
na PEP 484 e implementada na versão 3.5 do Python.

OBS.: Passar um valor de tipo diferente do indicado por
type hinting não impedirá a execução, mas fará com que
a IDE avise que um valor passado não é o indicado.
"""


def cumprimentar(_nome: str) -> str:  # Type hinting
    return f"Olá, {_nome}"


print(cumprimentar('João'))


def cabecalho(_texto: str, _alinhamento: bool = True) -> str:
    if _alinhamento:
        return f"{_texto.title()}\n{'-' * len(_texto)}"
    else:
        return f" {_texto.title()} ".center(50, '#')


print(cabecalho('Nepu'))
print(cabecalho('Nepu', False))
