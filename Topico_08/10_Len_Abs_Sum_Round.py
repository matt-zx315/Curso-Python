"""
Len, Abs, Sum e Round

len() -> Retorna o número de itens iterados.
    - Por "debaixo dos panos", toda vez que a função len() é chamada,
    o Python executa a função Dunder len: iterável.__len__()

abs() -> Retorna o valor absoluto de um número inteiro ou real. É o valor do número sem o sinal.

sum() -> Retorna a soma de um iterável, podendo receber um valor inicial,
e retorna a soma dos elementos, inclusive do valor inicial. Por padrão,
esse valor é 0. Essa função só pode ser usada com iteráveis puramente numéricos com valores inteiros ou reais.

round() -> Retorna um número arredondado para n dígitos de precisão após a casa decimal.
Se a precisão não for informada, retorna o inteiro mais próximo da entrada.
Caso o último dígito seja 5, será feito o arredondamento para cima.
"""

# Revisando len():
print(len("Nepuruzugyapea"))
print(len([1, 2, 3, 4, 5, 6]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5, 6, 7}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}))

# Dunder len
print("Nepu".__len__())

# abs():
print(abs(-5))
print(abs(14))
print(abs(-9.6))
print(abs(64))

# sum()
print(sum([1, 2, 3, 4]))  # Somando um iterável.
print(sum([1, 2, 3, 4], 5))  # Adicionando um valor inicial.

print(sum([1, 2, 3, 4, 5, 6]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5, 6, 7}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}.values()))

# round()
print(round(10.2))
print(round(5.89))
print(round(225.4478, 2))
print(round(68.1478525, 3))
print(round(78.901669741, 5))