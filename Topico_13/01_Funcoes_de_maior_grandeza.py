"""
Funções de Maior Grandeza - Higher Order Functions (HOF)

 - Quando uma linguagem de programação suporta HOF,  indica
 que podemos ter funções que retornam outras funções como
 resultado ou mesmo que podemos passar funções como argumento
 para outras funções e ainda criar variáveis do tipo função.

Em Python, as funções são Cidadãos de Primeira Classe (First Class Citizens)
"""
# Definindo funções


def soma(_a, _b):
    return _a + _b


def subtrai(_a, _b):
    return _a - _b


def multiplica(_a, _b):
    return _a * _b


def divide(_a, _b):
    return _a / _b


def calcula(_a, _b, _funcao):
    return _funcao(_a, _b)


# Testando as funções:
a, b = 6, 3

print(soma(a, b))
print(subtrai(a, b))
print(multiplica(a, b))
print(divide(a, b))

print(calcula(a, b, soma))
print(calcula(a, b, subtrai))
print(calcula(a, b, multiplica))
print(calcula(a, b, divide))

"""
Nested Functions (Funções aninhadas)

Em Python, é possível criar funções dentro de funções, conhecidas como
Nested Functions (Funções Aninhadas) ou Inner Functions (Funções internas).


"""
from random import choice


def cumprimento(_pessoa):
    def humor():
        return choice(("Iaê ", "Vaza ", "Tá vivo "))
    return humor() + _pessoa


print(cumprimento("Manoel"))


def faz_me_rir():
    def rir():
        return choice(("HUEHUEHUEHUE", "KKKKKKKKKKKKKKK", "LOLOLOLOLOLOLOLOLOL"))
    return rir  # Retornando a função, não a execução, definida pelos parênteses.


rindo = faz_me_rir()
print(rindo())  # Executando a função retornada e armazenada na variável.


# Funções internas conseguem acessar o escopo de funções externas.


def faz_me_rir(_pessoa):
    def _dando_risada():
        _r = choice(("HUEHUEHUEHUE", "KKKKKKKKKKKKKKK", "LOLOLOLOLOLOLOLOLOL"))
        return f'{_r} {_pessoa}'
    return _dando_risada


rindo = faz_me_rir("Jão")
print(rindo())
print(rindo())
print(rindo())
