"""
Doctests

Testes podem servir como documentação.

Para escrever um doctest, é preciso criar um docstring
e digitar o sinal de maior (>) 3 vezes, como se fosse
um console Python, seguido da função, argumentos e
terminando na linha inferior com o resultado da operação.
Também é possível fazer mais de um teste por doctest.

Rodando doctest no terminal (python -m doctest -v <nome do arquivo>):

# Entrada:
python -m doctest -v Topico_18/03_Doctests.py

# Saída (teste bem-sucedido):
17
Trying:
    soma(1, -2, 3)
Expecting:
    2
ok
1 items had no tests:
    03_Doctests
1 items passed all tests:
   1 tests in 03_Doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Saída (teste mal-sucedido):
File "Topico_18/03_Doctests.py", line 43, in 03_Doctests.soma
Failed example:
    soma(9, -7, 8)
Expected:
    16
Got:
    10
1 items had no tests:
    03_Doctests

Trying -> Operação que o teste executa.
Expected -> O que o desenvolvedor colocou como resultado esperado.
Got -> Resultado obtido pelo programa ao executar a função/método.
ok -> Indica que o resultado obtido se iguala ao resultado esperado.

O maior problema dos doctests é que o resultado esperado deve ser escrito
EXATAMENTE da mesma maneira que o terminal apresentará o resultado obtido.
"""


# Exemplo 1:


def soma(*args):
    """
    Soma um conjunto de valores.

    >>> soma(1, -2, 3)
    2

    >>> soma(9, -7, 8)
    16
    """

    _soma = 0
    for num in args:
        _soma += num

    return _soma


print(soma(9, -6, 7, 8, -1))


# Exemplo 2 - Aplicando o TDD:


def duplicar(*args):
    """
    Duplica os valores de entrada.

    >>> duplicar(*[1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar('a', 'b', 'c', 'd')
    ['aa', 'bb', 'cc', 'dd']

    >>> duplicar(True, None)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * valor for valor in args]


print(duplicar(6, 9, 8))


# Exemplo 3 - Erro inesperado


def fala_oi():
    # O Python não reconhece aspas duplas dentro do docstring. É necessário utilizar aspas simples.

    """
    >>> fala_oi()
    'oi'
    """

    return "oi"


# Exemplo 4 - caso estranho


def verdade():
    """
    Retorna verdade

    >>> verdade()
    True
    """

    return True


"""
Nesse caso, a IDE ajuda a evitar o erro, mas se o código for executado pelo terminal, haverá um erro.

No terminal:

True
Trying:
    verdade()
Expecting:
    True  
**********************************************************************
File "erro_estranho.py", line 5, in erro_estranho.verdade
Failed example:
    verdade()
Expected:
    True  
Got:
    True
1 items had no tests:
    erro_estranho
**********************************************************************
1 items had failures:
   1 of   1 in erro_estranho.verdade
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.

Isso acontece porque espaços a mais escritos depois do retorno são ignorados
pela IDE, mas o mesmo não acontece pelo interpretador Python executado pelo
terminal.
"""
print(verdade())
