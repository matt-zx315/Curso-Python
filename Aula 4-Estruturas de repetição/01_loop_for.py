"""
Loop for

Loop -> estruturas de repetição

For -> estrutura que itera sobre uma sequência
ou valores iteráveis.

Iteráveis:
- Strings
- Listas
- Range

Ranges são utilizados para gerar sequências numéricas não-aleatórias.

Sintaxe:

- range(valor_de_parada) -> valor inicial: 0; passo: 1 em 1 unidade.
Define um número limite de iterações. O valor de parada ou valor final NÃO é incluído.

- range(valor_de_início, valor_de parada) -> passo de 1 em 1 unidade.
Define um número limite de iterações dentro de um intervalo. O valor inicial é incluído, mas não o final.

-range(valor_de_início, valor_de_parada, passo)
Neste caso, todos os valores são especificados pelo programador.
Permanece a regra de inclusão e exclusão dos valores inicial e final, respectivamente.
Podemos ainda gerar passo negativo.

OBS.: Todos os valores devem ser INTEIROS.
"""

string = "Xablau"
lista = [1, 2, 3, 4, 5]

# Iteração em string
for letra in string:
    print(letra)

# Iteração sobre lista
for numero in lista:
    print(numero)

# Iteração sobre range
for numero in range(0, 10):
    print(numero)

# OBS.: dos valores passandos para a função range, inicial e final, o inicial é incluído, mas o valor final não.

for indice, letra in enumerate(string):
    print((indice, letra))

for indice, _ in enumerate(string):
    print(indice)

for _, letra in enumerate(string):
    print(letra)

"""
A função enumerate pega uma lista e separa em tuplas,
cada uma com o índice e o valor correspondente. Em string,
temos os pares ((0, X), (1, a), (2, b), (3, l), (4, a), (5, u))

Outra forma de escrever é usando '_' como parâmetro.
'_' é utilizado quando não precisamos de um valor.
"""

qtd = int(input("Executar loop quantas vezes? "))

for n in range(0, qtd + 1):
    print(f"Imprimindo... {n}")

qtd = int(input("Executar loop quantas vezes? "))
soma = 0

for n in range(0, qtd):
    num = int(input(f"Insira o {n}/{qtd} valor: "))
    soma += num
print(f"A soma é {soma}.")

for i in string:
    print(i, end='')

# O parâmtro end define como a função print vai encerrar a impressão de caracteres na tela. Por padrão, seu valor é \n.

emoji = "\U0001F60D"

for _ in range(3):
    for num in range(1, 11):
        print(emoji * num)