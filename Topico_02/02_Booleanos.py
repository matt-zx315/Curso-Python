"""
Tipo booleanos

Álgebra booleana, criada por George Boole.

2 constantes:

True -> Verdadeiro
False -> Falso

OBS.: os valores das constantes começam com letras MAIÚSICULAS.
"""

estado = True
print(estado)

"""
Operações básicas:

Negação (not) -> altera o valor da variável de True para False e de False para True.
Sempre o contrário de seu valor atual.

Ou (ou) -> operação binária (necessita de duas variáveis para comparação). Pelo menos
uma delas deve ser True para que o retorno seja verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False

E (and) -> Também é uma operação binária. Ambos os valores devem ser verdadeiros para que o retorno seja verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

# Negação
estado = not estado
print(estado)
print(type(estado))

# Ou
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# E
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(6 < 5)
print(4 > 1)
print(6 < 5 or 4 > 1)
print(6 < 5 and 4 > 1)
print(not (9 < 8))
# Lembrando que podemos fazer essas comparações também entre variáveis.