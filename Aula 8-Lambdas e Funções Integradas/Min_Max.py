"""
Min e Max

max() -> Retorna o maior valor do iterável ou de dois ou mais valores.
min() -> Retorna o menor valor do iterável ou de dois ou mais valores.
"""
from random import randint

# Usando max()
lista = [43, 9, 85, 490, 210, 64, 982, 123]
tupla = (43, 9, 85, 490, 210, 64, 982, 123)
conjunto = {43, 9, 85, 490, 210, 64, 982, 123}
dicionario = {'a': 43, 'b': 9, 'c': 85, 'd': 490, 'e': 210, 'f': 64, 'g': 982, 'h': 123}

print(max(lista))
print(max(tupla))
print(max(conjunto))
print(max(dicionario.values()))
print(max(dicionario.keys()))

print(min(lista))
print(min(tupla))
print(min(conjunto))
print(min(dicionario.values()))
print(min(dicionario.keys()))

# OBS.: Caso haja comparação numa string, o menor valor é o espaço (" ").

a, b, c = randint(0, 50), randint(0, 50), randint(0, 50)

print(f"Entre {a}, {b} e {c}, {max(a, b, c)} é o maior e {min(a, b, c)} é o menor.")

nomes = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

musicas = [
    {"Faixa": "Zombie Viking", "Artista": "Armored Dawn", "Tocou": 20},
    {"Faixa": "Petalstorm", "Artista": "Elvenking", "Tocou": 17},
    {"Faixa": "Rainmaker", "Artista": "Iron Maiden", "Tocou": 35},
    {"Faixa": "Armaggedon Soul", "Artista": "Blackline", "Tocou": 12},
    {"Faixa": "Electric Eye", "Artista": "Judas Priest", "Tocou": 16},
    {"Faixa": "Live to Win", "Artista": "Paul Stanley", "Tocou": 9}
]

print(max(musicas, key=lambda musica: musica["Tocou"]))
print(min(musicas, key=lambda musica: musica["Tocou"]))

# DESAFIO: Imprimir somente o nome das músicas mais e menos tocadas.

# Forma 1:
print(musicas[musicas.index(max(musicas, key=lambda musica: musica["Tocou"]))]["Faixa"])
print(musicas[musicas.index(min(musicas, key=lambda musica: musica["Tocou"]))]["Faixa"])

# Forma 2:
print(max(musicas, key=lambda musica: musica["Tocou"])["Faixa"])  # Forma 2
print(min(musicas, key=lambda musica: musica["Tocou"])["Faixa"])  # Forma 2

# Realizar o mesmo procedimento sem uso de max(), min() e lambda.

# Forma 1
menor, maior = musicas[0]["Tocou"], musicas[0]["Tocou"]
mais_tocada, menos_tocada = None, None

for faixa in musicas:
    if faixa["Tocou"] > maior:
        maior = faixa["Tocou"]
        mais_tocada = faixa["Faixa"]
    if faixa["Tocou"] < menor:
        menor = faixa["Tocou"]
        menos_tocada = faixa["Faixa"]

print(mais_tocada, menos_tocada)

# Forma 2:
for faixa in musicas:
    if faixa["Tocou"] > maior:
        maior = faixa["Tocou"]
    if faixa["Tocou"] < menor:
        menor = faixa["Tocou"]

for faixa in musicas:
    if faixa["Tocou"] == maior:
        print(f"A faixa mais tocada foi {faixa['Faixa']}.")
    if faixa["Tocou"] == menor:
        print(f"A faixa menos tocada foi {faixa['Faixa']}.")
