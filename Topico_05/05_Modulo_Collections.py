"""
Módulo Collections -> High-performance Container Datatypes

Container de tipos de dados de alta performance -> Tipos de dados
para otimizar execução do programa
"""

from collections import Counter

"""
Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter,
semelhante a um dicionário, contendo como chave o elemento da lista passada e como valor, a
quantidade de ocorrências desse elemento.
"""
# Exemplo 1
lista = [1, 2, 3, 2, 3, 4, 3, 3, 3, 1, 2, 8, 4, 4, 5, 6, 6, 9, 7, 4, 5, 5, 0, 6, 6, 0, 5, 8, 7, 7]

cont = Counter(lista)
print(cont)
print(type(cont))

# Exemplo 2
print(Counter("Nepuruzugya"))

# Exemplo 3
texto = "Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter," \
        "semelhante a um dicionário, contendo como chave o elemento da lista passada e como valor, a" \
        "quantidade de ocorrências desse elemento."

palavras = texto.split(' ')
print(Counter(palavras))

# Mostrando os N elementos com a maior ocorrência.
print(Counter(palavras).most_common(3))

"""
Default Dict -> Permite a criação de um dicionário mesmo que seja passada apenas a chave e nenhum valor.
Poderá ser criado, então, um valor default, através de um lambda.
Caso a chave não exista, ela será criada e o valor atribuído a ela será o valor default.
Dessa forma, não haverá retorno de KeyError.

OBS.: lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.
"""

from collections import defaultdict

animais = defaultdict(lambda: 0)  # Valor default é 0.
print(animais)
print(type(animais))

animais[0]
print(animais)

animais[0] = "Raposa"
print(animais)

"""
Ordered Dict -> Em um dicionário comum, a ordem dos elementos não é garantida.
Para isso, é utilizado OrderedDict({chave: valor}). É um dicionário que garante
a ordem de inserção dos elementos.
"""

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f"Chave: {chave}: Valor: {valor}")

# Demonstrando:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # Retorna True

dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2)  # Retorna False

"""
Named Tuple -> Tupla que possui um nome e parâmetros
"""

from collections import namedtuple

cachorro = namedtuple("Cachorro", "idade raça nome")  # Forma 1
gato = namedtuple("Gato", "idade, raça, nome")  # Forma 2
passaro = namedtuple("Passaro", ["idade", "raça", "nome"])  # Forma 3

fenrir = cachorro(idade=5, raça='Husky', nome='Fenrir')
print(fenrir)

isis = gato(idade=4, raça='Siamês', nome='Isis')
print(isis)

zis = passaro(idade=3, raça='Pardal', nome='Zis')
print(zis)

print(fenrir[2])  # Forma 1: por índice
print(isis.nome)  # Forma 2: por nome de variável

"""
Deque -> Lista de alta performance.
"""

from collections import deque

deq = deque('Nepu')
print(deq)
print(type(deq))

# Adicionando itens
deq.append('r')
deq.append('u')
print(deq)

deq.append('I')         # Adiciona no final
deq.appendleft('C')     # Adiciona no começo
print(deq)

deq.pop()
deq.popleft()
print(deq)