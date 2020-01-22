"""
Maps

- Com Map, fazemos mapeamento de valores para função;
- Recebe dois parâmetros: a função (sem parênteses) e um iterável;
- Retorna um objeto iterável de tipo map;
- Após seu uso (print, conversão para lista etc.), o objeto é apagado da memória.

Sintaxe:

map(função, iterável)

OBS.: map pode receber somente funções que recebam UM argumento apenas.

Para mapa = map(f, [a, b, c])
Temos mapa = f(a), f(b), f(c)
"""
import math


def area(raio):
    """Calcula a área de um círculo com raio r.
    raio -> float: distância do centro até a circunferência."""
    return int(math.pi * (raio ** 2) * 100) / 100


print(area(2))
print(area(5.3))

raios = [2, 5.3, 9, 7.2, 6.4]

# Forma comum:
areas = []

for r in raios:
    areas.append(area(r))

print(areas)

# Com list comprehension:
areas = [area(r) for r in raios]

print(areas)

# Utilizando Map:
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Map com lambda:
print(list(map(lambda r: int(math.pi * (r ** 2) * 100) / 100, raios)))

# OBS.: Após utilizar a função map(), seu valor será zerado:
for a in areas:
    print(a)  # Limpa a memória.

# Situação: uma lista de cidades e suas temperaturas, separadas por tuplas, precisa ter as temperaturas convertidas.
cidades = [("Berlim", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tóquio", 27), ("Nova Iorque", 28),
           ("Londres", 22), ("São Paulo", 20)]

# Lambda °C -> °F

print(list(map(lambda dado: (dado[0], 9 * dado[1] / 5 + 32), cidades)))