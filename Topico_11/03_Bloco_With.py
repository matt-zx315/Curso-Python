"""
Bloco with

Passos para trabalhar com arquivos:

 1 - Abrir arquivo
 2 - Trabalhar arquivo
 3 - Fechar arquivo

O bloco with é utilizado para criar um contexto no qual os arquivos em uso são fechados no fim do bloco.
"""

with open("texto.txt") as arquivo:
    print(arquivo.read())
    print(arquivo.closed)  # Dentro do bloco with o arquivo ainda está aberto.

print(arquivo.closed)  # O arquivo só se fecha após o fim do bloco with.
