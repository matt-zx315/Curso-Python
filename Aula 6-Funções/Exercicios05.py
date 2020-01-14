import math
from random import choice, randint, uniform
from math import factorial, radians, sqrt

# Exercício 1: Criar uma função que recebe um número e retorna seu dobro.


def retorna_dobro(numero):
    return numero * 2


print(retorna_dobro(5))

# Exercício 2: Receber data e retornar. Exemplo: 01/01/2000 retorna 1 de Janeiro de 2000


def exibe_data(dia, mes, ano):
    if dia < 1:
        return "Dia inválido!"
    else:
        if mes == 1:
            if dia <= 31:
                mes = "Janeiro"
            else:
                return "Dia inválido!"
        elif mes == 2:
            if dia <= 28 and ano % 4 != 0:
                mes = "Fevereiro"
            elif dia == 29 and (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0):
                mes = "Fevereiro"
            else:
                return "Dia inválido!"
        elif mes == 3:
            if dia <= 31:
                mes = "Março"
            else:
                return "Dia inválido!"
        elif mes == 4:
            if dia <= 30:
                mes = "Abril"
            else:
                return "Dia inválido!"
        elif mes == 5:
            if dia <= 31:
                mes = "Maio"
            else:
                return "Dia inválido!"
        elif mes == 6:
            if dia <= 30:
                mes = "Junho"
            else:
                return "Dia inválido!"
        elif mes == 7:
            if dia <= 31:
                mes = "Julho"
            else:
                return "Dia inválido!"
        elif mes == 8:
            if dia <= 31:
                mes = "Agosto"
            else:
                return "Dia inválido!"
        elif mes == 9:
            if dia <= 30:
                mes = "Setembro"
            else:
                return "Dia inválido!"
        elif mes == 10:
            if dia <= 31:
                mes = "Outubro"
            else:
                return "Dia inválido!"
        elif mes == 11:
            if dia <= 30:
                mes = "Novembro"
            else:
                return "Dia inválido!"
        elif mes == 12:
            if dia <= 31:
                mes = "Dezembro"
            else:
                return "Dia inválido!"
        else:
            return "Mês inválido!"

    return f"{dia} de {mes} de {ano}."


print(exibe_data(1, 13, 2016))

# Exercício 3: Verificar se um valor é positivo ou não. Retornar 1 se for positivo e 0 se for 0 ou negativo.


def e_positivo(valor):
    if valor > 0:
        return 1
    return 0


print(e_positivo(6))
print(e_positivo(0))
print(e_positivo(-9))

# Exercício 4: Verificar se um número é um quadrado perfeito.


def quadrado_perfeito(quadrado):
    raiz = quadrado ** (1 / 2)

    if int(raiz) ** 2 == quadrado:
        return f"{quadrado} é um quadrado perfeito."
    return f"{quadrado} não é um quadrado perfeito."


print(quadrado_perfeito(64))
print(quadrado_perfeito(60))

# Exercício 5: Receber o raio de uma esfera e calcular seu volume.


def calcula_volume(raio):
    volume = round((4 / 3) * 3.141592 * (raio ** 3), 3)
    return volume


print(calcula_volume(randint(0, 100)))
print(calcula_volume(randint(0, 100)))
print(calcula_volume(randint(0, 100)))
print(calcula_volume(randint(0, 100)))

# Exercício 6: Receber como argumentos horas, nminutos e segundos e converter em segundos.


def converte_segundos(horas, minutos, segundos):
    if 0 <= segundos <= 59 and 0 <= minutos <= 59:
        return f"{horas} horas, {minutos} minutos e {segundos} segundos " \
               f"são {(horas * 3600) + (minutos * 60) + segundos} segundos."
    return "Valor(es) inválido(s)!"


print(converte_segundos(3, 56, 19))
print(converte_segundos(5, 48, 27))
print(converte_segundos(7, 67, 52))
print(converte_segundos(1, 45, 62))
print(converte_segundos(15, 79, 84))

# Exercício 7: Receber temperatura em Celsius e retornar em graus Farenheit.


def c_para_f(celsius):
    return round(celsius * (9 / 5) + 32, 2)


print(c_para_f(randint(0, 101)))
print(c_para_f(randint(0, 101)))
print(c_para_f(randint(0, 101)))
print(c_para_f(randint(0, 101)))
print(c_para_f(randint(0, 101)))

# Exercício 8: Receber os catetos de um triângulo retângulo e retornar a hipotenusa.


def calcula_hipotenusa(c1, c2):
    return ((c1 ** 2) + (c2 ** 2)) ** (1 / 2)


print(calcula_hipotenusa(3, 4))

# Exercício 9: Receber o raio e a altura de um cilindro de retornar o volume.


def volume_cilindro(raio, altura):
    return round(3.141592 * altura * (raio ** 2), 2)


print(volume_cilindro(randint(0, 11), randint(0, 11)))
print(volume_cilindro(randint(0, 11), randint(0, 11)))
print(volume_cilindro(randint(0, 11), randint(0, 11)))

# Exercício 10: Receber 2 números e retornar o maior.


def maior_numero(a, b):
    if a > b:
        return a
    return b


print(maior_numero(randint(0, 10), randint(0, 10)))
print(maior_numero(randint(0, 10), randint(0, 10)))
print(maior_numero(randint(0, 10), randint(0, 10)))

# Exercício 11: Receber 3 notas de um aluno e uma letra. A para média aritimética e P para ponderada (pesos 5, 3, 2).


