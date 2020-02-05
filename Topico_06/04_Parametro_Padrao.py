"""
Parâmetro padrão (default parameter)

Funções com parâmetro padrão são aquelas que podem ou não receber um parâmetro de entrada.
Exemplo: print()

sintaxe:

def função(parâmetro1=valor_padrão1, parâmetro2=valor_padrão2 ...):
    <bloco de código>

OBS.: valores padrão devem ser declarados DEPOIS dos valores não-default.

Aplicação:

 - Flexibilidade nas funções;
 - Evita erros com parâmetros incorretos;
 - Permite trabalhar com exemplos mais legíveis de código.

Qualquer tipo de dado serve como parâmetro padrão: ints, strings, booleanos, floats, tuplas, listas, dicionários,
conjuntos, classes e até mesmo funções.
"""


def quadrado(numero):
    return numero ** 2


print(quadrado(6))  # É obrigatório passar o parâmetro.

# Se o programa precisar, por padrão, elevar o número por 2 na ausência de um argumento, basta atribuir o valor.


def exponencial(numero, potencia=2):  # O valor padrão torna opcional a passagem de um dado de entrada.
    return numero ** potencia


print(exponencial(7, 3))  # A potência é calculada utulizando os argumentos passados.
print(exponencial(8))  # A potência é calculada com apenas um argumento e o parâmetro padrão.

# OBS.: A função pode ter TODOS os parâmetros como opcionais.


def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo, instrutor Geek."
    elif nome == "Geek":
        return "Eu pensei que você fosse o instrutor."
    return f"Olá {nome}."


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao("Ozzy"))
print(mostra_informacao("Stephanie"))

# Usando funções como parâmetros:


def soma(a, b):
    return a + b


def mat(a, b, fun=soma):
    return fun(a, b)


def diferenca(a, b):
    return a - b


print(mat(2, 3))
print(mat(4, 6, soma))
print(mat(7, 5, diferenca))