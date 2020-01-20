"""
Utilizando lambdas

- Conhecidas como expressões lambdas, ou simplesmente lambdas, são funções anônimas (sem nome).

- funções em Python:

def soma(a, b):
    return a + b

- lambdas:

lambda parâmetro: return retorno

Podemos ter expressões lambda com múltiplas entradas.
Passar parâmetros a mais ou a menos retorna um TypeError.
"""


# Exemplo de função:


def funcao(x):
    return 3 * x + 1


print(funcao(5))

# Exemplo de expressão lambda:
lambda x: 3 * x + 1

# Utilizando lambdas:
calc = lambda x: 3 * x + 1  # Não recomendável.

print(calc(4))
print(calc(7))

# Lambda com múltiplos parâmetros:
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
# Função strip(): remove espaços em branco no início e no fim de uma string.
# Função title(): capitaliza a primeira letra de uma string e deixa as outras letras minúsculas.

print(nome_completo("João", "da Silva"))

# Exemplo sem entradas
amar = lambda: "Como não amar Python?"
lamb1 = lambda x: 4 * x - 1
lamb2 = lambda x, y: (x + y) ** 0.5
lamb3 = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(lamb1(6))
print(lamb2(64, 36))
print(lamb3(3, 5, 4))

# Uso de expressões lambda:
autores = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card",
           "Douglas Adams", "H. G. Wells", "Leigh Brackett", "H. P. Lovecraft", "Agatha Christie", "Arthur Conan Doyle",
           "Kazuma Kamachi"]

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
"""
sort(key, reverse): função que ordena a lista
key: parâmetro usado como referência para ordenação

sobrenome.split(" "): separa a string em uma lista de strings. O espaço vazio como parâmetro indica onde a string
sofrerá a separação.
sobrenome.split()[-1]: retorna o último elemento da lista formada pelo split.
sobrenome.split()[-1].lower(): deixa todos os caracteres em minúsculo.

"""

print(autores)

# Definindo a expressão e passando o argumento:
print((lambda x: x + 5)(3))

# Funções aninhadas:


def fora(x):
    y = 4

    def dentro(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return dentro


for i in range(3):
    cl = fora(i)
    print(f"cl({i + 5}) = {cl(i + 5)}")
    # cl recebe o valor da função aninhada dentro(z). Ao passar um argumento para cl,
    # esse valor é passado para a função retornada por fora(x)


# Com lambda:


def fora(x):
    y = 4
    return lambda z: x + y + z


for i in range(3):
    cl = fora(i)
    print(f"cl({i + 5}) = {cl(i + 5)}")
    # Mesmo caso da função aninhada dentro(z), só que com menos linhas.

# Função quadrática: f(x) = ax² + bx + c


def gerador_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


fx = gerador_funcao_quadratica(1, -4, 3)

print(fx(0))
print(fx(2))
print(fx(1))
print(fx(3))

# Outra possibilidade:
print(gerador_funcao_quadratica(1, -5, 6)(0))
print(gerador_funcao_quadratica(1, -5, 6)(2))
print(gerador_funcao_quadratica(1, -5, 6)(3))
print(gerador_funcao_quadratica(1, -5, 6)(6))
print(gerador_funcao_quadratica(1, -5, 6)(4))