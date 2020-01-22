"""
Filter

- Serve para filtrar dados de uma coleção;
- Recebe como parâmetro uma função e um iterável;
- Retorna um objeto do tipo Filter;
- Assim como acontece com map(), os dados são apagados da memória após o uso.
"""
import statistics  # Biblioteca para trabalhar com dados estatísticos

# Exemplo 1 - Trabalhando com dados coletados:
dados = [1.3, 2.7, 8.8, 4.1, 4.3, -8.1]

# Calculando média dos dados com a função mean()
media = statistics.mean(dados)

print(media)

res = filter(lambda x: x > media, dados)
valores = list(res)

print(type(res))
print(valores)

# Removendo dados faltantes:
paises = ["", "Argentina", "", "Brasil", "Chile", "", "Colômbia", "", "Equador", "", "", "Venezuela"]

print(paises)

res = filter(None, paises)  # Passar None como argumento remove os dados faltantes (vazios).

print(list(res))

# Com lambda:
res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

res = filter(lambda pais: pais != "", paises)

print(list(res))

# Exemplo mais complexo:
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolo"]},
    {"username": "Carla", "tweets": ["Amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "Bob123", "tweets": ["Que país é esse?"]},
    {"username": "doggo", "tweets": ["Sextou", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar usuários inativos:

inativos = filter(lambda user: len(user["tweets"]) == 0, usuarios)  # Forma 1

print(list(inativos))

inativos = filter(lambda user: not user["tweets"], usuarios)  # Forma 2: lista vazia, em booleano, é falso.

print(list(map(lambda user: user['username'], inativos)))  # Pegando apenas os nomes de usuários.

# Exemplo de map() e filter():
nomes = ["Vanessa", "Ana", "Maria"]

# Criar uma lista de instrutoras, desde que o nome tenha menos de 5 caracteres:
instrutoras = filter(lambda nome: len(nome) < 5, nomes)
lista = list(map(lambda nome: f"Sua instrutora é: {nome}", instrutoras))

print(lista)