def media_notas(n1=0, n2=0, n3=0, tipo='a'):
    if tipo.upper() == 'A':
        print(f"Notas:\nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\n\nTipo de média: Aritimiética.")
        return round((n1 + n2 + n3) / 3, 2)
    elif tipo.upper() == 'P':
        print(f"Notas:\nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\n\nTipo de média: Ponderada (Pesos: 5, 3 e 2).")
        return f"{round(((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10, 2)}\n"
    return "Formato de média inválido!"


print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'a'))
print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'p'))
print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'p'))
print(media_notas(randint(0, 11), randint(0, 10), randint(0, 10), 'a'))

# Exercício 12: Receber um número maior que zero e retornar a soma de seus algarismos.


def soma_algarismos_fatorial(numero):
    if numero > 0:
        print(numero)

        numero = str(numero)
        soma = 0

        for algarismo in numero:
            soma += int(algarismo)

        return soma
    return "Número inválido!"


print(soma_algarismos_fatorial(1789))
print(soma_algarismos_fatorial(0))
print(soma_algarismos_fatorial(-90))
print(soma_algarismos_fatorial(896))

# Exercício 13: Receber dois números e um símbolo de operação matemática básica. Retornar o valor da operação.


def operacao(a=0, b=0, operador='+'):
    if operador == '+':
        print(f"Operação: {a} + {b}")
        return a + b
    elif operador == '-':
        print(f"Operação: {a} - {b}")
        return a - b
    elif operador == '*':
        print(f"Operação: {a} * {b}")
        return a * b
    elif operador == '/':
        print(f"Operação: {a} / {b}")
        return a / b
    return f"Operador {operador} inexistente ou desconhecido."


a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
op = input("Digite a operação a ser realizada (opções disponíveis: +, -, *, /) ")

print(operacao(a, b, op))

# Exercício 14: Passar os valores de distância e consumo de combustível e imprimir mensagens de acordo com o consumo.


def consumo_km(distancia, consumo):
    km_l = round(distancia / consumo)

    if km_l < 8:
        print("Venda o carro!")
    elif 8 <= km_l < 14:
        print("Econômico.")
    else:
        print("Super econômico!")


consumo_km(288, 9)
consumo_km(140, 16)
consumo_km(350, 25)
consumo_km(100, 20)

# Exercício 15: Passar 3 valores maiores que 0.
x = randint(0, 10)
y = randint(0, 10)
z = randint(0, 10)

print(x, y, z)

# item a: Determinar se os valores formam um triângulo.


def e_triangulo(a, b, c):
    if a < b + c and b < c + a and c < a + b and a > 0 and b > 0 and c > 0:
        print("É um triângulo.")
        return True
    print("Não é um triângulo.")
    return False


t = e_triangulo(x, y, z)

# item b: Determinar o tipo de triângulo (equilátero, isóceles ou escaleno)


def tipo_triangulo(a, b, c, triangulo):
    if triangulo:
        if a == b and b == c:
            print("Triângulo equilitátero.")
        elif (a == b and b != c) or (a != b and b == c) or (a != b and a == c):
            print("Triângulo isóceles.")
        else:
            print("Triângulo escaleno.")


tipo_triangulo(x, y, z, t)

# Exercício 16: Criar uma função que desenhe uma linha com sinais de igual. Deve receber o número de sinais a imprimir.


def desenha_linha(repeticoes):
    linha = ""
    for r in range(0, repeticoes):
        linha += '='

    print(linha)


desenha_linha(9)
desenha_linha(8)
desenha_linha(2)
desenha_linha(5)
desenha_linha(6)

# Exercício 17: Receber dois valores e imprimir a soma dos N números entre eles.


def soma_intervalo(a, b):
    soma = 0

    for i in range(a + 1, b):
        soma += i

    print(soma)


soma_intervalo(6, 14)
soma_intervalo(8, 36)
soma_intervalo(5, 17)
soma_intervalo(10, 39)

# Exercício 18: Receber 2 valores X e Z e retornar X elevado a Z.


def exponenciação(x, z):
    return x ** z


print(exponenciação(5, 2))
print(exponenciação(7, 3))
print(exponenciação(6, 8))
print(exponenciação(9, 4))

# Exercício 19: Retornar o maior fator primo de um número recebido.


def maior_primo(numero):
    numero = str(numero)
    num = 0

    for n in numero:
        n = int(n)

        if n > num and (n == 2 or n == 3 or n == 5 or n == 7):
            num = n

    if num != 0:
        return f"O maior fator primo de {numero} é {num}."
    return f"{numero} não possui fatores primos."


valor = randint(1000, 10000)
print(maior_primo(valor))

# Exercício 20: Recer um valor N e retornar o seu fatorial:


def fatorial(numero):
    fat = 1

    for f in range(1, numero + 1):
        fat *= f

    return fat


print(fatorial(6))

# Exercício 21: Determinar a quantidade de números primos abaixo de um número N.


def quantidade_primos(numero):
    numeros_primos = 0
    for cont in range(0, numero):
        divisores = 0
        for div in range(1, cont + 1):
            if cont % div == 0:
                divisores += 1

        if divisores == 2:
            numeros_primos += 1

    return f"Abaixo de {numero} existem {numeros_primos} números primos."


print(quantidade_primos(9852))

# Exercício 22: Gerar na saída de uma função N linhas, cada uma com seu número expresso pela quantidade de exclamações.


