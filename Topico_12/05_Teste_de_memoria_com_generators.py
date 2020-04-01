"""
Teste de memória com generaors

# Sequência de Fibonacci
0, 1, 1, 2, 3, 5, 8, 13...
"""


def fib(_max):
    _a, _b = 0, 1
    _nums = [_a]

    while len(_nums) < _max:
        _nums.append(_b)
        _a, _b = _b, _a + _b

    return _nums


# Teste 1 - Usando lista: média de ~454 MB de memória para 100.000 números gerados (valores podem variar)
for f in fib(10):
    print(f)


def fib_gen(_max):
    _a, _b, _cont = 0, 1, 1

    while _cont < _max:
        yield _a
        _a, _b = _b, _b + _a
        _cont += 1


# Teste 2 - Usando geradores: média de ~8 MB de memória para 100.000 números gerados  (valores podem variar)
for f in fib_gen(10):
    print(f)
