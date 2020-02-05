"""
Set comprehension

Sintaxe:

{valor for valor in iterável}

O iterável pode ser: lista, tupla, conjunto ou dicionário.
"""
# Exemplo 1:
numeros = {numero for numero in range(0, 10)}

print(numeros)

# Exemplo 2:
numeros = {numero ** 2 for numero in range(0, 10)}

print(numeros)

# DESAFIO: Fazer uma alteração no código acima para gerar um dicionário.
res = {f"{i}² = ": i ** 2 for i in range(0, 10)}

print(res)

# Exemplo 3:
texto = "Três pratos de trigo para três tigres tristes."
res = {letra for letra in texto}

print(res)