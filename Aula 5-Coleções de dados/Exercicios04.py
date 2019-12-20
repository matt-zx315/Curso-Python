import math
import random
import statistics

#
# # LISTA 1:
# # Exercício 1: Criar um vetor que armazene 6 valores.
# A = [None, None, None, None, None, None]
#
# # item a) Armazenar os valores 1, 0, 5, -2, -5, 7.
# A[0] = 1
# A[1] = 0
# A[2] = 5
# A[3] = -2
# A[4] = -5
# A[5] = 7
#
# # item b) Armazenar o valor da soma de A[0], A[1] e A[5].
# A.append(A[0] + A[1] + A[5])
#
# # item c) Modificar o valor da posição 4 para 100.
# A[4] = 100
#
# # item d) Imprimir cada valor de A em uma linha.
# for valor in A:
#     print(valor)
#
# # Exercício 2: Ler 6 valores inteiros e imprimir os valores após a leitura.
# lista = []
#
# for i in range(0, 6):
#     valor = int(input("Digite um valor inteiro: "))
#     lista.append(valor)
#
# for valor in lista:
#     print(valor, end=', ')
#
# print('\b' * 2)
#
# # Exercício 3: Ler e armazenar em um vetor 10 valores reais, armazenar os quadrados em outro vetor e imprimir ambos.
# numeros = []
# quadrados = []
#
# for i in range(0, 10):
#     numero = float(input("Digite um número real: "))
#     numeros.append(numero)
#     quadrados.append(numero ** 2)
#
# for n in numeros, quadrados:
#     print(n)
#
# # Exercício 4: Ler um vetor de 8 posições e dois valores X e Y, representando duas posições. Imprimir a soma de X e Y.
# vetor = []
# x, y = 0, 0
#
# for i in range(0, 8):
#     numero = int(input("Digite um número inteiro: "))
#     vetor.append(numero)
#
# x = int(input("Digite um valor de 0 a 7: "))
# y = int(input("Digite um valor de 0 a 7: "))
#
# print(f"A soma de {vetor[x]} e {vetor[y]} é {vetor[x] + vetor[y]}.")
#
# # Exercício 5: Ler um vetor de 10 posições e contar quantos números pares existem.
# numeros = []
# pares = 0
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# for n in numeros:
#     if n % 2 == 0:
#         pares += 1
#
# print(f"No vetor de números, foram encontrado {pares} números pares.")
#
# # Exercício 6: Receber 10 valores, armazenar e imprimir o menor e maior valor.
# numeros = []
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# print(f"O maior valor foi {max(numeros)} e o menor valor foi de {min(numeros)}.")
#
# # Exercício 7: Ler 10 elementos, armazenar e imprimir o maior valor e a a sua posição.
# numeros = []
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# print(f"O maior valor encontrado foi {max(numeros)} na posição {numeros.index(max(numeros))}.")
#
# # Exercício 8: Ler 6 valores e imprimir na ordem inversa.
# numeros = []
#
# for i in range(0, 6):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# print(numeros[::-1])
#
# # Exercício 9: Ler 6 valores pares, armazenar e imprimir na ordem inversa.
# numeros = []
#
# while len(numeros) < 6:
#     numero = int(input("Digite um número inteiro: "))
#     if numero % 2 == 0:
#         numeros.append(numero)
#
# print(numeros[::-1])
#
# # Exercício 10: Ler 15 notas de alunos, armazenar e imprimir a média.
# notas = []
#
# for i in range(0, 15):
#     nota = float(input("Digite um número inteiro: "))
#     notas.append(nota)
#
# print(f"A média dos alunos foi de {round(sum(notas) / len(notas), 2)} pontos.")
#
# # Exercício 11: Ler 10 inteiros, armazenar, imprimir o total de valores negativos e a soma dos positivos.
# numeros = []
# negativos, soma_positivos = 0, 0
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# for n in numeros:
#     if n < 0:
#         negativos += 1
#     else:
#         soma_positivos += n
#
# print(f"Foram encontrados {negativos} números negativos, enquanto a soma dos positivos foi {soma_positivos}.")
# # Exercício 12: Ler 5 valores, armazenar e imprimir todos os valores, o maior, o menor e a média.
# numeros = []
# mensagem = f"Os valores armazenados foram:\n"
#
# for i in range(0, 5):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# for i in numeros:
#     mensagem += f"{i}  "
#
# mensagem += f"\nO maior valor foi {max(numeros)}, o menor valor foi {min(numeros)}" \
#             f"e a média foi {sum(numeros) / len(numeros)}."
#
# print(mensagem)
#
# # Exercício 13: Ler 5 valores, armazenar e imprimir as posições do maior e menor valor.
# numeros = []
#
# for i in range(0, 5):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# print(f"O maior valor está na posição {numeros.index(max(numeros))}, "
#       f"enquanto o menor valor está na posição {numeros.index(min(numeros))}.")
#
# # Exercício 14: Ler 10 valores, armazenar e imprimir valores iguais na tela.
# numeros = []
# repetidos = []
# n = 0
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# for n in numeros:
#     if numeros.count(n) > 1 and n not in repetidos:
#         repetidos.append(n)
#
# if len(repetidos) > 0:
#     print("Os valores")
#     for c in repetidos:
#         print(c, end=', ')
#
#     print('\b' * 2 + " se repetem na lista.")
# else:
#     print("Não há valores repetidos na lista.")
#
# # Exercício 15: Ler 20 números e imprimir os valores, exceto repetidos.
# numeros = []
# elementos = set({})
#
# for i in range(0, 20):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# for n in numeros:
#     elementos.add(n)
#
# print(elementos)
#
# # Exercício 16: Ler 5 reais e armazenar. Ler um inteiro a seguir: 0 = encerrar 1 = ordem direta, 2 = ordem inversa.
# numeros = []
#
# for i in range(0, 5):
#     numero = float(input("Digite um número real: "))
#     numeros.append(numero)
#
# comando = int(input("Instruções:\n0-Encerrar\n1-Imprimir lista em ordem direta.\n2-Imprimir na ordem inversa.\n"))
#
# if comando == 0:
#     print("Encerrando...")
# elif comando == 1:
#     print(numeros)
# elif comando == 2:
#     print(numeros[::-1])
# else:
#     print("Comando inválido. Encerrando.")
#
# # Exercício 17: Ler 10 valores e armazenar. Atribuir 0 para todos os valores negativos.
# numeros = []
#
# for i in range(0, 10):
#     numero = int(input("Digite um número inteiro: "))
#     if numero < 0:
#         numeros.append(0)
#     else:
#         numeros.append(numero)
#
# print(numeros)
#
# # Exercício 18: Ler 10 valores e armazenar. Ler um inteiro X, contar seus múltiplos e os imprimir em um vetor.
# numeros = []
# multiplos_x = []
#
# for i in range(0, 10):
#     numero = float(input("Digite um número real: "))
#     numeros.append(numero)
#
# x = int(input("Digite um número: "))
#
# for n in numeros:
#     if n % x == 0:
#         multiplos_x.append(n)
#
# print(f"Os múltiplos de {x} encontrados foram: {multiplos_x}.")
#
# # Exercício 19: Criar um vetor de tamamnho 50. Seus valores serão: (i + 5i)%(i + 1), sendo i a posição no vetor.
# vetor = []
#
# for i in range(0, 50):
#     vetor.append(None)
#     vetor[i] = (i + 5 * i) % (i + 1)
#
# print(vetor)
#
# # Exercício 20: Ler números de 0 a 50 e armazenar num vetor de 10 posições. Preencher outro vetor com os valores ímpares
# # e imprimir dois valores por linha.
# vetor = []
# impares = []
#
# while len(vetor) < 10:
#     numero = int(input("Digite um número de 0 a 50: "))
#     # numero = random.randint(0, 51)
#
#     if 0 <= numero <= 50:
#         vetor.append(numero)
#     else:
#         print("Número inválido!")
#
# for v in vetor:
#     if v % 2 == 1:
#         impares.append(v)
#
# print(impares)
#
# for i in impares:
#     if impares.index(i) % 2 == 0:
#         print(i, end=' ')
#     else:
#         print(i, end='\n')
#
# # Exercício 21: Criar dois vetores A e B que recebem 10 valores cada. Criar e imprimir um vetor C que é a soma de A e B.
# A, B = [], []
#
# for n in range(0, 10):
#     numero_a = int(input("Digite um valor para o vetor A: "))
#     A.append(numero_a)
#     numero_b = int(input("Digite um valor para o vetor B: "))
#     B.append(numero_b)
#
# C = A + B
# print(C)
#
# # Exercício 22: Repetir ex. 21. No vetor C, colocar nas posições pares os valores de A e nas ímpares os de B.
# A, B, C = [], [], []
# index_a, index_b, index_c = 0, 0, 0
#
# for n in range(0, 10):
#     numero_a = int(input("Digite um valor para o vetor A: "))
#     A.append(numero_a)
#     numero_b = int(input("Digite um valor para o vetor B: "))
#     B.append(numero_b)
#
# while len(C) < 20:
#     C.append(None)
#     if index_c % 2 == 0:
#         C[index_c] = A[index_a]
#         index_a += 1
#     else:
#         C[index_c] = B[index_b]
#         index_b += 1
#
#     index_c += 1
#
# print(C)
#
# # Exercício 23: Ler 2 conjuntos de 5 números reais cada e armazenar. Imprimir o produto escalar dos dois vetores.
# vetor_a, vetor_b = [], []
# produto_escalar = 0
#
# for i in range(0, 5):
#     numero_a = float(input("Digite um valor real para o vetor A: "))
#     vetor_a.append(numero_a)
#     numero_b = float(input("Digite um valor real para o vetor B: "))
#     vetor_b.append(numero_b)
#
# for n in range(0, len(vetor_a)):
#     produto_escalar += vetor_a[n] * vetor_b[n]
#
# print(f"O produto escalar dos vetores:\nA = {vetor_a}\nB = {vetor_b}\né {produto_escalar}.")
#
# # Exercício 24: Ler 2 conjuntos: um número de aluno e sua altura. Encontrar os números e alturas dos mais baixo e alto.
# numeros, alturas = [], []
# alunos = {}
#
# for r in range(0, 10):
#     numero = int(input("Insira o número do aluno: "))
#     numeros.append(numero)
#     altura = float(input("Digite o valor da altura: "))
#     alturas.append(altura)
#
# while len(alunos) < 10:
#     alunos[numeros[len(alunos)]] = alturas[len(alunos)]
#
# print(alunos)
#
# # Exercício 25: Preencher um vetor com os 100 primeiros números naturais não múltiplos de 7 ou terminados em 7.
# numeros = []
# numero = 0
#
# while len(numeros) < 100:
#     if numero % 7 != 0 and numero % 10 != 7:
#         numeros.append(numero)
#     numero += 1
#
# for n in numeros:
#     if numeros.index(n) % 10 == 0:
#         print(n)
#     else:
#         print(n, end=' ')
#
# # Exercício 26: Calcular o desvio padrão de um vetor de 10 posições.
# vetor = []
# desvio, media, variancia = 0, 0, 0
#
# while len(vetor) < 10:
#     vetor.append(random.randint(0, 101))
#
# media = sum(vetor) / len(vetor)
#
# for valor in vetor:
#     variancia += (valor - media) ** 2
#
# desvio = math.sqrt(variancia / (len(vetor) - 1))
# print(desvio)
#
# # Jeito simples: statistics.stdev(vetor). Também pode ser usada pra saber se o cálculo está correto.
# desvio = statistics.stdev(vetor)
# print(desvio)
#
# # Exercício 27: Ler 10 valores e armazenar. imprimir os valores primos e suas posições no vetor.
# numeros = []
#
# for i in range(0, 10):
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
#
# for num in numeros:
#     divisores = 0
#
#     for n in range(1, num + 1):
#         if num % n == 0:
#             divisores += 1
#
#     if divisores == 2:
#         print(f"Número primo encontrado na posição {numeros.index(num)} ({num}).")
#
# # Exercício 28: Ler 10 valores e armazenar. Copiar os valores pares e ímpares pra dois novos vetores e imprimir.
# v, v1, v2 = [], [], []
#
# while len(v) < 10:
#     numero = int(input("Digite um número inteiro: "))
#     v.append(numero)
#
# for n in v:
#     if n % 2 == 0:
#         v2.append(n)
#     else:
#         v1.append(n)
#
# if len(v1) > 0:
#     print(f"O vetor v1 possui {len(v1)} elementos: {v1}")
# if len(v2) > 0:
#     print(f"O vetor v2 possui {len(v2)} elementos: {v2}")
#
# # Exercício 29: Ler 6 ímpares e armazenar. Exibir...
# numeros = []
#
# while len(numeros) < 6:
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
#
# # item a: os números pares digitados:
# print("Os números pares encontrados foram: ")
# for n in numeros:
#     if n % 2 == 0:
#         print(n, end=' ')
#
# # item b: exibir a soma dos números pares.
# soma_pares = 0
#
# for n in numeros:
#     if n % 2 == 0:
#         soma_pares += n
#
# print(soma_pares)
#
# # item c: os números ímpares digitados:
# print("Os números ímpares encontrados foram: ")
# for n in numeros:
#     if n % 2 == 1:
#         print(n, end=' ')
#
# # item d: a quantidade de números ímpares digitados.
# quantidade_impares = 0
#
# for n in numeros:
#     if n % 2 == 1:
#         quantidade_impares += 1
#
# print(f"\nForam encontrados {quantidade_impares} números ímpares.")
#
# # Exercício 30: Ler 2 vetores de 10 elementos. Criar um novo vetor que seja a instersecção dos outros 2, sem repetição.
# numeros1, numeros2 = [], []
#
# while len(numeros1) < 10 and len(numeros2) < 10:
#     numero = int(input("Digite um número para o vetor 1: "))
#     numeros1.append(numero)
#     numero = int(input("Digite um número para o vetor 2: "))
#     numeros2.append(numero)
#
# numeros1 = set(numeros1)
# numeros2 = set(numeros2)
# print(f"A intersecção entre os conjuntos 1 e 2 tem como elementos: {numeros1 & numeros2}.")
#
# # Exercício 31: Ler 2 vetores de 10 elementos. Criar um novo vetor que seja a união dos outros 2.
# numeros1, numeros2 = [], []
#
# while len(numeros1) < 10 and len(numeros2) < 10:
#     numero = int(input("Digite um número para o vetor 1: "))
#     numeros1.append(numero)
#     numero = int(input("Digite um número para o vetor 2: "))
#     numeros2.append(numero)
#
# numeros1 = set(numeros1)
# numeros2 = set(numeros2)
# print(f"A união entre os conjuntos 1 e 2 tem como elementos: {numeros1 | numeros2}.")
#
# # Exercício 32: Ler 2 vetores X e Y, de 5 elementos cada. Calcular e imprimir:
# x, y = [], []
#
# while len(x) < 5 and len(y) < 5:
#     # numero = int(input("Digite um número para o vetor 1: "))
#     # x.append(numero)
#     # numero = int(input("Digite um número para o vetor 2: "))
#     # y.append(numero)
#
#     numero = random.randint(0, 16)
#     x.append(numero)
#     numero = random.randint(0, 16)
#     y.append(numero)
#
# print(x)
# print(y)
#
# # item a: O vetor resultante da soma de cada elemento de X com o elemento na mesma posição de Y.
# soma = []
#
# for i in range(0, 5):
#     soma.append(x[i] + y[i])
#
# print(soma)
#
# # item b: O vetor resultante da multiplicação de cada elemento de X com o elemento na mesma posição de Y.
# produto = []
#
# for i in range(0, 5):
#     produto.append(x[i] * y[i])
#
# print(produto)
#
# # item c: O vetor resultante da diferença (elementos que existem em um vetor e não no outro) entre X e Y.
# x = set(x)
# y = set(y)
#
# diferenca_x = tuple(x.difference(y))
# diferenca_y = tuple(y.difference(x))
#
# print(diferenca_x)
# print(diferenca_y)
#
# # item d: intersecção de X e Y.
# interseccao = tuple(x & y)
#
# print(interseccao)
#
# # item e: união de X e Y.
# uniao = tuple(x | y)
#
# print(uniao)
#
# # Exercício 33: Ler um vetor de 15 posições e remover o valor 0 de todas as posições.
# numeros = []
#
# while len(numeros) < 15:
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
#
# print(numeros)
#
# for n in numeros:
#     if n == 0:
#         numeros.remove(n)
#
# print(numeros)
#
# # Exercício 34: Ler 10 valores DIFERENTES, armazenar, verificar a cada leitura se o valor já existe no vetor e imprimir.
# numeros = []
#
# while len(numeros) < 10:
#     numero = int(input("Digite um número: "))
#     if numero not in numeros:
#         numeros.append(numero)
#     else:
#         print("Valor repetido!")
#
# print(numeros)
#
# # Exercício 35: Ler 2 valores A e B (positivos e menores que 10.000) e armazenar seus algarismos em vetores.
# A, B = [], []
# soma = 0
#
# while True:
#     if len(A) == 0:
#         a = int(input("Digite um número positivo e menor que 10.000: "))
#
#         if a <= 0 or a >= 10_000:
#             print("Número inválido!")
#         else:
#             print(a)
#             A.append(a)
#             soma += a
#     elif len(B) == 0:
#         b = int(input("Digite um número positivo e menor que 10.000: "))
#
#         if b <= 0 or b >= 10_000:
#             print("Número inválido!")
#         else:
#             print(b)
#             B.append(b)
#             soma += b
#     else:
#         print(soma)
#         break
#
# # item a: criar um vetor no qual cada posição é um algarismo. A primeira posição é o algarismo menso significativo.
# A = list(str(A[0]))[::-1]
# B = list(str(B[0]))[::-1]
#
# for n in range(0, len(A)):
#     A[n] = int(A[n])
#
# for n in range(0, len(B)):
#     B[n] = int(B[n])
#
# print(A)
# print(B)
#
# # item b: criar um vetor que seja a soma de A e B.
# # DICA: Caso a soma seja maior que 9, subtrair 10 de uma posição e somar 1 na próxima.
# C = [0, 0, 0, 0, 0]
#
# if len(A) < len(B):
#     for c in range(0, len(A)):
#         C[c] = A[c] + B[c]
# elif len(B) < len(A):
#     for c in range(0, len(B)):
#         C[c] = A[c] + B[c]
# else:
#     for c in range(0, len(A)):
#         C[c] = A[c] + B[c]
#
# for i in range(0, len(C)):
#     if 10 <= C[i] < 20:
#         C[i] -= 10
#         C[i + 1] += 1
#
# print(C)
#
# # Exercício 36: Ler um vetor de 10 posições, ordenar e imprimir.
# numeros = []
#
# while len(numeros) < 10:
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
#
# numeros.sort()
# print(numeros)
#
# # Exercício 37: Ordenar um vetor de 11 posições em ordem crescente até o 6º elemento e em ordem decrescente o restante.
# numeros = []
#
# while len(numeros) < 11:
#     numero = random.randint(0, 100)
#     numeros.append(numero)
#
# numeros.sort()
# print(numeros)
# reverso = numeros[5::]
# reverso.reverse()
#
# for i in range(0, len(reverso)):
#     numeros[i + 5] = reverso[i]
#
# print(numeros)
#
# # Exercício 38: Ler 10 valores e armazenar. Ordenar cada valor assim que digitado.
# numeros = []
#
# while len(numeros) < 10:
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)
#     numeros.sort()
#
# print(numeros)
#
# # Exercício 39: Ler um número natural N e imprimir o triângulo de Pascal.
# lista = []
#
# linhas = int(input("Digite um número natural. "))
#
# if linhas <= 0:
#     print("Encerrando...")
# else:
#     lista = [[1], [1, 1]]
#     for i in range(1, linhas):
#         linha = [1]
#         print(i)
#
#         for j in range(0, len(lista[i]) - 1):
#             print(j)
#             print(f"{lista[i][j]} + {lista[i][j + 1]}")
#             linha += [lista[i][j] + lista[i][j + 1]]
#             print(linha)
#
#         linha += [1]
#         lista += [linha]
#         print(f"Linha {i + 1} => {linha}")
#         print(lista)
#
# for lin in lista:
#     print(lin)
#
# # LISTA 02
# # Exercício 1: Ler uma matriz 4 x 4, contar e escrever quantos números maiores que 10 ela possui.
# matriz = [[], [], [], []]
# maior_10 = 0
#
# for i in range(0, 4):
#     for j in range(0, 4):
#         numero = random.randint(0, 100)
#         matriz[i].append(numero)
#
# for i in range(0, 4):
#     for j in range(0, 4):
#         if matriz[i][j] > 10:
#             maior_10 += 1
#
# print(f"Na matriz 4 x 4 há {maior_10} valores maiores que 10.")
#
# # Exercício 2: Fazer uma matriz 5 x 5, preencher a diagonal principal com 1 e o restante com 0.
# matriz = [[], [], [], [], []]
#
# for i in range(0, 5):
#     for j in range(0, 5):
#         if i == j:
#             matriz[i].append(1)
#         else:
#             matriz[i].append(0)
#
# for m in matriz:
#     print(m)
#
# # Exercício 3: Preencher uma matriz 4 x 4 com o produto do valor de linha e coluna.
# matriz = [[], [], [], []]
#
# for i in range(0, 4):
#     for j in range(0, 4):
#         matriz[i].append(i * j)
#
# for m in matriz:
#     print(m)
#
# # Exercício 4: Ler uma matriz 4 x 4, imprimir e retornar a posição do maior valor.
# matriz = [[], [], [], []]
# valores = {}
# posicao = None
#
# for i in range(0, 4):
#     for j in range(0, 4):
#         numero = random.randint(0, 100)
#         matriz[i].append(numero)
#
# for m in matriz:
#     print(m)
#
# for linha in range(0, len(matriz)):
#     lin, col = linha, 0
#
#     for coluna in range(0, len(matriz[linha])):
#         col = coluna
#         posicao = (lin, col)
#         valores[matriz[linha][coluna]] = posicao
#
#
# print(f"O valor máximo da matriz ({max(valores.keys())}) 4 x 4 está na posição {valores[max(valores.keys())]}.")

# Exercício 5: Ler uma matriz 5 x 5 e um valor X. Procurar X e retornar uma mensagem se o valor foi encontrado ou não.
matriz = [[], [], [], [], []]
X = int(input("Digite um número: "))
encontrado = False

for lin in range(0, 5):
    for col in range(0, 5):
        numero = random.randint(0, 100)
        matriz[lin].append(numero)

for lin in matriz:
    print(matriz[matriz.index(lin)])
    if X in matriz[matriz.index(lin)]:
        print(f"O valor {X} foi encontrado.")
        break
    elif X not in matriz and matriz.index(lin) == len(matriz) - 1:
        print(f"O valor {X} não foi encontrado.")