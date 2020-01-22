"""
List Comprehension

- permite gerar novas listas com dados procesados a partir de outro iterável.
- podemos, ainda, adicionar estruturas condicionais lógicas.

Sintaxes:

1 - gerando uma nova lista: [dado for dado in iterável]
2 - usando condicional if: [dado for dado in iterável if condição]
3 - usando condicionais if/else: [dado if condição else condição for dado in iterável]

O iterável pode ser: lista, tupla, conjunto ou dicionário.
"""

# Exemplo 1:
numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 10 for numero in numeros]

print(res)

"""
Separando em duas partes:

 1 - for numero in numero: para cada dado dentro do iterável
 2 - numero * 10: realize uma operação
"""

# Exemplo 2:
res = [numero / 2 for numero in numeros]

print(res)

# Exemplo 3 (usando funções):


def quadrado(_valor):
    return _valor * _valor


res = [quadrado(numero) for numero in numeros]

print(res)

# List comprehension X loop
# Loop
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List comprehension
print([numero * 2 for numero in numeros])

# Exemplo 4 (caracteres):
texto = "nepu"

print([letra.upper() for letra in texto])

# Exemplo 5 (strings):
pessoas = ["maria", "julia", "pedro", "guilherme", "vanessa"]

print([pessoa.capitalize() for pessoa in pessoas])

# Exemplo 6 (criando lista com range e list comprehension):
print([numero * 3 for numero in range(0, 11)])

# Exemplo 7 (booleanos):
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 8 (cast):
print([str(numero) for numero in [1, 2, 3, 4, 5, 6]])

# Exemplo 9 (condicionais):
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Refatorando...

pares = [numero for numero in numeros if not numero % 2]
# O módulo de qualquer número par por 2 (numero_par % 2) é 0. 0, em booleano, é False. not False = True

impares = [numero for numero in numeros if numero % 2]
# O módulo de 2 de qualquer ímpar é 1, o qual equivale a True em booleano.

print(pares)
print(impares)

# Exemplo 10 (if/else):
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)
