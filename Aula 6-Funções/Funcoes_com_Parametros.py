"""
São funções que recebem dados para processamento.

Funções podem:

- não ter dados de entrada
- não ter dados de saída
- ter dados de entrada mas não ter dados de saída
- ter dados de saída mas não ter dados de entrada
- ter dados de entrada e de saída

Funções que peçam parâmetros de entrada, caso não os recebam, retornam erro do tipo TypeError
O mesmo tipo de erro pode ser retornado se a função receber um valor de tipo errado, a mais ou a menos.

Uma função pode receber N parâmetros, de acordo com a necessidade do programa.

Diferença entre parâmetros e argumentos:

- Parâmetros são variáveis declaradas na definição de uma função;
- Argumentos são dados passados durante a execução de uma função.

A ordem dos argumentos importa.
"""

# Na função quadrado_de_7():


def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())  # Essa função não recebe nenhum dado, portanto, retorna sempre o mesmo valor.

# Refatorando:


def quadrado(numero):
    return numero ** 2


print(quadrado(8))
print(quadrado(7))
print(quadrado(9))  # Retorna resultados diferentes por conta do parâmetro de entrada.


def cantar_parabens(aniversariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva {aniversariante}!")


cantar_parabens("Marcos")

# Funções com mais de um parâmetro:


def soma(a, b):
    return a + b


def produto(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(6, 4))
print(produto(3, 5))
print(outra(8, 7, "Nepu "))


def nome_completo(nome, sobrenome):  # parâmetros
    return f"Nome completo: {nome} {sobrenome}."


print(nome_completo("Keanu", "Reeves"))  # argumentos

# Ordem importa:
print(nome_completo("Reeves", "Keanu"))

# Argumentos nomeados: utilizando o nome dos parâmetros nos argumentos, podemos passá-los em qualquer ordem.
nome, sobrenome = "Keanu", "Reeves"

print(nome_completo(nome="Keanu", sobrenome="Reeves"))
print(nome_completo(sobrenome=sobrenome, nome=nome))

# Erro comum na utilização de return:


def soma_impares(numeros):
    soma_total = 0

    for numero in numeros:
        if numero % 2 == 1:
            soma_total += numero

    return soma_total


lista = list(range(0, 99))

print(soma_impares(lista))