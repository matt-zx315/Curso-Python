"""
Utilitários Python para auxiliar na programação

dir -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinados tipos de dado ou
variável.

dir(dado_de_qualquer_tipo)

help-> Apresenta a documentação/como utulizar os atributos/propriedades e funções/métodos disponíveis para determinado
tipo de dado ou variável.

help(dado_de_qualquer_tipo.propriedade)
"""

num = 10
print(dir(num))
print(help(num.__add__))

# É recomendável rodar esses comandos no terminal.
