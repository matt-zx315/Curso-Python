"""
Checagem de tupos com MyPy

Novamente, o type hinting NÃO interrompe o código por passar argumentos de tipos diferentes do indicado.
O MyPy serve como um checador de tipos que acusa errosa no código caso o type hinting não seja respeitado.

Usado via terminal com o comando mypy <nome do arquivo.py>

No arquivo .py:
print(cabecalho('Nepu', 1))

Retorno (no caso de argumento de tipos diferentes):
mypy Topico_20/04_Tipos_com_my_py.py
Topico_20/04_Tipos_com_my_py.py:22: error: Argument 2 to "cabecalho" has incompatible type "int"; expected "bool"

Retorno (caso não haja diferenças nos tipos):
Success: no issues found in 1 source file

OBS.: O mypy só acusa erro SE for usado o type hinting.
Caso a tipagem seja dinâmica, não adianta seu uso.

Também é possível utilizar type hinting em comentários.
Os tipos dos parâmetros e do retorno podem ser escritos em um comentário
de uma linha. É importante lembrar que NUNCA deve se usar o type hint
ao lado dos parâmetros de da função e na linha seguinte utilizar o
type hinting no comentário. Nesses casos, o MyPy retorna a seguinte mensagem:

'error: Function has duplicate type signatures'
"""
import math

# Caso da aula anterior:


def cabecalho(_texto: str, _alinhamento: bool = True) -> str:
    if _alinhamento:
        return f"{'-' * len(_texto)}\n{_texto.title()}\n{'-' * len(_texto)}"
    else:
        return f" {_texto.title()} ".center(50, '#')


print(cabecalho('Nepu'))
print(cabecalho('Nepu', False))


def circunferencia(_raio):
    # type: (float) -> float  # Função com um parâmetro
    return 2 * math.pi * _raio


circunferencia(8)


def cabecalho_2(_texto, _alinhamento=True):
    # type: (str, bool) -> str  # Função com múltiplos parâmetros
    if _alinhamento:
        return f"{'-' * len(_texto)}\n{_texto.title()}\n{'-' * len(_texto)}"
    else:
        return f" {_texto.title()} ".center(50 - len(_texto), '*')


print(cabecalho_2('Nepu'))
print(cabecalho_2('Nepu', False))


def cabecalho_3(
            _texto,  # type: str
            _alinhamento=True,  # type: bool
            ):  # type: (...) -> str

    # Caso BEM esquisito: tipagem de parâmetros por comentários na entrada da função.
    if _alinhamento:
        return f"{'-' * len(_texto)}\n{_texto.title()}\n{'-' * len(_texto)}"
    else:
        return f" {_texto.title()} ".center(50 - len(_texto), '&')


print(cabecalho_3("Nepu"))
print(cabecalho_3("Nepu", False))
