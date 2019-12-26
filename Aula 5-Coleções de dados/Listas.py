"""
Listas em Python funcionam como vetores e matrizes (arrays) em outras linguagens.
São DINÂMICAS e MUTÁVEIS, podendo colocar QUALQUER tipo de dado.

-Dinâmica = não tem tamanho fixo. Você pode adicionar elementos enquanto houver memória disponível.
-Mutáveis = seus valores podem ser alterados, novos valores podem ser adicionados e valores podem ser removidos.
-Qualquer tipo de dado = não tem tipo de dado fixo. Podemos, inclusive, misturar vários tipos de dados.

Sintaxe:
lista = []
"""

lista0 = [1, True, "Água", 16.5]
lista1 = [0, 1, 2, 3, 4, 5]
lista2 = ['N', 'e', 'p', 'u']
lista3 = []
lista4 = list(range(6))
lista5 = list("Nepu")

# Função list(parâmetro) -> Gera uma lista a partir do parâmetro inserido. Retorna uma lista vazia caso não receba nada.

print(lista0)
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

if 8 in lista1:
    print("8 encontrado na lista 1.")
else:
    print("8 não encontrado na lista 1.")

if 'N' in lista2:
    print("N encontrado na lista 2.")
else:
    print("N não encontrado na lista 2.")

# Palavra-chave in é utilizada para encontrar elementos em uma lista.

lista6 = [2, 8, 9, 0, 4, 6, 1, 3, 7, 5]
lista6.sort()
print(lista6)

lista7 = list("Nepuruzugya, 1432")
lista7.sort()
print(lista7)

"""
Método sort(lista) -> organiza os itens em ordem crescente/alfabética*. Deve ser invocado ANTES da função print.
*Para strings, a ordem é pontuação, números, caracteres maiúsculos, minúsculos, caracteres acentuados, caracteres
especiais.
"""

print(lista7.count('u'))

# Método count(elemento) -> conta o número de repetições de um determinado elemento.

lista8 = ["banana", "maçã", "limão"]
print(lista8)
lista8.append("laranja")
print(lista8)

# Método append(elemento) -> adiciona um elemento no final lista. Apenas um elemento por chamada do método.

lista8.append(["uva", "mamão"])
print(lista8)

# Uma lista foi adicionada dentro da outra como um novo elemento.

if ["uva", "mamão"] in lista8:
    print("Lista encontrada.")
else:
    print("Lista não encontrada.")

# Podemos procurar listas dentro de listas.

lista8.extend(["uva", "mamão"])
print(lista8)

lista9 = []
lista9.extend(lista6)
lista9.extend("Nepuruzugya")
print(lista9)

"""
Método extend(lista) -> insere os dados de uma lista em outra lista.
Não aceita valor único (exceto lista de um elemento). Pode ser usada com strings também.
"""

lista8.insert(3, "morango")
print(lista8)

"""
Método insert(posição, elemento) -> insere um novo elemento numa posição já existente da lista.
Não substitui o valor original, o qual será deslocado para a direita (posição seguinte).
"""

lista9 = lista6 + lista7
print(lista9)
lista8 += ["kiwi", "coco"]
print(lista8)

# Somar listas funciona como o extend (+=) ou para criar uma lista que junte os dados de várias (lista1 + lista2).

lista6.reverse()
print(lista6)
print(lista6[:: -1])

# Reverse troca os valores de posição, escrevendo-os na ordem inversa. Podemos também usar o slice.

lista9 = lista0.copy()
print(lista9)
print(lista9 is lista0)

"""
O método copy() permite criar uma cópia de uma lista para atribuir a outra lista.
Diferente de uma atribuíção direta (lista9 = lista0), o uso desse método permite
a criação de uma lista inteiramente nova, cujos valores podem ser alterados sem
que os valores da lista original sofram quaisquer alterações. Para confirmar isso,
basta usar o comparador is. Se o retorno for False, significa que a lista que recebeu
a cópia da original é uma lista nova e com valores independetes. Caso o retorno seja
True, a lista nova é um ponteiro e quaiquer alterações nessa afetarão a lista original.
"""

print(len(lista6))

# A função len(lista) retorna o número de elementos de uma lista.

print(lista9.pop())
print(lista9)
print(lista9.pop(0))
print(lista9)

"""
Método pop() -> remove o último elemento da lista. Ele também retorna o elemento removido.
Pode ser usado, ainda, para remover por índice. Ao fazer isso, ele desloca os outros
elementos da lista para a esquerda (um índice antes).
Se não existir um elemento na posição indicada no método, um teremos um erro (IndexError)
"""

lista8.remove(["uva", "mamão"])
print(lista8)

# Método remove(elemento) -> remove o elemento especificado como parâmetro.

lista9.clear()
print(lista9)

# Método clear() -> apaga TODOS os elementos da lista.

lista9 = lista1 * 3

# Podemos multiplicar listas por números para repetir seus elementos.

mensagem = "I don't give a fuck!"
print(mensagem)
mensagem = mensagem.split()
print(mensagem)

# Sperar uma string com split() transforma seus elementos em listas. Por padrão, as palavras são separadas por espaços.

mensagem = "O rato roeu a roupa do rei de roma."
print(mensagem)
mensagem = mensagem.split('r')
print(mensagem)

# Separação também ocorre quando passamos um caractere como parâmetro. Este caractere é removido no processo.

mensagem = 'r'.join(mensagem)
print(mensagem)

