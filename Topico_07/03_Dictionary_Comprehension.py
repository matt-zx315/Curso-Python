"""
Dictionary comprehension

Para criar uma lista: lista = [1, 2, 3, 4]
Para criar uma tupla: tupla = (1, 2, 3, 4)
Para criar um conjunto: conjunto = {1, 2, 3, 4}
Para criar um dicionário: dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Sintaxe:

{chave: valor for valor in iterável}

O iterável pode ser: lista, tupla, conjunto ou dicionário.
"""

# Exemplo 1:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrados)

# Exemplo 2 (criando dicionário a partir de lista):
numeros = [valor for valor in range(1, 10)]
quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# Exemplo 3 (combinando chaves e valores num dicionário):
chaves = 'abcdefghi'
valores = [numero for numero in range(1, 10)]

mistura = {chaves[i]: valores[i] for i in range(len(chaves))}

print(mistura)

# Exemplo 4 (condicionais)
res = {num: ("par" if num % 2 == 0 else "ímpar") for num in numeros}

print(res)