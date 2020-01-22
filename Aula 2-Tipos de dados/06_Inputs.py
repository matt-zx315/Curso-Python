"""
Recebendo dados de usuário
e formatação de saída de dados.

input() -> Todo dado recebido é uma string
int(dado) -> Cast: conversão de um tipo de dado em outro.
"""

# Em Python, string é tudo que estiver entre:
# - Aspas simples -> 'string'
# - Aspas duplas -> "string"
# - Aspas simples triplas -> '''string'''
# - Aspas duplas triplas -> """string"""


# Entrada de dados
nome = input("Qual o seu nome?")

idade = int(input("Quantos anos você tem?"))

# Processamento

# saída de dados

############################## Formatação Python 2.x ################################################
"""
print("Seja bem-vindo(a) %s" %nome)

print("%s tem %s anos." %(nome, idade))  # Obrigatório os parênteses para mais de uma variável
"""
############################## Formatação Python 3.x ################################################
"""
print("Seja bem-vindo(a) {0}" .format(nome))

print("{0} tem {1} anos." .format(nome, idade))
"""
############################## Formatação Python 3.7 ################################################

print(f"Seja bem-vindo(a) {nome}.")

print(f"{nome} tem {idade} anos.")

print(f"{nome} nasceu em {2019 - idade}.")