def linhas_exclamacoes(n):
    linhas = ""
    for l in range(0, n + 1):
        for e in range(0, l):
            linhas += '!'
        linhas += '\n'
    return linhas


print(linhas_exclamacoes(6))
print(linhas_exclamacoes(9))
print(linhas_exclamacoes(25))

# Exercício 23: Desenhar um triângulo lateral isóceles de altura 2n - 1 com asteriscos.


def desenha_triangulo(n):
    linhas = ""
    for l in range(1, n + 1):
        for e in range(0, l):
            linhas += '*'
        linhas += '\n'
    for l in range(n - 1, 0, -1):
        for e in range(0, l):
            linhas += '*'
        linhas += '\n'
    return linhas


print(desenha_triangulo(6))

# Exercício 24: Desenhar um triângulo isóceles de base 2n - 1.


def desenha_triangulo(n):
    linhas = ""
    for l in range(0, n):
        linhas += (" " * (n - l)) + ("*" * ((2 * l) + 1)) + '\n'
    return linhas


print(desenha_triangulo(6))

# Exercício 25: Receber um inteiro N e retornar o resultado da somatória de (N² + 1) / (N + 3)


def soma_serie(n):
    soma = 0

    for c in range(1, n + 1):
        soma += ((c ** 2) + 1) / (c + 3)

    print((int(soma) * 100) / 100)


soma_serie(280)

# Exercício 26: Calcular o somatório de 1 até um valor N passado como argumento.


def somatorio(n):
    soma = 0

    for n in range(1, n + 1):
        soma += n

    print(f"O somatório de 1 até {n} é {soma}.")


somatorio(5)
somatorio(2)
somatorio(4)
somatorio(9)

# Exercício 27: Fazer uma função que calcule o seno de um ângulo (em radianos) pela sua série de Taylor.


