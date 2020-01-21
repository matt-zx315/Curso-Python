"""
Generators ou Generator expressions

Em aulas passadas:
 - List comprehension;
 - Dictionary comprehension;
 - Set comprehension.

Generators funcionam de maneira semelhantes, porém para tuplas.

- Retorna um objeto do tipo Generator
- Assim como Maps, e Filters, os Generators são apagados da memória após seu uso;
- Tem melhor performance que os outros comprehensions.
"""
from sys import getsizeof  # Retorna a quantidade de bytes em memória do elemento passado como argumento

# Exemplo
nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina", "Aloízio"]

print([nome[0] == "C" for nome in nomes])  # List comprehension
print(nome[0] == "C" for nome in nomes)  # Objeto do tipo Generator

print(type([nome[0] == "C" for nome in nomes]))
print(type(nome[0] == "C" for nome in nomes))

# Convertendo pra tupla:
print(tuple(nome[0] == "C" for nome in nomes))

print(getsizeof("Nepu"))  # Mostra quantos bytes a string "Nepu" está ocupando em memória.
print(getsizeof(9))
print(getsizeof(978))
print(getsizeof(True))
print(getsizeof([nome[0] == "C" for nome in nomes]))
print(getsizeof(nome[0] == "C" for nome in nomes))

lista = [x for x in range(1000) if x % 7 == 0]
conjunto = {x for x in range(1000) if x % 7 == 0}
dicionario = {x // 7: x for x in range(1000) if x % 7 == 0}
generator = (x for x in range(1000) if x % 7 == 0)

print(f"\nUso de memória por list comprehension: {getsizeof(lista)} Bytes.")
print(f"Uso de memória por set comprehension: {getsizeof(conjunto)} Bytes.")
print(f"Uso de memória por dictionary comprehension: {getsizeof(dicionario)} Bytes.")
print(f"Uso de memória por generator expression: {getsizeof(generator)} Bytes.\n")

# Iterando em generator expressions:
for g in generator:
    print(g)