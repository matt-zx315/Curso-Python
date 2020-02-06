"""
Pacotes

Módulo -> Arquivo com extensão .py
Pacote -> Coleção de módulos.

OBS.: No Python 2.x, é necessário um arquivo de nome __init__.py para a criação de um pacote.
Já no Python 3.x não é mais obrigatório. A prática ainda existe, porém, para manter compatibilidade.
No PyCharm, ao criar um novo pacote, este já vem com o arquivo __init__.py
"""

from Topico_10.pacote import WTF
from Topico_10.pacote.subpacote import modulo

p = WTF.palindromo(100)

print(f"O maior palíndromo de 0 a 100 é {p}.")

c = modulo.numeros_para_caracteres(30, 100)

print(f"De 20 a 100, por extenso, há {c} caracteres.")