def seno_taylor(angulo):
    x = angulo * (3.141593 / 180)
    seno = 0.0

    for n in range(70):
        if n % 2 == 0:
            seno += (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        else:
            seno -= (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

    return int(seno * 1000) / 1000


print("Seno de 0")
print(seno_taylor(0))

print("\nSeno de 30")
print(seno_taylor(30))

print("\nSeno de 45")
print(seno_taylor(45))

print("\nSeno de 60")
print(seno_taylor(60))

print("\nSeno de 90")
print(seno_taylor(90))

print("\nSeno de 120")
print(seno_taylor(120))

print("\nSeno de 135")
print(seno_taylor(135))

print("\nSeno de 150")
print(seno_taylor(150))

print("\nSeno de 180")
print(seno_taylor(180))

print("\nSeno de 210")
print(seno_taylor(210))

print("\nSeno de 225")
print(seno_taylor(225))

print("\nSeno de 240")
print(seno_taylor(240))

print("\nSeno de 270")
print(seno_taylor(270))

print("\nSeno de 300")
print(seno_taylor(300))

print("\nSeno de 315")
print(seno_taylor(315))

print("\nSeno de 330")
print(seno_taylor(330))

print("\nSeno de 360")
print(seno_taylor(360))

# Exercício 28: Fazer uma função que calcule o cosseno de um ângulo (em radianos) pela sua série de Taylor.


def cosseno_taylor(angulo):
    x = angulo * (3.141593 / 180)
    cosseno = 0

    for n in range(80):
        if n % 2 == 0:
            cosseno += (x ** (2 * n)) / math.factorial(2 * n)
        else:
            cosseno -= (x ** (2 * n)) / math.factorial(2 * n)

    return int(cosseno * 1000) / 1000


print("Cosseno de 0")
print(cosseno_taylor(0))

print("\nCosseno de 30")
print(cosseno_taylor(30))

print("\nCosseno de 45")
print(cosseno_taylor(45))

print("\nCosseno de 60")
print(cosseno_taylor(60))

print("\nCosseno de 90")
print(cosseno_taylor(90))

print("\nCosseno de 120")
print(cosseno_taylor(120))

print("\nCosseno de 135")
print(cosseno_taylor(135))

print("\nCosseno de 150")
print(cosseno_taylor(150))

print("\nCosseno de 180")
print(cosseno_taylor(180))

print("\nCosseno de 210")
print(cosseno_taylor(210))

print("\nCosseno de 225")
print(cosseno_taylor(225))

print("\nCosseno de 240")
print(cosseno_taylor(240))

print("\nCosseno de 270")
print(cosseno_taylor(270))

print("\nCosseno de 300")
print(cosseno_taylor(300))

print("\nCosseno de 315")
print(cosseno_taylor(315))

print("\nCosseno de 330")
print(cosseno_taylor(330))

print("\nCosseno de 360")
print(cosseno_taylor(360))

# Exercício 29: Fazer uma função que calcule o seno hiperbólico de um ângulo (em radianos) pela sua série de Taylor.


def seno_hiperbolico_taylor(angulo):
    x = angulo * (3.141593 / 180)
    seno_hiperbolico = 0

    for n in range(70):
        seno_hiperbolico += (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

    return int(seno_hiperbolico * 1000) / 1000


print("Seno hiperbólico de 0:")
print(seno_hiperbolico_taylor(0))

print("Seno hiperbólico de 30:")
print(seno_hiperbolico_taylor(30))

print("Seno hiperbólico de 45:")
print(seno_hiperbolico_taylor(45))

print("Seno hiperbólico de 60:")
print(seno_hiperbolico_taylor(60))

print("Seno hiperbólico de 90:")
print(seno_hiperbolico_taylor(90))

# Exercício 30: Fazer uma função que calcule o cosseno hiperbólico de um ângulo (em radianos) pela sua série de Taylor.


def cosseno_hiperbolico_taylor(angulo):
    x = angulo * (3.141593 / 180)
    cosseno_hiperbolico = 0

    for n in range(70):
        cosseno_hiperbolico += (x ** (2 * n)) / math.factorial(2 * n)

    return int(cosseno_hiperbolico * 1000) / 1000


print("Cosseno hiperbólico de 0")
print(cosseno_hiperbolico_taylor(0))

print("Cosseno hiperbólico de 30")
print(cosseno_hiperbolico_taylor(30))

print("Cosseno hiperbólico de 45")
print(cosseno_hiperbolico_taylor(45))

print("Cosseno hiperbólico de 60")
print(cosseno_hiperbolico_taylor(60))

print("Cosseno hiperbólico de 90")
print(cosseno_hiperbolico_taylor(90))

# Exercício 31: Criar uma função que usa uma série que calula o número neperiano.


def calcula_neper(ordem):
    e = 0

    for i in range(ordem):
        e += 1 / math.factorial(i)

    return e


print(calcula_neper(9))
print(calcula_neper(15))
print(calcula_neper(100))
print(calcula_neper(64))
print(calcula_neper(36))

# Exercício 32: Criar uma função que simplifica frações.


def simplifica_fracao(numerador, denominador):
    anterior = numerador
    atual = denominador

    resto = anterior % atual

    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual

    print(atual)

    return f"{numerador}/{denominador} = {numerador/atual}/{denominador/atual}"


print(simplifica_fracao(36, 60))
print(simplifica_fracao(108, 105))
print(simplifica_fracao(64, 80))
print(simplifica_fracao(25, 130))

# Exercício 33: Receber um número N e calcular a soma dos algarismos de N!.


def soma_algarismos_fatorial(numero):
    fat = math.factorial(numero)
    fat = str(fat)
    soma = 0

    for algarismo in fat:
        soma += int(algarismo)

    return soma


num = randint(0, 10)
print(f"A soma dos algarismos de {num}! é {soma_algarismos_fatorial(num)}.")
num = randint(0, 10)
print(f"A soma dos algarismos de {num}! é {soma_algarismos_fatorial(num)}.")
num = randint(0, 10)
print(f"A soma dos algarismos de {num}! é {soma_algarismos_fatorial(num)}.")
num = randint(0, 10)
print(f"A soma dos algarismos de {num}! é {soma_algarismos_fatorial(num)}.")

# Exercício 34: Fazer uma função não-recursiva que recebe um número ímpar positivo N e retorna o fatorial duplo de N.


def fatorial_duplo(numero):
    if numero % 2 == 1 and numero > 0:
        fat = 1

        for n in range(numero):
            if n % 2 == 1:
                fat *= n

        return fat
    elif numero % 2 == 1:
        return f"{numero} não é maior que zero!"
    return f"{numero} não é ímpar!"


print(fatorial_duplo(5))
print(fatorial_duplo(6))
print(fatorial_duplo(9))
print(fatorial_duplo(-7))

# Exercício 35: Retornar o fatorial quádruplo de um número N com uma função não-recursiva.


def fatorial_quadruplo(numero):
    if numero > 0:
        fat = 1

        for n in range(1, (2 * numero) + 1):
            fat *= n
        for n in range(1, numero + 1):
            fat /= n

        return fat
    elif numero == 0:
        return 1
    return f"{numero} não é maior que zero."


print(fatorial_quadruplo(4))
print(fatorial_quadruplo(0))
print(fatorial_quadruplo(-8))

# Exercício 36: Receber um número e retornar seu superfatorial.


def superfatorial(numero):
    if numero > 0:
        sfat = 1

        for sf in range(1, numero + 1):
            for f in range(1, sf + 1):
                sfat *= f
        return sfat
    elif numero == 0:
        return 1
    return f"{numero} é menor que zero!"


print(superfatorial(4))
print(superfatorial(0))
print(superfatorial(-1))

# Exercício 37: Receber um número e retornar seu hiperfatorial.


def hiperfatorial(numero):
    if numero > 0:
        hfat = 1

        for hf in range(1, numero + 1):
            hfat *= (hf ** hf)

        return hfat
    elif numero == 0:
        return 1
    return f"{numero} é menor que zero."


print(hiperfatorial(3))
print(hiperfatorial(1))
print(hiperfatorial(-8))

# Exercício 38: Receber um número e retornar seu fatorial exponencial.
#
#
# def fatorial_exponencial(numero):
#     if numero > 0:
#         fat_exp = 2
#
#         for fe in range(3, numero + 1):
#             fat_exp = fe ** fat_exp
#
#         return fat_exp
#     elif numero == 0:
#         return 1
#     return f"{numero} é menor que zero."
#
#
# print(fatorial_exponencial(4))
# print(fatorial_exponencial(0))
# print(fatorial_exponencial(-5))

# Exercício 39: Receber dois valores A e B e trocá-los.


def troca(a, b):
    aux = a
    a = b
    b = aux

    return a, b


print(troca(6, 8))
print(troca(True, "Nepu"))
print(troca(16.5, 'F'))

# Exercício 40: Receber um vetor de inteiros e contar quantos valores pares existem nesse vetor.


def conta_pares(vetor):
    if type(vetor).__name__ != "list":
        return "Variável inserida não é um vetor!"
    elif len(vetor) == 0:
        return "Lista vazia (igual à tua cabeça!)"

    cont = 0

    for v in vetor:
        if type(v).__name__ == "int" and v % 2 == 0:
            cont += 1

    return cont


vetor = [0, True, 2, "Nepu", 3, 8, 9, 6]
print(f"No vetor {vetor} há {conta_pares(vetor)} números pares.")

# Exercício 41: Receber um vetor de inteiros e retornar o maior valor.


def retorna_maior(vetor):
    if len(vetor) == 0:
        return "Vetor vazio."

    maior_valor = vetor [0]

    for i in range(0, len(vetor) - 1):
        if vetor[i] > maior_valor:
            maior_valor = vetor[i]

    return maior_valor


vetor = []

while len(vetor) < 20:
    num = randint(0, 1000)
    vetor.append(num)

print(f"O maior valor do vetor:\n{vetor}\né {retorna_maior(vetor)}.")

# Exercício 42: Receber um vetor de números reais e retornar sua média.


def media_vetor(vet):
    if len(vet) > 0:
        media = sum(vet) / len(vet)
        return media
    return "Vetor vazio!"


vetor = []

for i in range(0, 10):
    num = int(uniform(0.0, 100.0) * 100) / 100
    vetor.append(num)

print(f"A média do vetor:\n{vetor}\né {media_vetor(vetor)}.")

# Exercício 43: Receber um vetor de inteiros e preencher sem repetição.


def preenche_vetor_srep(vet):
    for v in range(0, 10):
        num = randint(0, 100)

        if num not in vet:
            vet.append(num)

    return vet


vetor = []
vetor = preenche_vetor_srep(vetor)

print(vetor)

# Exercício 44: Receber um vetor de 30 elementos e retornar os vetores A e B, contendo os valores pares e ímpares.


def retorna_vetores(vet):
    A, B = [], []

    for v in vet:
        if v % 2 == 0:
            A.append(v)
        else:
            B.append(v)

    return A, B


vetor = []

for i in range(0, 30):
    num = randint(0, 300)
    vetor.append(num)

vetores = retorna_vetores(vetor)
print(f"O vetor\n{vetor}\ntem como valores pares:\n{vetores[0]}\ne como valores ímpares:\n{vetores[1]}.")

# Exercício 45: Receber um vetor e calcular o desvio padrão


def desvio_padrao(vet):
    media = sum(vet) / len(vet)
    variancia = 0

    for valor in vet:
        variancia += (valor - media) ** 2

    desvio = sqrt(variancia / (len(vet) - 1))

    return int(desvio * 1000) / 1000


vetor = []

for i in range(50):
    num = int(uniform(0.0, 100.0) * 100) / 100
    vetor.append(num)

print(vetor)
print(desvio_padrao(vetor))

# Exercício 46: Criar funções que recebem um vetor.
vetor = []

for i in range(10):
    num = randint(0, 100)
    vetor.append(num)


# Item a: Imprimir o vetor.


def imprime_vetor(vet):
    print(vet)


imprime_vetor(vetor)

# Item B: Imprimir o vetor ao contrário.


def imprime_inverso(vet):
    print(vet[::-1])


imprime_inverso(vetor)

# Item C: Retornar a média aritimética dos valores.


def media_aritimetica(vet):
    return sum(vetor) / len(vetor)


print(media_aritimetica(vetor))

# Exercício 47: Receber uma matriz 4 x 4 e contar quantos valores são maiores que 10.
matriz = []

for i in range(0, 4):
    matriz.append([])

    for j in range(0, 4):
        num = randint(0, 20)
        matriz[i].append(num)

for vetor in matriz:
    print(vetor)


def maior_q10(mat):
    cont = 0

    for vet in mat:
        for numero in vet:
            if numero > 10:
                cont += 1

    return cont


print(f"Há, na matriz, {maior_q10(matriz)} valores maiores que 10.")

# Exercício 48: Receber uma matriz 3 x 3 e retornar a soma dos elementos acima da diagonal principal.


def soma_acima_dp(mat):
    soma = 0

    for lin in range(len(mat)):
        for col in range(len(mat[lin])):
            if col > lin:
                soma += mat[lin][col]

    return soma


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

print(soma_acima_dp(matriz))

# Exercício 49: Receber uma matriz 3 x 3 e retornar a soma dos elementos abaixo da diagonal principal.


def soma_abaixo_dp(mat):
    soma = 0

    for lin in range(len(mat)):
        for col in range(len(mat[lin])):
            if col < lin:
                soma += mat[lin][col]

    return soma


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])


print(soma_abaixo_dp(matriz))

# Exercício 50: Receber uma matriz 3 x 3 e retornar a soma dos elementos da diagonal principal.


def soma_diagonal_principal(mat):
    soma = 0

    for k in range(len(mat)):
        soma += mat[k][k]

    return soma


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

print(soma_diagonal_principal(matriz))

# Exercício 51: Receber uma matriz 3 x 3 e retornar a soma dos elementos da diagonal secundária.


def soma_diagonal_secundaria(mat):
    soma = 0

    for lin in range(len(mat)):
        for col in range(len(mat)):
            if lin + col == len(mat) - 1:
                soma += mat[lin][col]

    return soma


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])


