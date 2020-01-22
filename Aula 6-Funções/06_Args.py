"""
*args

 - É um parâmetro como outro qualquer. Isso significa que poderá receber
 qualquer nome, desde que comece com asterisco (*).

 Por convenção, utilizamos *args para definí-lo.

 O parâmetro *args coloca os valores de entrada informados em uma tupla.
"""

# Em uma função comum, precisamos criar parâmetros default para termos flexibilidade.


def soma_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_numeros(9, 4, 6))

# Com *args, no entanto...


def soma_numeros(*args):
    # total = 0
    #
    # for num in args:
    #     total += num
    #
    # return total

    return sum(args)  # Muito mais simples.


print(soma_numeros())
print(soma_numeros(5))
print(soma_numeros(3, 8))
print(soma_numeros(6, 4, 9))
print(soma_numeros(2, 1, 7, 6))

# OBS.: Tomar cuidado com os parâmtros passados. Tipos de dados diferentes podem não se misturar dependendo da operação.

# Usando listas:


def soma_numeros(*args):
    return sum(args)


numeros = range(1, 8)

# Desempacotador

print(soma_numeros(*numeros))  # O asterisco indica que o argumento passado é uma coleção de dados.