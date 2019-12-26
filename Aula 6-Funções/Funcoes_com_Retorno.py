"""
Em Python, funções que retornam None são funções sem retorno.

Para que uma função retorne um valor, seu bloco de código deve
ser finalizado com a palavra reservada return seguida do valor a retornar.

Não precisamos, necessariamente, criar uma variável para receber o valor
retornado pela função.

OBS.: Sobre a palavra reservada return:

1 - Ela finaliza a função, ou seja, encerra a execução.
2 - Podemos ter múltiplos retornos numa função.
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.
"""
from random import random

numeros = [1, 2, 3]
retorno_print = print(numeros)  # Apesar de ser apenas uma atribuíção, vemos que print imprime a lista no console.

retorno_pop = numeros.pop()

print(f"Retorno de pop: {retorno_pop}")
print(f"Retorno de print: {retorno_print}")  # A função print() não retorna nada.


def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()

ret = quadrado_de_7()

print(f"Retorno da função: {ret}")

# Refatorando a função para retornar o valor. (Refatorar = reescrever)


def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()

print(f"Retorno da função: {ret}")
print(f"Retorno da função: {quadrado_de_7()}")

# OBS.: Assim como variáveis, nomes de funções podem ser reutilizados e seus valores sobrescritos.


def diz_oi():
    print("Execução antes do retorno")
    return "Oi"
    print("Execução após retorno")  # Essa linha NUNCA será executa, pois está DEPOIS do return


print(diz_oi())


def nova_funcao():
    var = False

    if var:
        return 4
    elif var is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1)
print(num2)
print(num3)
print(num4)
print(outra_funcao())  # Retorna uma tupla.


def joga_moeda():
    valor = random()

    if valor > 0.5:
        return "Cara"
    return "Coroa"


print(joga_moeda())

# Exemplos de codificação desnecessária com retorno:


def eh_impar():
    numero = 6

    if numero % 2 != 0:
        return True
    else:
        return False  # Não é necessário usar else nesse caso.


print(eh_impar())