print(soma_diagonal_secundaria(matriz))

# Exercício 52: Receber uma matriz quadrada de ordem N e retornar sua transposta.


def calcula_transposta(mat):
    transposta = mat.copy()

    for lin in range(len(mat)):
        for col in range(len(mat)):
            if col > lin:
                aux = mat[col][lin]
                mat[col][lin] = mat[lin][col]
                mat[lin][col] = aux

    return transposta


matriz = []

for i in range(4):
    matriz.append([])

    for j in range(4):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

t = calcula_transposta(matriz)
print()

for l in t:
    print(l)

# Exercício 53: Verificar se uma matriz quadrada de ordem N é a matriz identidade.


def e_identidade(mat):
    identidade = True

    for lin in range(len(mat)):
        for col in range(len(mat)):
            if lin == col:
                if mat[lin][col] != 1:
                    identidade = False
            elif mat[lin][col] != 0:
                identidade = False

    if identidade:
        return "É matriz identidade."
    return "Não é matriz identidade."


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

matriz2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print(e_identidade(matriz))
print(e_identidade(matriz2))

# Exercício 54: Receber uma matriz 4 x 4 e retornar a soma de seus elementos.


def soma_elementos(mat):
    soma = 0

    for lin in range(len(mat)):
        for col in range(len(mat)):
            soma += mat[lin][col]

    return soma


