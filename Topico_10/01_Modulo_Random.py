"""
Em Python, módulos nada mais são que arquivos.

 - Módulo random -> Possui várias funções para geração de números pseudo-aleatórios.
 - Número pseudo-aleatório: A cada execução, o valor pode ser repetido.

OBS.: Existem duas formas de utilizar um módulo ou suas funções

 1) Importando o módulo inteiro:

 Dessa forma, todo o conteúdo do módulo (classes, funções, aributos e propriedades)
 estará disponível para uso (ficará em memória). Para acessar o conteúdo, é necessário escrever o nome do módulo,
 seguido por ponto (.) e o nome da classe/função/aributo/propriedade.

 Não recomendado caso se saiba quais propriedades serão utilizadas no código.

 2) Importando apenas a classe/função/aributo/propriedade específica:

 Neste caso, apenas a classe/função/aributo/propriedade necessária ao código será importada e armazenada na memória.
 Para utilizar uma propriedade que foi importada dessa forma, basta digitar seu nome.

 Forma recomendada.

"""

# # Forma 1 - Sintaxe:
# import random
#
# print(random.random())  # Exibe um número aleatório entre 0 e 1, com 0 pertencente aos valores e 1 não pertencente.

# Forma 2 - Sintaxe:
from random import random  # Esse import pega do módulo random apenas a função random.
from random import uniform, randint, choice, shuffle  # Importando várias funções de uma vez.

for i in range(10):
    print(random())  # Acesso direto à função

for i in range(10):
    print(uniform(5, 25))  # Gera um valor pseudo-aleatório com casas decimais dentro de um intervalo.

for i in range(6):
    print(randint(1, 60), end=', ')  # Gera um valor pseudo-aleatório inteiro dentro de um intervalo.

print()

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))  # Escolhe aleatoriamente um valor dentro de um iterável

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

print(cartas)

shuffle(cartas)  # Embaralha dados. Não pode ser passada como argumento de print().

print(cartas)
