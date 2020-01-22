"""
**kwargs

 - Assim como o *args, poderia receber qualquer nome,
 mas foi adotado o **kwargs por convenção.

Diferente do *args, que coloca os valores em uma tupla,
o **kwargs exige que usemos parâmetros nomeados,
os transfomrando em um dicionário.

Em funções, podemos ter:

 - Parâmetros obrigatórios
 - *args
 - Parâmetros default (não obrigatórios)
 - **kwargs

Os parâmetros devem ser ordenados conforme lista acima
ao declarar a função.

Não seguir a ordem acima não retornará erros, mas pode
criar confusões no código.
"""


def paises(**kwargs):
    for codigo, pais in kwargs.items():
        print(f"O código de {pais} é '{codigo}'.")


paises(br="Brasil", us="Estados Unidos", ag="Argentina", de="Alemanha")


def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos.")
    print(args)

    if solteiro:
        print("Solteiro")
    else:
        print("Casado")

    print(kwargs)


funcao(8, "Julia")
funcao(18, "Marcos", 5, 3, 9, 8, None, solteiro=True)
funcao(34, "Felipe", você="Vai")
funcao(19, "Carla", 9, 4, 3, Java=False, Python=True)

# Funçaõ com a ordem correta de parâmetros:


def mostra_info(a, b, *args, instrutor="Geek", **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome="University", cargo="Instrutor"))

"""
a = 1
b = 2
args = (3, )
instrutor = "Geek"
kwargs = {"sobrenome": "University", "cargo": "Instrutor}
"""

# Função com a ordem incorreta dos parâmetros:


def mostra_info(a, b, instrutor="Geek", *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome="University", cargo="Instrutor"))

"""
a = 1
b = 2
args = ()
instrutor = 3
kwargs = {"sobrenome": "University", "cargo": "Instrutor}
"""


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': "Rodrigo", 'sobrenome': "Silveira"}

print(mostra_nomes(**nomes))


def soma_numeros(a, b, c):
    print(a + b + c)


# Desempacotando com * e ** (não precisamos usar *args e **kwargs):
lista = [1, 5, 9]
tupla = (3, 4, 8)
conjunto = {2, 6, 7}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(a=9, b=6, c=4)

soma_numeros(**dicionario)  # OBS.: Os nomes das chaves do dicionário devem ser OS MESMOS dos parâmetros da função!