matriz = []

for i in range(4):
    matriz.append([])

    for j in range(4):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

print(soma_elementos(matriz))

# Exercício 55: Receber uma matriz 3 x 3 e retornar a soma de suas diagonais.


def soma_diagonais(mat):
    soma = 0

    for lin in range(len(mat)):
        for col in range(len(mat[lin])):
            if lin == col or lin + col == len(mat) - 1:
                soma += mat[lin][col]

    return soma


matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

print(soma_diagonais(matriz))

# Exercício 56: Receber uma matriz 7 x 6 e um número N representando uma linha.


def soma_linha(mat, lin):
    soma = 0

    if 0 <= lin < len(mat):
        for col in range(len(mat[lin])):
            soma += mat[lin][col]

        return soma
    return "Linha inexistente!"


matriz = []

for i in range(7):
    matriz.append([])

    for j in range(6):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])

print(soma_linha(matriz, 4))
print(soma_linha(matriz, 1))
print(soma_linha(matriz, 9))
print(soma_linha(matriz, -6))

# Exercício 57: Receber uma matriz 7 x 6 e um número N representando uma coluna.


def soma_coluna(mat, col):
    soma = 0

    if 0 <= col < len(mat[0]):
        for lin in range(len(mat)):
            soma += mat[lin][col]

        return soma
    return "Coluna inexistente!"


matriz = []

for i in range(7):
    matriz.append([])

    for j in range(6):
        num = randint(0, 30)
        matriz[i].append(num)

    print(matriz[i])


print(soma_coluna(matriz, 5))
print(soma_coluna(matriz, 0))
print(soma_coluna(matriz, -2))
print(soma_coluna(matriz, 8))

# Exercício 58: Receber 2 matrizes A e B e retornar a matriz C, sendo essa o produto de A e B.


def produto_matricial(a, b):
    C = []

    if len(a[0]) == len(b):
        for lin in range(len(a)):
            C.append([])

            for col in range(len(b[0])):
                C[lin].append(0)

                for k in range(len(a[0])):
                    C[lin][col] += a[lin][k] * b[k][col]

        return C
    return "Impossível realizar multiplicação de A e B."


matrizA = []
matrizB = []

for i in range(3):
    matrizA.append([])
    matrizB.append([])

    for j in range(3):
        num = randint(0, 9)
        matrizA[i].append(num)
        num = randint(0, 9)
        matrizB[i].append(num)


for l in matrizA:
    print(l)

print()

for l in matrizB:
    print(l)

print()

for l in produto_matricial(matrizA, matrizB):
    print(l)

# Exercício 59: Receber 2 vetores de tamanho 10 e retornar o vetor união desses vetores.


def vetor_uniao(a, b):
    return a + b


A, B = [], []

for i in range(10):
    num = randint(0, 50)
    A.append(num)
    num = randint(0, 50)
    B.append(num)

print(A)
print(B)
print(vetor_uniao(A, B))

# Exercício 60: Retornar a primeira posição de uma substring dentro de uma string ou -1 caso aquela não exista.


def substring(string, start=None, stop=None):
    if start > len(string):
        return -1
    return f"Substring: {string[start:stop]}, primeira posição: {string[start:stop][0]}."


st = "Isso não faz o menor sentido."

print(substring(st, 19, 23))

# Exercício 61: Comaparar e reotrnar verdadeiro se uma string for um anagrama de uma palavra.


def compara_palavra(original, palavra):
    if len(palavra) == len(original):
        comparacoes = 0

        for letra1 in palavra:
            for letra2 in original:
                if letra1.lower() == letra2.lower():
                    comparacoes += 1

        if comparacoes == len(original):
            return True
        return False
    return False


o = "Alice"
p = "Celia"

print(compara_palavra(o, p))

# Exercício 62: Calcular o tamanho de uma string numa função com a assinatura void tamanho(char *str, int *strsize)


def tamanho(string):
    print(f"\"{string}\" tem {len(string)} letras.")


st = "Sai da frente, Satanás!!!"

tamanho(st)

# Exercício 63: Retornar se duas strings são iguais ou diferentes.


def compara_strings(st1, st2):
    if len(st1) == len(st2):
        for letra in range(len(st1)):
            if st1[letra].lower() != st2[letra].lower():
                return f"{st1} e {st2} não são iguais."
        return f"{st1} e {st2} são iguais."
    return f"{st1} e {st2} não são iguais."


