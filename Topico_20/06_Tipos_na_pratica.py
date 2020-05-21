"""
Tipos de variáveis na prática.
"""
from typing import Dict, List, Set, Tuple

# Especificando tipos de dados mais complexos:
nomes: list = ["Nepu", "Puru"]
versoes: tuple = (3, 6, 9)
opcoes: dict = {'a': True, 'b': False}
valores: set = {1.6, 3.5, 4.2, 0.8, 7.9}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)

# Definindo tipos para dados DENTRO de uma coleção:
nomes: List[str] = ["Nepu", "Puru"]
versoes: Tuple[int, int, int] = (3, 6, 9)
opcoes: Dict[str, bool] = {'a': True, 'b': False}
valores: Set[float] = {1.6, 3.5, 4.2, 0.8, 7.9}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
