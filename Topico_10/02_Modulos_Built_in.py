"""
Módulos built-in

 - Módulos integrados ao Python;
 - São adicionados ao instalar o Python;
 - Não são carregados ao iniciar para não haver sobrecarga da memória;
 - Precisam ser importados.

Lista completa dos módulos do Python em https://docs.python.org/3/py-modindex.html

Ao importar um módulo ou propriedade, estes se tronam "visíveis" ao usar a função dir().
"""

# # Utilizando alias (apelidos):
# import random as rdm  # rdm é o alias (apelido) de random.
#
# print(rdm.randint(0, 10))  # A partir de agora, é obrigatório usar esse alias.

# Usando o alias para uma função:
# from random import randint as rdi, uniform as ufm  # É possível, ainda, importar várias funções com alias por vez.
#
# print(rdi(0, 10))  # Novamente, a partir de agora, a função só sera reconhecida pelo Python se for usado o alias.
# print(ufm(4, 36))

# # Importando todo o conteúdo do módulo de uma vez:
# from random import *
#
# print(randint(0, 10))
#
# cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
# shuffle(cartas)
# print(cartas)
#
# print(choice(["pedra", "papel", "tesoura"]))

# Para organizar múltiplos imports, é utilizada tupla, cada item numa linha:
from random import (
    choice,
    randint,
    shuffle,
    uniform
)

print(dir())

print(randint(0, 10))

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
shuffle(cartas)
print(cartas)

print(choice(["pedra", "papel", "tesoura"]))
print(uniform(9, 90))
