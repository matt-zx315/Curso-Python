"""
Sorted

OBS.: Não confundir com o método sort(), o qual só funciona em listas.

Podemos utilizar sorted() com qualquer iterável.
Como o próprio nome diz, sorted() serve para ordenar elementos de uma coleção de dados.
Retorna uma nova lista com os elementos ordenados.
"""
from random import randint

# Método sort()
lista = [1, 3, 9, 8, 2, 0, 7, 4, 5, 6]
print(lista)
lista.sort()
print(lista)

lista = []

while len(lista) < 10:
    n = randint(0, 50)
    lista.append(n)

print(lista)

print(sorted(lista))  # Retorna uma lista ordenada
print(sorted(lista, reverse=True))  # Retorna uma lista na ordem inversa
print(sorted(lista, key=lambda x: x % 3))  # Retorna uma lista ordenada de acordo com o resto da divisão por 3

# Utilizando com outras coleções de dados
tupla = lista.copy()
print(sorted(tupla))

dicionario = {x // 7: x for x in range(1000) if x % 7 == 0}
print(sorted(dicionario.items()))

# Com dicionários dentro de listas:
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolo"]},
    {"username": "Carla", "tweets": ["Amo meu gato"], "Cor": "amarelo"},
    {"username": "jeff", "tweets": [], "Cor": "azul", "música": "Heavy Metal"},
    {"username": "Bob123", "tweets": ["Que país é esse?"]},
    {"username": "doggo", "tweets": ["Sextou", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(sorted(usuarios, key=lambda user: len(user)))  # Ordena pelo tamanho de cada dicionário dentro da lista.
print(sorted(usuarios, key=lambda user: user["username"]))  # Ordena de acordo com o nome de usuário.
print(sorted(usuarios, key=lambda user: len(user["tweets"]), reverse=True))  # Ordenando pelo número de tweets.

musicas = [
    {"Faixa": "Zombie Viking", "Artista": "Armored Dawn", "Tocou": 20},
    {"Faixa": "Petalstorm", "Artista": "Elvenking", "Tocou": 17},
    {"Faixa": "Rainmaker", "Artista": "Iron Maiden", "Tocou": 35},
    {"Faixa": "Armaggedon Soul", "Artista": "Blackline", "Tocou": 12},
    {"Faixa": "Electric Eye", "Artista": "Judas Priest", "Tocou": 16}
]

lista = sorted(musicas, key=lambda faixa: faixa["Tocou"], reverse=True)

for dado in lista:
    print(f"A faixa {dado['Faixa']}, do artista {dado['Artista']}, foi tocada {dado['Tocou']} vezes.")