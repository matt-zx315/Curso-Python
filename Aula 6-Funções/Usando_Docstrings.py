"""
Documentando funções com Docstrings

 - Docstrings: textos escritos entre aspas triplas duplas \"""

Podemos acessar docstrings de funções utilizando a propriedade .__doc__
Também podemos acessar a documentação com a função help()

Podem ser gerados automaticamente no PyCharm usando \""" seguido de enter.
"""


def diz_oi(nome="pessoa"):
    """Uma função simples que retorna "Oi" e o nome da pessoa
    Por padrão, retorna "Oi pessoa"

    Parâmetros:

     - nome: O nome da pessoa cumprimentada."""

    return "Oi " + nome + "!"


print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna o um número elevado à potência informada.
    Se nenhuma potência for passada, retorna o quadrado do número.
    :param numero: Número a ser elevado à potência.
    :param potencia: Potência a elevar o número. Por padrão, seu valor é 2.
    :return: retorna o valor de número elevado a uma potência.
    """

    return numero ** potencia


print(exponencial.__doc__)