"""
Zip

Cria um iterável de tipo Zip Object, que agrega elementos de cada um dos iteráveis passados em tuplas.

- Apaga da memória após o primeiro uso
- Utiliza como parâmetro o menor tamanho de iterável, ou seja, para quando acabar de varrer o menor iterável.

OBS.: Para trabalhar com dicionários, prestar atenção no que é passado como argumento de zip().
- Para chaves, utilizar o próprio dicionário ou dicionário.keys();
- Para valores, utilizar dicionário.values()
- Para ambos, utilizar dicionário.items() -> retorna uma tupla.
"""

# Exemplo 1:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))
print(list(zip1))

# Removido da memória após o primeiro uso:
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

# Convertendo para outras coleções de dados:
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip(lista1, lista2)))  # Transforma os elementos do primeiro iterável em chaves e os do segundo em valores.

# Com listas de tamanhos diferentes:
lista3 = [7, 8, 9, 10, 11]

print(list(zip(lista1, lista2, lista3)))

# Trabalhando com diferentes iteráveis:
lista = [1, 2, 3, 4, 5]
tupla = (6, 7, 8, 9, 10)
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
conjunto = {16, 17, 18, 19, 20}

zipa_tudo = zip(lista, tupla, dicionario.values(), conjunto)
print(list(zipa_tudo))

# Lista de tuplas:
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))  # Desempacotamento

# Exemplos práticos:
prova1 = [88, 93, 75]
prova2 = [96, 70, 84]
alunos = ["Maria", "Pedro", "Carla"]

print(list(zip(alunos, prova1, prova2)))

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Usando map():
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

print(dict(zip(alunos, map(lambda x: list(x), zip(prova1, prova2)))))