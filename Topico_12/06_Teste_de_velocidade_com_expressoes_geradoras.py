"""
Teste de velocidade com expressões geradoras
"""
import time

# Gerador (Generator)


def nums():
    for _num in range(10):
        yield _num


gen1 = nums()
print(gen1)  # <generator object nums at 0x7fbe55e1a5d0>

print(next(gen1))
print(next(gen1))

# Expressão geradora (Generator expression)


gen2 = (num for num in range(10))
print(gen2)  # <generator object <genexpr> at 0x7fbe55e1a650>

print(next(gen2))
print(next(gen2))

# Teste de velocidade:
gen_inicio = time.time()
print(sum(num for num in range(100_000_000)))
gen_tempo = time.time() - gen_inicio

list_inicio = time.time()
print(sum([num for num in range(100_000_000)]))
list_tempo = time.time() - list_inicio

print(f"\nA expressão geradora levou {gen_tempo}\nenquanto o list comprehension levou {list_tempo}.")
