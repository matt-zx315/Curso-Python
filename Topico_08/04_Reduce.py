"""
Reduce

OBS.: A partir do Python 3, a função reduce() não é mais uma função integrada (built-in).
Para utilizar essa função, é necessário importá-la do módulo functools.

Guido van Rossum: "Utilize a função reduce() se você realmente precisar dela.
Em todo caso, 99% das vezes, um loop for é mais legível."

Entendendo o reduce()

Imagine uma coleção de dados:
dados = [a1, a2. a3 ... an]

E uma função que recebe dois parâmetros:

def função(x, y):
    return x * y

Assim como map() e filter(), reduce também recebe como paramêtros uma função e um iterável.

Sintaxe: reduce(função, iterável)

Funcionamento de reduce():

    Passo 1: res1 = função(a1, a2) -> Aplica a função nos dois primeiros números e guarda o resultado.
    Passo 2: res2 = função(res1, a3) -> Aplica a função no resultado anterior e no terceiro dado, guardadno o resultado.
    Passo 3: res 3 = função(res2, a4)
    ...
    Passo n-1: res n-1 = função(resn-2, an)

Em cada passo, ela aplica a função, passando como primeiro argumento o resultado da aplicação anterior.
No último passo (n-1), reduce() retorna o resultado final.

Outra forma de explicar reduce():

função(...função(função(a1, a2), a3), ... an)

OBS.: reduce() trabalha com funções que recebem DOIS parâmetros.
"""
from random import randint
from functools import reduce

# Na prática:
dados = []

for i in range(10):
    num = randint(0, 50)
    dados.append(num)

print(dados)

res = reduce(lambda x, y: x * y, dados)
print(res)