palavra1 = "Réptil"
palavra2 = "Reptil"

print(compara_strings(palavra1, palavra2))

# Exercício 64: Receber duas strings, str1 e str2, e concatenar str2 a str1.


def concatena_strings(str1, str2):
    str1 += str2
    return str1


s1, s2 = "Gato ", "comeu!"

print(concatena_strings(s1, s2))

# Exercício 65: Receber 2 strings, str1 e str2 e um inteiro N. Concatenar os N primeiros caracteres de str2 a str1.


def concatena_n(str1, str2, n):
    str1 += str2[:n]
    return str1


s1, s2 = "Eu não faço ", "a menor ideia do que estou fazendo."

print(concatena_n(s1, s2, 13))

# Exercício 66: Retornar um caractere recebido em maíusculo.


def caractere_maiusculo(string):
    return string.upper()


st = "a"
print(caractere_maiusculo(st))

# Exercício 67: Receber um vetor e seu tamanho. Inserir caracteres no vetor até que atinja o tamanho ou presionar enter.


def getchar():
    char = input()
    return char


def preenche_vetor_char(_vetor, _tamanho):
    while len(_vetor) < _tamanho:
        char = getchar()
        if char != "":
            _vetor.append(char)
        else:
            break
    return _vetor


v = preenche_vetor_char([], 5)

print(v)

# Exercício 68: Receber duas strings e intercalá-las letra a letra na primeira string.


def intercala_strings(_str1, _str2):
    aux = ""
    if _str1 < _str2:
        for i in range(len(_str1)):
            aux += _str1[i]
            aux += _str2[i]
    else:
        for i in range(len(_str2)):
            aux += _str1[i]
            aux += _str2[i]

    _str1 = aux
    return _str1


s1, s2 = "Criança insuportável!", "Para de chorar, desgraça!!!"

print(intercala_strings(s1, s2))

# Exercício 69: Criar funções que realizem operações com frações.

# item a: Criar e ler duas frações, P e Q, com numerador e denominador:


def le_fracao(numerador, denominador):
    return numerador, denominador


P = le_fracao(4, 14)
Q = le_fracao(9, 15)

print(P, Q)

# item b: encontrar o MDC entre numerador e denominador para simplificar as frações.


def simplifica_fracao(fracao):
    numerador = fracao[0]
    denominador = fracao[1]

    anterior = numerador
    atual = denominador

    resto = anterior % atual

    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual

    return numerador/atual, denominador/atual


P = simplifica_fracao(P)
Q = simplifica_fracao(Q)

print(P, Q)

# item c: criar uma função para cada operação básica entre frações (soma, diferença, produto e razão):


def numero_primo(_numero):
    _divisores = 0

    for c in range(1, _numero + 1):
        if _numero % c == 0:
            _divisores += 1

    if _divisores == 2:
        return True
    return False


def calcula_mmc(_n1, _n2):
    _mmc = 1
    _num = 2
    _multiplica = True  # Evita multiplicações adicionais, as quais resultariam em um valor de MMC errado.

    while _n1 != 1 or _n2 != 1:

        if numero_primo(_num):  # Realiza as divisões apaenas com números primos.
            if _n1 % _num == 0:
                _n1 /= _num
                _mmc *= _num
                _multiplica = False

            elif _n2 % _num == 0:
                _n2 /= _num

                if _multiplica:  # Só haverá multiplicação por _num se _n1 não tiver sofrido divisão.
                    _mmc *= _num
            else:
                _multiplica = True
                _num += 1
        else:
            _num += 1
    return _mmc


