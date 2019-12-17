"""
Sintaxe

while expressão_ou_variável_booleana:

O bloco while será repetido enquanto a expressão for verdaddeira.
"""

num = 0

while num < 10:
    print("Nepu!")
    num += 1

# Nos loops while, é necessário cuidar do critério de parada para não criar um loop infinito.

jessica = ''

while jessica != 'sim':
    jessica = input("Já acabou, Jéssica? ")