"""
Transformando uma lista em uma string. Para isso, usamos um carctere que servirá para unir os elementos,
em seguida usamos o método join(lista) para unir os elementos. O caracter pode ser um espaço, uma letra,
um cifrão ou qualquer outra coisa. Pode até mesmo ser um texto inteiro.
"""

# Iterando sobre uma lista.
for item in lista8:
    print(item)

# Somando itens:
soma = 0

for numero in lista6:
    soma += numero

print(soma)

# Com while:
cesta = []
fruta = ''

while fruta != 'sair':
    fruta = input("Nome da fruta: ")
    cesta.append(fruta)

cesta.pop()
print(cesta)

# Inserindo variáveis:
num0, num1, num2, num3, num4 = 0, 1, 2, 3, 4
lista9 = [num0, num1, num2, num3, num4]

print(lista9)

# Acessando elementos por índice:
cores = ["laranja", "roxo", "verde", "azul", "amarelo", "vermelho", "marrom", "rosa", "branco", "preto"]

print(cores[0])
print(cores[4])
print(cores[6])
print(cores[8])
print(cores[-3])  # Acesso ao terceiro elemento de trás para a frente.
print(cores[-10])

for cor in cores:
    print(cor, end=', ')

print('\b' * 2)

# Descobrindo os índices:
for indice, cor in enumerate(cores):
    print(indice, cor)

"""
enumerate(lista) cria pares de chaves e valores para cada elemento da lista.
Podemos usar _ caso não queiramos saber um dos valores.
"""

# Listas aceitam valores repetidos:
lista9.append(0)
lista9.append(0)
lista9.append(2)
lista9.append(4)

print(lista9)

# Contando elementos
print(lista7.count('u'))

# Outros métodos úteis:

# 1-Encontrar o índice do elemento na lista.
print(cores.index("roxo"))
print(cores.index("laranja"))

print(lista9.index(2))  # Retorna o índice do primeiro elemento encontrado com o valor passado.

# Busca por range:
print(lista9.index(0, 1))  # Buscando a partir do índice 1
print(lista9.index(4, 6, 9))  # Buscando dentro do intervalo de 6 a 8 (9 não é considerado).

# OBS.: Caso não exista o elemento na lista ou com o determinado índice, será apresentado um erro do tipo ValueError.

# 2-Slice
# Sintaxe: lista[início : fim : passo] ou range[início : fim : passo]. OBS: início < fim SEMPRE!

print(cores[1:])  # Corre a lista a partir do parâmetro início.
print(cores[:4])  # Exibe a lista até o elemento fim - 1.
print(cores[::2])  # Corre a lista de X em X itens, com X sendo o valor do passo.

print(cores[3:8])  # Exibe a lista de início até o elemento fim - 1.
print(cores[1::2])  # Corre a lista a partir do parâmetro início de acordo com o valor do passo.
print(cores[:8:3])  # Corre a lista até o elemento fim - 1 de acordo com o passo.

print(cores[2:7:3])  # Trabalhando com os três parâmetros. Segue as regras dos parâmetros fim e passo.

# Com valores negativos:
print(cores[-1:])  # Exibe os elementos da lista a partir do último.
print(cores[:-4])  # Exibe todos os elementos da lista menos os do parâmetro fim.
print(cores[::-2])  # Corre a lista de trás para frente de acordo com o passo.

print(cores[-9:-1])  # Corre a lista do mesmo jeito que com valores positivos. Lembrar que início < fim.
print(cores[-7::-2])  # Corre a lista do mesmo jeito que com valores positivos.
print(cores[:-5:-2])  # Mesma coisa aqui.

print(cores[-1:-8:-2])  # Com passo negativo, início > fim.

"""
Quando o sinal do passo é o oposto dos sinais de início e fim
(ambos SEMPRE devem ter o MESMO sinal, seja + ou -), a lista
será invertida.

Por exemplo, a lista cores, de 10 elementos:

0 ou -10 laranja
1 ou -9 roxo
2 ou -8 verde
3 ou -7 azul
4 ou -6 amarelo
5 ou -5 vermelho
6 ou -4 marrom
7 ou -3 rosa
8 ou -2 branco
9 ou -1 preto

OBS.: Vale lembrar que, no caso de passo com sinal trocado,
a saída continua sendo fim - 1. A inversão ocorre APÓS
a lista ser varrida.
"""
print(cores[-7::2])
print(cores[:-5:2])
print(cores[-8:-1:2])  # Com passo positivo, voltar à regra de início < fim.

# 3-Soma*, máximo*, mínimo*, tamanho (*Apenas valores inteiros ou reais)

print(sum(lista6))  # Soma
print(max(lista6))  # Valor máximo
print(min(lista6))  # Valor mínimo
print(len(lista6))  # Tamanho

# 4-Conversão para tupla

tupla = tuple(lista6)
print(lista6)
print(type(lista6))
print(tupla)
print(type(tupla))

# 5-Desempacotamento de listas. O número de variáveis deve ser IGUAL ao de elementos da lista, se não, ValueError.

lista9 = [0, 1, 2]
num0, num1, num2 = lista9
print(num0)
print(num1)
print(num2)

# 6-Cópia de listas (Shallow Copy e Deep Copy)

# Deep Copy: cópia de listas na qual as duas listas são independentes, ou seja, as alterações de uma não afetam a outra.
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(nova)

# Shallow Copy: nesse modelo de cópia, uma lista, quando alterada, altera também a outra.
nova = lista
print(lista)
print(nova)

nova.append(4)
print(lista)
print(nova)

lista.append(5)
print(lista)
print(nova)