"""
Escopo de variáveis

2 casos:

1 - variáveis globais
    - São reconhecidas em todo o programa.

2 - variáveis locais
    - São reconhecidas apenas noz blocos nos quais são declaradas

Sintaxe Python para declarar variáveis:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que não colocamos o tipo da variável ao declará-la.
O tipo é inferido a partir do valor atribuído à variável.

Em C:
int num = 10;

Em Java
int num = 10;

Em Python:
num = 10

A consequência da tipagem dinâmica é a REATRIBUÍÇÃO: a capacidade de atribuirmos um novo valor de um tipo diferente
a uma variável anteriormente declarada.

Também é necessário que o valor seja atribuído a uma variável antes de usá-la.


"""

var = 10
print(var)

var = "Nepu"
print(var)

num = 54

# Exemplo de variável de escopo local
class Classe:
    novo = num + 10

print(Classe.novo)
"""
Novo é uma variável local. É impossível acessar seu valor diretamente.
Ele é acessível somente pela classe que o contem.
"""