def soma_fracoes(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3, _den3 = 1, 1

    if _den1 != _den2:
        _den3 = calcula_mmc(_den1, _den2)
        _num3 = _num1 * (_den3 / _den1) + _num2 * (_den3 / _den2)
    else:
        _den3 = _den1
        _num3 = _num1 + _num2
    return int(_num3), _den3


def subtrai_fracoes(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3, _den3 = 1, 1

    if _den1 != _den2:
        _den3 = calcula_mmc(_den1, _den2)
        _num3 = _num1 * (_den3 / _den1) - _num2 * (_den3 / _den2)
    else:
        _den3 = _den1
        _num3 = _num1 - _num2
    return int(_num3), _den3


def multiplica_fracoes(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3 = _num1 * _num2
    _den3 = _den1 * _den2

    return _num3, _den3


def divide_fracoes(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3 = _num1 * _den2
    _den3 = _num2 * _den1

    return _num3, _den3


print(soma_fracoes(P, Q))
print(subtrai_fracoes(P, Q))
print(multiplica_fracoes(P, Q))
print(divide_fracoes(P, Q))

# Exercício 70: Um número racional composto pelas partes P e Q, com Q > 0 e MDC = 1:
# item a: Receber os valores A e B, reduzí-los e retornar o racional representado por a/b.


def reduzir(_numerador, _denominador):
    _anterior = _numerador
    _atual = _denominador

    _resto = _anterior % _atual

    while _resto != 0:
        _anterior = _atual
        _atual = _resto
        _resto = _anterior % _atual

    return _numerador/_atual, _denominador/_atual


A, B = 9, 6
C, D = 8, 14

print(f"{A}/{B} = {reduzir(A, B)[0]}/{reduzir(A, B)[1]}")
print(f"{C}/{D} = {reduzir(C, D)[0]}/{reduzir(C, D)[1]}")

# item b: receber um racional X e retornar -X.
E = reduzir(A, B)
F = reduzir(C, D)


def neg(_p, _q):
    return -_p, _q


print(f"{neg(*E)[0]}/{neg(*E)[1]}")

# item c: Receber 2 racionais e retornar sua soma.


def numero_primo(_numero):
    _divisores = 0

    for c in range(1, _numero + 1):
        if _numero % c == 0:
            _divisores += 1

    if _divisores == 2:
        return True
    return False


def calcula_mmc(_n1, _n2):
    _mmc = 1
    _num = 2
    _multiplica = True  # Evita multiplicações adicionais, as quais resultariam em um valor de MMC errado.

    while _n1 != 1 or _n2 != 1:

        if numero_primo(_num):  # Realiza as divisões apaenas com números primos.
            if _n1 % _num == 0:
                _n1 /= _num
                _mmc *= _num
                _multiplica = False

            elif _n2 % _num == 0:
                _n2 /= _num

                if _multiplica:  # Só haverá multiplicação por _num se _n1 não tiver sofrido divisão.
                    _mmc *= _num
            else:
                _multiplica = True
                _num += 1
        else:
            _num += 1
    return _mmc


def soma(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3, _den3 = 1, 1

    if _den1 != _den2:
        _den3 = calcula_mmc(_den1, _den2)
        _num3 = _num1 * (_den3 / _den1) + _num2 * (_den3 / _den2)
    else:
        _den3 = _den1
        _num3 = _num1 + _num2
    return int(_num3), _den3


print(f"{soma(E, F)[0]}/{soma(E, F)[1]}")

# item d: receber dois racionais e retornar seu produto.


def mult(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3 = _num1 * _num2
    _den3 = _den1 * _den2

    return _num3, _den3


print(f"{reduzir(*mult(E, F))[0]}/{reduzir(*mult(E, F))[1]}")

# item e: Receber dois racionais e retornar sua razão.


def div(_fracao1, _fracao2):
    _num1 = _fracao1[0]
    _num2 = _fracao2[0]
    _den1 = _fracao1[1]
    _den2 = _fracao2[1]

    _num3 = _num1 * _den2
    _den3 = _num2 * _den1

    return _num3, _den3


print(f"{div(E, F)[0]}/{div(E, F)[1]}")

# Exercício 71: Dado um ponto nas coordenadas (X,Y), determinar se esse ponto está dentro de um retângulo,
# o qual é definido pelos vértices inferior esquerdo v1 e superior direito v2. Retornar 1 para dentro e 0 para fora.
ponto_A = {'x': 0, 'y': 0}
ponto_B = {'x': 10, 'y': 3}
ponto_C = {'x': -6, 'y': 15}
v1 = {'x': -10, 'y': 10}
v2 = {'x': 10, 'y': -10}


def dentro_ret(_ponto, _vertice1, _vertice2):
    if _vertice1['x'] < _ponto['x'] < _vertice2['x'] and _vertice2['y'] < _ponto['y'] < _vertice1['y']:
        return 1
    return 0


print(dentro_ret(ponto_A, v1, v2))
print(dentro_ret(ponto_B, v1, v2))
print(dentro_ret(ponto_C, v1, v2))

# Exercício 72: Dados dois vetores V1 e V2 (X, Y, Z), recebê-los como dados e armazenar sua soma numa variável.
V1 = {'x': 5, 'y': 6, 'z': 4}
V2 = {'x': 2, 'y': 8, 'z': 3}
vetor_soma = None


def soma_vetores(_v1, _v2):
    _soma = {}
    for chave in _v1.keys():
        _soma[chave] = _v1[chave] + _v2[chave]

    global vetor_soma
    vetor_soma = _soma.copy()


soma_vetores(V1, V2)
print(vetor_soma)

# Exercício 73: A partir dos dados coletados de pessoas numa pesquisa, elaborar funções:
# item a: ler os dados recolhidos em um vetor.
pessoas = []

for i in range(5):
    temp_dict = {'sexo': choice(['M', 'F']), 'olhos': choice(['a', 'c']), 'cabelos': choice(['l', 'p', 'c']),
                 'idade': randint(10, 45)}

    pessoas.append(temp_dict)


def le_dados(_lista):
    for item in _lista:
        print(item)
    return


le_dados(pessoas)

# item b: Calcular a média da idade das pessoas com cabelos castanhos.


def media_idades(_lista, _tipo='cabelos', _dado='c'):
    soma, cont, media = 0, 0, 0

    for p in _lista:
        if p[_tipo] == _dado:
            soma += p['idade']
            cont += 1

    if cont > 0:
        media = soma / cont
        return media
    return 0


print(media_idades(pessoas))

# item c: Encontrar e retornar a maior idade entre os habitantes.


def maior_idade(_lista):
    idade = _lista[0]['idade']

    for j in range(len(_lista)):
        if _lista[j]['idade'] > idade:
            idade = _lista[j]['idade']

    return idade


print(f"A maior idade entre os habitantes pesquisados é {maior_idade(pessoas)}.")

# item d: Retornar o número de mulheres entre 18 e 35 anos.


def conta_habitantes(_lista, _tipo='sexo', _dado='F', _idade_min=18, _idade_max=35):
    cont = 0

    for p in _lista:
        if p[_tipo] == _dado and _idade_min < p['idade'] < _idade_max:
            cont += 1

    return cont


print(f"Há, nesse estudo, {conta_habitantes(pessoas)} mulheres entre 18 e 35 anos.")