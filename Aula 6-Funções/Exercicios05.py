from random import randint

# # Exercício 1: Criar uma função que recebe um número e retorna seu dobro.
#
#
# def retorna_dobro(numero):
#     return numero * 2
#
#
# print(retorna_dobro(5))
#
# # Exercício 2: Receber data e retornar. Exemplo: 01/01/2000 retorna 1 de Janeiro de 2000
#
#
# def exibe_data(dia, mes, ano):
#     if dia < 1:
#         return "Dia inválido!"
#     else:
#         if mes == 1:
#             if dia <= 31:
#                 mes = "Janeiro"
#             else:
#                 return "Dia inválido!"
#         elif mes == 2:
#             if dia <= 28 and ano % 4 != 0:
#                 mes = "Fevereiro"
#             elif dia == 29 and (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0):
#                 mes = "Fevereiro"
#             else:
#                 return "Dia inválido!"
#         elif mes == 3:
#             if dia <= 31:
#                 mes = "Março"
#             else:
#                 return "Dia inválido!"
#         elif mes == 4:
#             if dia <= 30:
#                 mes = "Abril"
#             else:
#                 return "Dia inválido!"
#         elif mes == 5:
#             if dia <= 31:
#                 mes = "Maio"
#             else:
#                 return "Dia inválido!"
#         elif mes == 6:
#             if dia <= 30:
#                 mes = "Junho"
#             else:
#                 return "Dia inválido!"
#         elif mes == 7:
#             if dia <= 31:
#                 mes = "Julho"
#             else:
#                 return "Dia inválido!"
#         elif mes == 8:
#             if dia <= 31:
#                 mes = "Agosto"
#             else:
#                 return "Dia inválido!"
#         elif mes == 9:
#             if dia <= 30:
#                 mes = "Setembro"
#             else:
#                 return "Dia inválido!"
#         elif mes == 10:
#             if dia <= 31:
#                 mes = "Outubro"
#             else:
#                 return "Dia inválido!"
#         elif mes == 11:
#             if dia <= 30:
#                 mes = "Novembro"
#             else:
#                 return "Dia inválido!"
#         elif mes == 12:
#             if dia <= 31:
#                 mes = "Dezembro"
#             else:
#                 return "Dia inválido!"
#         else:
#             return "Mês inválido!"
#
#     return f"{dia} de {mes} de {ano}."
#
#
# print(exibe_data(1, 13, 2016))
#
# # Exercício 3: Verificar se um valor é positivo ou não. Retornar 1 se for positivo e 0 se for 0 ou negativo.
#
#
# def e_positivo(valor):
#     if valor > 0:
#         return 1
#     return 0
#
#
# print(e_positivo(6))
# print(e_positivo(0))
# print(e_positivo(-9))
#
# # Exercício 4: Verificar se um número é um quadrado perfeito.
#
#
# def quadrado_perfeito(quadrado):
#     raiz = quadrado ** (1 / 2)
#
#     if int(raiz) ** 2 == quadrado:
#         return f"{quadrado} é um quadrado perfeito."
#     return f"{quadrado} não é um quadrado perfeito."
#
#
# print(quadrado_perfeito(64))
# print(quadrado_perfeito(60))
#
# # Exercício 5: Receber o raio de uma esfera e calcular seu volume.
#
#
# def calcula_volume(raio):
#     volume = round((4 / 3) * 3.141592 * (raio ** 3), 3)
#     return volume
#
#
# print(calcula_volume(randint(0, 100)))
# print(calcula_volume(randint(0, 100)))
# print(calcula_volume(randint(0, 100)))
# print(calcula_volume(randint(0, 100)))
#
# # Exercício 6: Receber como argumentos horas, nminutos e segundos e converter em segundos.
#
#
# def converte_segundos(horas, minutos, segundos):
#     if 0 <= segundos <= 59 and 0 <= minutos <= 59:
#         return f"{horas} horas, {minutos} minutos e {segundos} segundos " \
#                f"são {(horas * 3600) + (minutos * 60) + segundos} segundos."
#     return "Valor(es) inválido(s)!"
#
#
# print(converte_segundos(3, 56, 19))
# print(converte_segundos(5, 48, 27))
# print(converte_segundos(7, 67, 52))
# print(converte_segundos(1, 45, 62))
# print(converte_segundos(15, 79, 84))
#
# # Exercício 7: Receber temperatura em Celsius e retornar em graus Farenheit.
#
#
# def c_para_f(celsius):
#     return round(celsius * (9 / 5) + 32, 2)
#
#
# print(c_para_f(randint(0, 101)))
# print(c_para_f(randint(0, 101)))
# print(c_para_f(randint(0, 101)))
# print(c_para_f(randint(0, 101)))
# print(c_para_f(randint(0, 101)))
#
# # Exercício 8: Receber os catetos de um triângulo retângulo e retornar a hipotenusa.
#
#
# def calcula_hipotenusa(c1, c2):
#     return ((c1 ** 2) + (c2 ** 2)) ** (1 / 2)
#
#
# print(calcula_hipotenusa(3, 4))
#
# # Exercício 9: Receber o raio e a altura de um cilindro de retornar o volume.
#
#
# def volume_cilindro(raio, altura):
#     return round(3.141592 * altura * (raio ** 2), 2)
#
#
# print(volume_cilindro(randint(0, 11), randint(0, 11)))
# print(volume_cilindro(randint(0, 11), randint(0, 11)))
# print(volume_cilindro(randint(0, 11), randint(0, 11)))
#
# # Exercício 10: Receber 2 números e retornar o maior.
#
#
# def maior_numero(a, b):
#     if a > b:
#         return a
#     return b
#
#
# print(maior_numero(randint(0, 10), randint(0, 10)))
# print(maior_numero(randint(0, 10), randint(0, 10)))
# print(maior_numero(randint(0, 10), randint(0, 10)))
#
# # Exercício 11: Receber 3 notas de um aluno e uma letra. A para média aritimética e P para ponderada (pesos 5, 3, 2).
#
#
# def media_notas(n1=0, n2=0, n3=0, tipo='a'):
#     if tipo.upper() == 'A':
#         print(f"Notas:\nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\n\nTipo de média: Aritimiética.")
#         return round((n1 + n2 + n3) / 3, 2)
#     elif tipo.upper() == 'P':
#         print(f"Notas:\nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\n\nTipo de média: Ponderada (Pesos: 5, 3 e 2).")
#         return f"{round(((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10, 2)}\n"
#     return "Formato de média inválido!"
#
#
# print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'a'))
# print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'p'))
# print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'p'))
# print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'a'))
#
# # Exercício 12: Receber um número maior que zero e retornar a soma de seus algarismos.
#
#
# def soma_algarismos(numero):
#     if numero > 0:
#         print(numero)
#
#         numero = str(numero)
#         soma = 0
#
#         for algarismo in numero:
#             soma += int(algarismo)
#
#         return soma
#     return "Número inválido!"
#
#
# print(soma_algarismos(1789))
# print(soma_algarismos(0))
# print(soma_algarismos(-90))
# print(soma_algarismos(896))
#
# # Exercício 13: Receber dois números e um símbolo de operação matemática básica. Retornar o valor da operação.
#
#
# def operacao(a=0, b=0, operador='+'):
#     if operador == '+':
#         print(f"Operação: {a} + {b}")
#         return a + b
#     elif operador == '-':
#         print(f"Operação: {a} - {b}")
#         return a - b
#     elif operador == '*':
#         print(f"Operação: {a} * {b}")
#         return a * b
#     elif operador == '/':
#         print(f"Operação: {a} / {b}")
#         return a / b
#     return f"Operador {operador} inexistente ou desconhecido."
#
#
# a = int(input("Digite um número: "))
# b = int(input("Digite outro número: "))
# op = input("Digite a operação a ser realizada (opções disponíveis: +, -, *, /) ")
#
# print(operacao(a, b, op))
#
# # Exercício 14: Passar os valores de distância e consumo de combustível e imprimir mensagens de acordo com o consumo.
#
#
# def consumo_km(distancia, consumo):
#     km_l = round(distancia / consumo)
#
#     if km_l < 8:
#         print("Venda o carro!")
#     elif 8 <= km_l < 14:
#         print("Econômico.")
#     else:
#         print("Super econômico!")
#
#
# consumo_km(288, 9)
# consumo_km(140, 16)
# consumo_km(350, 25)
# consumo_km(100, 20)
#
# # Exercício 15: Passar 3 valores maiores que 0.
# x = randint(0, 10)
# y = randint(0, 10)
# z = randint(0, 10)
#
# print(x, y, z)
#
# # item a: Determinar se os valores formam um triângulo.
#
#
# def e_triangulo(a, b, c):
#     if a < b + c and b < c + a and c < a + b and a > 0 and b > 0 and c > 0:
#         print("É um triângulo.")
#         return True
#     print("Não é um triângulo.")
#     return False
#
#
# t = e_triangulo(x, y, z)
#
# # item b: Determinar o tipo de triângulo (equilátero, isóceles ou escaleno)
#
#
# def tipo_triangulo(a, b, c, triangulo):
#     if triangulo:
#         if a == b and b == c:
#             print("Triângulo equilitátero.")
#         elif (a == b and b != c) or (a != b and b == c) or (a != b and a == c):
#             print("Triângulo isóceles.")
#         else:
#             print("Triângulo escaleno.")
#
#
# tipo_triangulo(x, y, z, t)
#
# # Exercício 16: Criar uma função que desenhe uma linha com sinais de igual. Deve receber o número de sinais a imprimir.
#
#
# def desenha_linha(repeticoes):
#     linha = ""
#     for r in range(0, repeticoes):
#         linha += '='
#
#     print(linha)
#
#
# desenha_linha(9)
# desenha_linha(8)
# desenha_linha(2)
# desenha_linha(5)
# desenha_linha(6)
#
# # Exercício 17: Receber dois valores e imprimir a soma dos N números entre eles.
#
#
# def soma_intervalo(a, b):
#     soma = 0
#
#     for i in range(a + 1, b):
#         soma += i
#
#     print(soma)
#
#
# soma_intervalo(6, 14)
# soma_intervalo(8, 36)
# soma_intervalo(5, 17)
# soma_intervalo(10, 39)
#
# # Exercício 18: Receber 2 valores X e Z e retornar X elevado a Z.
#
#
# def exponenciação(x, z):
#     return x ** z
#
#
# print(exponenciação(5, 2))
# print(exponenciação(7, 3))
# print(exponenciação(6, 8))
# print(exponenciação(9, 4))
#
# # Exercício 19: Retornar o maior fator primo de um número recebido.
#
#
# def maior_primo(numero):
#     numero = str(numero)
#     num = 0
#
#     for n in numero:
#         n = int(n)
#
#         if n > num and (n == 2 or n == 3 or n == 5 or n == 7):
#             num = n
#
#     if num != 0:
#         return f"O maior fator primo de {numero} é {num}."
#     return f"{numero} não possui fatores primos."
#
#
# valor = randint(1000, 10000)
# print(maior_primo(valor))
#
# # Exercício 20: Recer um valor N e retornar o seu fatorial:
#
#
# def fatorial(numero):
#     fat = 1
#
#     for f in range(1, numero + 1):
#         fat *= f
#
#     return fat
#
#
# print(fatorial(6))
#
# # Exercício 21: Determinar a quantidade de números primos abaixo de um número N.
#
#
# def quantidade_primos(numero):
#     numeros_primos = 0
#     for cont in range(0, numero):
#         divisores = 0
#         for div in range(1, cont + 1):
#             if cont % div == 0:
#                 divisores += 1
#
#         if divisores == 2:
#             numeros_primos += 1
#
#     return f"Abaixo de {numero} existem {numeros_primos} números primos."
#
#
# print(quantidade_primos(9852))
#
# # Exercício 22: Gerar na saída de uma função N linhas, cada uma com seu número expresso pela quantidade de exclamações.
#
#
# def linhas_exclamacoes(n):
#     linhas = ""
#     for l in range(0, n + 1):
#         for e in range(0, l):
#             linhas += '!'
#         linhas += '\n'
#     return linhas
#
#
# print(linhas_exclamacoes(6))
# print(linhas_exclamacoes(9))
# print(linhas_exclamacoes(25))
#
# Exercício 23: Desenhar um triângulo lateral isóceles de altura 2n - 1 com asteriscos.


def desenha_triangulo(n):
    linhas = ""
    for l in range(0, n + 1):
        for e in range(0, l):
            linhas += '*'
        linhas += '\n'
    for l in range(n - 1, 0, -1):
        for e in range(0, l):
            linhas += '*'
        linhas += '\n'
    return linhas


print(desenha_triangulo(6))