"""
Tuplas são bastante parecidas com listas. Existem, basicamente, duas diferenças:

1-Tuplas são representadas por parênteses. Sintaxe: tupla = ()
2-São imutáveis, ou seja, após criadas, não é possível mudar seus valores.
Toda operação em uma tupla gera uma nova tupla.

Podem ser escritas também como uma sequência de elementos separados por vírgula e sem parenteses.

Tuplas de um elemento devem ser escritas com o elemento seguido de vírgula: tupla(elemento,)
caso contrário serão consideradas como um tipo diferente de dado. São definidas pelo uso da
vírgula, não pelo parênteses.
"""

tupla0 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla0)
print(type(tupla0))

tupla1 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(tupla1)
print(type(tupla1))

tupla2 = (4)  # Não é uma tupla.
print(tupla2)
print(type(tupla2))

tupla3 = (4,)  # É uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = 4,
print(tupla4)
print(type(tupla4))

tupla5 = tuple(range(10))
print(tupla5)
print(type(tupla5))

# Desempacotamento de tupla:
tupla = ("Geek University", "Programação em Python: Essencial")
escola, curso = tupla
print(escola, end=' ')
print(curso)

tupla6 = (1, True, "Água", 16.5)
print(tupla6)
print(type(tupla6))

# É possível realizar operações de Máximo*, Mínimo*, Soma* e tamanho em tuplas. (*apenas com valores inteiros ou reais)

print(sum(tupla1))  # Soma
print(max(tupla1))  # Valor máximo
print(min(tupla1))  # Valor mínimo
print(len(tupla1))  # Tamanho

tupla0 = (0, 2, 4, 6, 8)
tupla1 = (1, 3, 5, 7, 9)

print(tupla0 + tupla1)
print(tupla0)
print(tupla1)

# É possível SOBRESCREVER uma tupla, porém é impossível alterar o(s) valor(es) de uma tupla já criada.
tupla0 = tupla1 + tupla0
print(tupla0)

# Verificar se há um determinado elemento na tupla.
print(3 in tupla5)
print(12 in tupla5)

if 4 in tupla5:
    print("Encontrado")
else:
    print("Não encontrado")

# Iterando sobre uma tupla.
for n in tupla5:
    print(n)

for indice, valor in enumerate(tupla6):
    print(indice, valor)

# Contando elementos
tupla = "Nepuruzugya"
tupla = tuple(tupla)
print(tupla.count('z'))

"""
Dicas na utilização de tuplas:

1-Devemos utilizá-las SEMPRE que não precisarmos modificar os dados contidos em uma coleção.
2-O acesso de elementos também é semelhante ao de uma lista.
3-Podemos encontrar os índices dos elementos.
4-Slice também é possível em tuplas. Segue as mesmas regras das listas.
5-Não possui o problema de shallow copy.

Por quê utilizar tuplas:

-São mais rápidas do que listas. A performance do programa é melhor.
-Deixam o código mais seguro. Por serem imutáveis, os dados correm menos risco de sofrerem alterações.
"""

# Dica 1:
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Dica 2:
print(meses[2])

# Dica 3:
print(meses.index("Agosto"))

# Dica 4:
print(meses[::2])
print(meses[1::2])
print(meses[:9:2])

# Dica 5:
tupla = 1, 2, 3
print(tupla)

nova = tupla
print(nova)

outra = 4, 5, 6
print(outra)

nova = nova + outra
print(nova)
print(tupla)