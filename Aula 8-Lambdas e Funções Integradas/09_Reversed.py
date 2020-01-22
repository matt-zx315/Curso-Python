"""
Reversed

OBS.: Não confundir com o método reverse(), que funciona capenas em listas.

- A função reversed() funciona em qualquer iterável, invertendo-o.
- Retorna um objeto do tipo list_reverseiterator (o.O)
- Preserva o objeto original.
- Utiliza um valor menor de memória.
- É apagado depois do primeiro uso.
"""
from sys import *

lista = [1, 2, 3, 4, 5, 6]
res = reversed(lista)

print(type(res))
print(list(res))

print(tuple(res))  # Imprime uma lista vazia, já que res já foi utilizado uma vez.

print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Em conjuntos, não há ordem na organização dos elementos

print(getsizeof(res))
print(getsizeof(lista))

# Iterando com for sobre o reversed:
for item in reversed(lista):
    print(item, end=" ")

print()

# Sem uso do for:
print(''.join(list(reversed("nepuruzugya"))))

# Com slice de string:
print("nepuruzugya"[::-1])

# Fazendo um loop reverso com reversed():
for n in reversed(range(0, 10)):
    print(n, end=" ")

print()

# É o mesmo que:
for n in range(9, -1, -1):
    print(n, end=' ')