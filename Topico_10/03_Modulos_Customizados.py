"""
Um módulo Python é todo arquivo com a extensão .py
Isso significa que qualquer arquivo Python pode ser considerado um módulo.
"""

from Topico_10.matrizes import *  # Diretório.módulo (Utilizar apenas letras e números, separados por underline)

matriz = gera_matriz(4, 3, 0, 9)
nova = calcula_transposta(matriz)

for linha in matriz:
    print(linha)

print()

for linha in nova:
    print(linha)
