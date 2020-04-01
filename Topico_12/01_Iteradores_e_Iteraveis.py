"""
Iteradores e iteráveis em Python

 - Iterador (Iterator)
    -> Um objeto que pode ser iterável;
    -> Objeto que retorna um dado, sendo um por vez quando uma função next() é chamada.

 - Iterável (Iterable)
    -> Um objeto que retornará um iterator quando a função iter() for chamada.

Em um loop for que itera sobre uma lista, por exemplo, por baixo dos panos,
o que acontece é uma operação que transforma o iterável em iterador por meio
do cast iterador = iter(iterável). A seguir, é executada uma sequência de chamadas da
função next(iterador) para cada item no iterador, encerrando o processo após encontrar
o último item.
"""

# Exemplos de iteráveis, porém não iteradores:
nome = "Fulano"
numeros = [1, 2, 3, 4, 5]

print(nome)
print(numeros)

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
# OBS.: Tentar seguir com a função next caso já esteja no último elemento do iterável
# resultará em um erro do tipo StopIteration

# Ao usar um loop for para iterar sobre um objeto iterável, ocorre o mesmo processo:
for letra in nome:
    print(letra)  # Equivalente à sequência de print(next(it1)) acima.

for numero in numeros:
    print(numero)  # Equivalente à sequência de print(next(it2)) acima.
