"""
Any e All

all() -> Retorna True se TODOS os elementos do iterável são verdadeiros,
ou ainda, se o iterável está vazio.

any() -> Retorna true se QUALQUER um dos elementos do iterável for verdadeiro.
"""

# Exemplo all():
print(all([0, 1, 2, 3, 4]))  # Retorna False por haver um valor 0 na lista.
print(all([1, 2, 3, 4]))  # Retorna True.
print(all([]))
print(all("Nepu"))

nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina"]

print(all(nome[0] == "C" for nome in nomes))  # Verifica se todos os nomes começam com "C".

nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina", "Aloízio"]

print(all([nome[0] == "C" for nome in nomes]))

# OBS.: Esse é um caso que sempre retorna True, já que o resultado que a função all() receberá
# sempre será um iterável com uma string ou vazio.
print(all([letra for letra in "eio" if letra in "aeiou"]))

print(all([num for num in [4, 2, 6, 8, 10] if num % 2 == 0]))

# Exemplo de any():

print(any([0, 1, 2, 3, 4]))
print(any([0, 0, False, 0, 0, (), []]))
print(any(nome[0] == 'C' for nome in nomes))

print(any([num for num in [4, 2, 6, 8, 10, 5, 3, 0] if num % 2 == 0]))