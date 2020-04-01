"""
Preservando metadata com wraps

 Metadata ou metadados -> dados intrínsecos ao arquivo.
 Wraps -> funções que envolvem elementos com diversas finalidades
"""
# Problema


def ver_log(_funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra."""
        print(f"Aqui você está chamando a função: {_funcao.__name__}.\n")
        print(f"Essa é a documentação:\n{_funcao.__doc__}.")

        return _funcao(*args, **kwargs)
    return logar


@ver_log
def soma(_a, _b):
    """Retorna a soma de dois números."""
    return _a + _b


# print(soma(6, 4))  # Teste

print(soma.__name__)  # Retorna 'logar'
print(soma.__doc__)  # Retorna 'Eu sou uma função (logar) dentro de outra.'

# Resolvendo o problema:
from functools import wraps


def ver_log(_funcao):
    @wraps(_funcao)  # Literalmente é só isso O.o
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra."""
        print(f"Aqui você está chamando a função: {_funcao.__name__}.\n")
        print(f"Essa é a documentação:\n{_funcao.__doc__}.")

        return _funcao(*args, **kwargs)
    return logar


@ver_log
def soma(_a, _b):
    """Retorna a soma de dois números."""
    return _a + _b


# print(soma(6, 4))  # Teste

print(soma.__name__)  # Retorna 'logar'
print(soma.__doc__)  # Retorna 'Eu sou uma função (logar) dentro de outra.'
