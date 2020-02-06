"""
Todo arquivo com a extensão .py é um módulo Python.
Isso significa que qualquer arquivo Python pode ser considerado um módulo.
Portanto, a sintaxe é a mesma.

É importante lembrar que, caso seu projeto possua diversas pastas (diretórios),
para acessar os módulos num mesma passa, é necessário digitar o caminho a partir
da raíz do projeto.
"""

from Topico_10.matrizes import *

matriz = gera_matriz(4, 3, 0, 9)
nova = calcula_transposta(matriz)

for linha in matriz:
    print(linha)

print()

for linha in nova:
    print(linha)
