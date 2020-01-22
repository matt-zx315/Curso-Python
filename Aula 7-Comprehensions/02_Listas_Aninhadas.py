"""
Listas Aninhadas

- Algumas linguagens de programação (C/Java/PHP) possuem uma estrutura de dados chamada array (vetor), que podem ser:
    - Unidumensionais (arrays (vetores))
    - Multidimensionais (matrizes)

Em Python, temos as listas.
"""

# Exemplo 1:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

# Acessando os dados:
print(listas[0])  # Acessando a linha 0
print(listas[1][1])  # Acessando a linha 1, coluna 1
print([coluna[2] for coluna in listas])  # Acessando a coluna 2

# Com índices negativos:
print(listas[-1])  # Acessando a linha 2 (índice_da_linha - tamanho_da_lista -> 2 - 3 = -1)
print(listas[-2][-2])  # Acessando a linha 1, coluna 1
print([coluna[-3] for coluna in listas])  # Acessando a coluna 1

# Iterando com loops numa lista aninhada
for lista in listas:
    print(lista)  # Imprimindo cada lista (linha)

for lista in listas:
    for num in lista:
        print(num)  # Imprimindo cada número

for lista in listas:
    for num in lista:
        print(num, end=" ")  # Iprimindo todos os números de cada linha
    print()  # Separando linhas

# Usando list comprehension
print([lista for lista in listas])  # Imprime linhas
[[print(valor, end=" ") for valor in lista] for lista in listas]  # Imprime valores
print()

# Gerando um tabuleiro/matriz 3 x 3
casas_brancas = "B"
casas_pretas = "P"

tabuleiro = [[casas_pretas if i % 2 == 0 else casas_brancas for i in range(0, 8)] if j % 2 == 1
             else [casas_pretas if i % 2 == 1 else casas_brancas for i in range(0, 8)]
             for j in range(0, 8)]

for linha in tabuleiro:
    print(linha)