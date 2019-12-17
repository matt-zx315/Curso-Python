"""
math.factorial(x) é usada para calcular fatoriais.
num2words é uma biblioteca que transforma números em sua forma escrita (ex.: 1 = um)

Para instalar, entrar no ambiente virtual (workon <nome do ambiente>) e depois digitar pip install num2words
"""

import math
import random

from num2words import num2words
# Exercício 1: Mostrar os 5 primeiros múltiplos de 3 maiores que 0.
i = 1

while i <= 5:
    print(i * 3)
    i += 1

# Exercício 2: Escrever 3 loops que imprimam números de 1 a 100, usando for, while e do while, respectivamente.

# Com loop for
for i in range(1, 101):
    print(i, end=', ')

    if i == 100:
        print('\b' * 2)

# Com loop while
i = 1

while i <= 100:
    print(i, end=', ')

    if i == 100:
        print('\b' * 2)

    i += 1

# Com loop do while (loop while com break)
i = 1

while True:
    if i > 100:
        break
    else:
        print(i, end=', ')

        if i == 100:
            print('\b' * 2)

        i += 1

# Exercício 3: Fazer contagem regressiva de 10 até 0 com loop while e mostrar mensagem ao final.
i = 10

while i >= 0:
    print(i)
    i -= 1

print("FIM!")

# Exercício 4: Inicializar um inteiro com valor 0, incrementar de 1000 em 1000 e parar ao chegar em 100000
for num in range(0, 100_001, 1_000):
    print(num)

# Exercício 5: Solicitar 10 valores ao usuário e imprimir a soma.
soma = 0

for i in range(0, 10):
    num = int(input(f"Digite o número {i + 1} de 10: "))
    soma += num

print(f"A soma dos valores inseridos é {soma}.")

# Exercício 6: Ler 10 inteiros e imprimir a média.
soma = 0

for i in range(0, 10):
    num = int(input(f"Digite o número {i + 1} de 10: "))
    soma += num

media = soma / 10
print(f"A média dos valores inseridos é {media}.")

# Exercício 7: Ler 10 inteiros e imprimir a média, ignorando os valores negativos.
soma = 0
denominador = 0

for i in range(0, 10):
    num = int(input(f"Digite o número {i + 1} de 10: "))

    if num >= 0:
        soma += num
        denominador += 1

if denominador > 0:
    media = soma / denominador
    print(f"A média dos valores inseridos é {media}.")
else:
    print("Não foi possível calcular.")

# Exercício 8: Receber 10 valores e imprimir o menor e maior valores inseridos.
menor_valor = 0
maior_valor = 0

for i in range(0, 10):
    valor = int(input("Digite um valor: "))

    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor

print(f"O menor valor é: {menor_valor}.\nO maior valor é: {maior_valor}.")

# Exercício 9: Ler um inteiro N e imprimir os N primeiros números ímpares.
n = int(input("Digite um número inteiro. "))

for i in range(0, n):
    print(1 + 2 * i)

# Exercício 10: Calcular e mostrar a soma dos primeiros 50 números pares.
soma = 0

for i in range(0, 50):
    soma += 2 * i

print(soma)

# Exercício 11: Ler um inteiro positivo N e imprimir os naturais de 0 a N em ordem crescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(0, n + 1):
    print(i, end=', ')

    if i == n:
        print('\b' * 2)

# Exercício 12: Ler um inteiro positivo N e imprimir os naturais de 0 a N em ordem decrescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(n, -1, -1):
    print(i, end=', ')

    if i == 0:
        print('\b' * 2)

# Exercício 13: Ler um inteiro positivo N e imprimir os pares de 0 a N em ordem crescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(0, n + 1):
    print(i * 2, end=', ')

    if i == n:
        print('\b' * 2)

# Exercício 14: Ler um inteiro positivo N e imprimir os pares de 0 a N em ordem decrescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(n, -1, -1):
    print(i * 2, end=', ')

    if i == 0:
        print('\b' * 2)

# Exercício 15: Ler um inteiro positivo N e imprimir os ímpares de 1 a N em ordem crescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(0, n + 1):
    print(i * 2 + 1, end=', ')

    if i == n:
        print('\b' * 2)

# Exercício 16: Ler um inteiro positivo N e imprimir os ímpares de 1 a N em ordem decrescente.

n = int(input("Insira um inteiro positivo: ")).__abs__()

for i in range(n, -1, -1):
    print(i * 2 + 1, end=', ')

    if i == 0:
        print('\b' * 2)

# Exercício 17: Ler um inteiro positivo N e imprimir a soma dos N primeiros números naturais.
num = int(input("Digite um número inteiro. "))
i = 0
soma = 0

while i <= num:
    soma += i
    i += 1

print(soma)

# Exercício 18: Ler o número de vezes que um valor será recebido e imprimir quantas vezes o maior número foi lido.
reps = int(input("Insira o número de vezes que o programa lerá um valor: "))
i = 0
maior_valor = 0
novo_maior = 0

while i < reps:
    valor = int(input("Digite um número inteiro. "))

    if valor > maior_valor:
        maior_valor = valor
        novo_maior += 1

    i += 1

print(f"O maior número foi lido {novo_maior} vezes.\nO maior valor recebido foi {maior_valor}.")

# Exercício 19: Receber um valor de 100 a 999 e imprimir cada algaritmo que compõe o número.
num = int(input("Digite um valor de 100 a 999. "))
i = 0

if num < 100 or num > 999:
    print("NÚMERO INVÁLIDO!")
else:
    num = str(num)

    while i < 3:
        print(num[i])
        i += 1

# Exercício 20: Ler uma sequência de números, contar quantos foram lidos e quantos são pares. Ao digitar 1000, encerrar.
numeros_lidos = 0
pares_lidos = 0

while True:
    num = int(input("Digite um número: "))

    if num == 1000:
        break
    else:
        if num % 2 == 0:
            print(f"{num} é par.")
            pares_lidos += 1

    numeros_lidos += 1

    print(f"Foram lidos {numeros_lidos} números, dos quais {pares_lidos} são pares.")

# Exercício 21: Ler 2 números e apresentar soma dos pares e multiplicação dos ímpares no intervalo, incluindo digitados.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
aux = 0

soma, produto = 0, 1
if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i
    elif i % 2 == 1:
        produto *= i

print(f"A soma dos números pares no intervalo de {num1} a {num2} é {soma}.")
print(f"O produto dos valores ímpares no intervalo de {num1} a {num2} é {produto}.")

# Exercício 22: Introduzir uma sequência de notas de 10 a 20, imprimir média e encerrar caso a nota seja inválida.
notas = 0
soma = 0
while True:
    nota = int(input("Digite uma nota de 10 a 20: "))
    if nota < 10 or nota > 20:
        print("Nota inválida. Encerrando...")
        break
    else:
        notas += 1
        soma += nota
        media = round(soma / notas, 2)
        print(f"A média atual das notas é de {media}.")

# Exercúcio 23: Ler um positivo e imprimir seus divisores.
num = int(input("Digite um número INTEIRO: ")).__abs__()

print(f"O número {num} tem como divisores: ")

for div in range(1, num):
    if num % div == 0:
        print(div, end=', ')

print('\b' * 2 + f" e {num}.")

# Exercício 24: Ler um inteiro e imprimir a soma de todos os divisores deste número exceto por ele mesmo.
num = int(input("Digite um número INTEIRO: ")).__abs__()
soma_div = 0

for div in range(1, num):
    if num % div == 0:
        soma_div += div

print(f"A soma dos divisores de {num} é {soma_div}.")

# Exercício 25: Somar os números naturais abaixo de 1000 múltiplos de 3 ou 5.
i = 0
soma = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        soma += i

    i += 1

print(f"A soma dos números naturais múltiplos de 3 ou 5 e menores que 1.000 é {soma}.")

# Exercício 26: Fazer um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após o valor ddigitado.
num1 = int(input("Digite um número: "))
num2 = 0 + num1

while True:
    num2 += 1

    if num2 % 11 == 0:
        print(f"O múltiplo mais próximo de {num1} é {num2}, um múltiplo de 11.")
        break
    elif num2 % 13 == 0:
        print(f"O múltiplo mais próximo de {num1} é {num2}, um múltiplo de 13.")
        break
    elif num2 % 17 == 0:
        print(f"O múltiplo mais próximo de {num1} é {num2}, um múltiplo de 17.")
        break

# Exercício 27: Ler um valor inteiro positivo e apresentar o valor da série harmônica. (Extra: imprimir série harmônica)
n = int(input("Digite um número: "))
i = 1
h = 0

mensagem = f"A série harmônica H({n}) = 1 + "

while i <= n:
    h += 1 / i

    if i >= 2:
        mensagem += f"1/{i} + "

    if i == n:
        mensagem += '\b' * 2 + "= "

    i += 1

h = round(h, 6)
mensagem += f'{h}.'

print(mensagem)

# Exercício 28: Receber um número inteiro positivo N e apresentar o valor da soma dos fatoriais inversos. de 1 a N.
n = int(input("Digite um valor inteiro positivo: "))
i = 1
seq = 0

mensagem = f"O valor da sequência S({n}) = 1 + "

while i <= n:
    seq += 1/math.factorial(i)

    if i >= 2:
        mensagem += f"1/{i}! + "

    if i == n:
        mensagem += '\b' * 2 + '= '

    i += 1

seq = round(seq, 5)
mensagem += f"{seq}."
print(mensagem)

# Exercício 29: Imprimir a soma de 5 termos.
i = 1
seq = 0

mensagem = "O valor da sequência S(5) = 0 + "

while i <= 5:
    seq += 1 * i/math.factorial(2 * i)
    mensagem += f"{1 * i}/{2 * i}! + "

    if i == 5:
        mensagem += '\b' * 2 + '= '

    i += 1

seq = round(seq, 5)
mensagem += f"{seq}."
print(mensagem)

# Exercícios 30: Calcular sequências.
n = int(input("Digite um número: "))

seq1, seq2, seq3 = 0, 0, 0

for i in range(1, n + 1):
    seq1 += n

for i in range(1, 2* n + 1):
    if i % 2 == 1:
        seq2 += i
    else:
        seq2 -= i

for i in range(1, 2 * n + 1):
    seq3 += 2 * i - 1

print(f"O valor da sequência 1 + 2 + 3 + ... + n é {seq1}.")
print(f"O valor da sequência 1 - 2 + 3 - 4 + ... + n é {seq2}.")
print(f"A soma da sequência 1 + 3 + 5 + 7 + .. + n é {seq3}.")

# Exercício 31: Calcular o valor da sequência de frações 1/1 + 3/2 + 5/3 + ... + 99/50
i = 1
seq = 0

while i <= 50:
    seq += (2 * i - 1)/i
    i += 1

seq = round(seq, 4)
print(f"A soma de 1/1 + 3/2 + 5/3 + ... + 99/50 é {seq}.")

# Exercício 32: Simular os lançamentos de dois dados N vezes e imprimir os resultados e a relação (<,>,=) entre eles.
reps = int(input("Digite o número de lançamentos. "))
i = 0

while i < reps:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f"O resultado de D1 foi {d1} e o de D2 foi {d2}.")
    if d1 > d2:
        print("O valor de D1 é maior que o de D2.")
    elif d1 < d2:
        print("O valor de D1 é menor que o de D2.")
    else:
        print("O valor de D1 é igual ao de D2.")

    print()
    i += 1

# Exercício 33: Imprimir em ordem crescente os N múltiplos de dois números inteiros positivos lidos I e J.
n = int(input("Digite o número de múltiplos a serem exibidos. "))
i = int(input("Insira o primeiro valor inteiro positivo. "))
j = int(input("Insira o segundo valor inteiro positivo. "))

mensagem = f"Em ordem crescente, os {n} primeiros múltiplos de {i} e/ou {j} são:\n"
multiplo = 0
conjunto = 0

while conjunto < n:
    if multiplo % i == 0:
        mensagem += f"{multiplo}, "
        conjunto += 1
    elif multiplo % j == 0:
        mensagem += f"{multiplo}, "
        conjunto += 1
    multiplo += 1

mensagem += '\b' * 2
print(mensagem)

# Exercício 34: Calcular o menor valor divisível pelos números de 1 a 20. (116.396.280)
num = 1
validador = 0

while validador < 20:
    validador = 0
    for i in range(1, 21):
        if num % i == 0:
            validador += 1
        else:
            print(f"{num} conseguiu validar {validador} valores.")
            break
    num += 1

print(f"O menor múltiplo comum de 1 a 20 é {num}.")

# Exercício 35: Ler um intervalo e imprimir a soma dos números ímpares dentro deste intervalo.
num1 = int(input("Digite um número inteiro. "))
num2 = int(input("Digite um número inteiro. "))
cont = num1
soma = 0

if num2 <= num1:
    print("VALORES INVÁLIDOS!")
else:
    while cont <= num2:
        if cont % 2 == 1:
            soma += cont
        cont += 1

    print(f"A soma dos números ímpares no intervalo de {num1} a {num2} é {soma}.")

# Exercício 36: Calcular a diferença entre o quadrado da soma e a soma dos quadrados dos 100 primeiros números naturais.
soma_quadrados = 0
quadrado_soma = 0
num = 0

while num <= 100:
    soma_quadrados += (num ** 2)
    quadrado_soma += num
    num += 1

diferenca = (quadrado_soma ** 2) - soma_quadrados
print(f"A diferença entre o quadrado da soma e a soma dos quadrados"
      f"dos 100 primeiros números naturais é {diferenca}.")

# Exercício 37: Achar os números de 1000 a 9999 nos quais o quadrado da soma dos dois dígitos de ordem mais alta
# e mais baixa seja igual ao próprio número. Ex: 3025 -> 30 + 25 = 55 -> 55² = 3025
num = 1000
mensagem = f"Os números cuja soma dos pares de dígitos de ordem mais alta com os pares de ordem mais baixa\n" \
           f"elevados ao quadrado são iguais ao próprio número são:\n"
ordem_alta = ''
ordem_baixa = ''

while num < 10_000:
    ordem_alta = int(str(num)[:2])  # Do início até o índice 2.
    ordem_baixa = int(str(num)[-2:])  # Do início até o índice 2 de trás para frente.

    if (ordem_alta + ordem_baixa) ** 2 == num:
        mensagem += f"{num}, "

    num += 1

mensagem += '\b' * 2

print(mensagem)

# SOLUÇÃO ALTERNATIVA
num = ordem_alta = ordem_baixa = None  # None atribui um valor nulo à variável.
mensagem = f"Os números cuja soma dos pares de dígitos de ordem mais alta com os pares de ordem mais baixa\n" \
           f"elevados ao quadrado são iguais ao próprio número são:\n"

for n in range(1_000, 10_000):
    num = str(n / 100)
    ordem_alta, ordem_baixa = num.split('.')  # split() é uma função que separa stings em um caractere específico.

    if (int(ordem_alta) + int(ordem_baixa)) ** 2 == n:
        mensagem += f"{n}, "

mensagem += '\b' * 2
print(mensagem)

# Exercício 38: Calcular o terno pitagórico a + b + c = 1000, sabendo que a² + b² = c²
terno = 1000
mensagem = f"Os ternos pitagóricos cujo valor é {terno} são:\n"

for a in range(1, terno + 1):
    for b in range(1, terno + 1):
        for c in range(1, terno + 1):
            if (a + b + c) == terno and ((a ** 2) + (b ** 2)) == (c ** 2):
                mensagem += f"{a}, {b} e {c}\n"

print(mensagem)

# Exercício 39: Calcular a área do triânlugo a partir da base a altura fornecidos pelo usuário.
while True:
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    if base <= 0 or altura <= 0:
        print("Valor(es) inváido(s)!")
    else:
        area = base * altura / 2
        print(f"A área do triângulo de base {base} e altura {altura} é {area}.")
        break

# Exercício 40: Ler números inteiros até que seja digitado um valor negativo. Exibir o maior valor digitado.
num = 0
maior_valor = 0
mensagem = "O maior valor inserido foi "

while num >= 0:
    num = int(input("Digite um número inteiro positivo: "))
    if num > maior_valor:
        maior_valor = num

mensagem += f"{maior_valor}."
print(mensagem)

# Exercício 41: Calcular resistência equivalente de dois valores fornecidos pelo usuário. Encerrar o digitar 0.
while True:
    r1 = float(input("Valor do resistor 1: "))
    r2 = float(input("Valor do resistor 2: "))

    if r1 != 0 and r2 != 0:
        req = (r1 * r2) / (r1 + r2)
        print(f"A resistência equivalente de R1 = {r1} e R2 = {r2} é {req}.")
    else:
        print("Operação encerrada pelo usuário (código 0).")
        break

# Exercício 42: Ler números e apresentar o cubo, quadrado e raíz quadrada. Encerrar ao digitar 0 ou valores negativos.
while True:
    num = int(input("Digite um número: "))

    if num <= 0:
        print("Valor menor ou igual a zero inserido. Encerrando...")
        break
    else:
        mensagem = f"O cubo de {num} é {num ** 3}.\n"
        mensagem += f"O quadrado de {num} é {num ** 2}.\n"
        mensagem += f"O a raíz de {num} é {num ** (1/int(2))}.\n"
        print(mensagem)

# Exercício 43: Ler as idades inseridas e imprimir a média. Encerrar quando a idade for 0.
idades = 0
soma = 0

while True:
    num = int(input("Digite um número: ")).__abs__()

    if num == 0:
        print("Idade igual a 0. Encerrando...")
        break
    else:
        soma += num
        idades += 1
        media = round(soma / idades, 2)

        print(f"Último valor de idade: {num}.\nIdades lidas: {idades}\nMedia das idades: {media}.")

# Exercício 44: Ler um valor positivo e apresentar a sequência Fibonacci até o primeiro número superior ao lido.
num = int(input("Digite um número inteiro positivo: ")).__abs__()
i = 1

novo = 0
fibonnaci = 0
anterior = 0

if num == 0:
    print("Número inválido. Encerrando...")
else:
    while i <= num + 1:
        print((i, fibonnaci))
        if fibonnaci == 0:
            fibonnaci += 1
        else:
            novo = fibonnaci + anterior
            anterior = fibonnaci
            fibonnaci = novo
        i += 1

print(f"O {num + 1}º termo da sequência Fibonnaci é {anterior}.")

# Exercício 45: Converter velocidades de de km/h para m/s e vice-versa. Criar um comando para finalizar.
instrucao = "1-Conversor km/h -> m/s\n" \
            "2-Conversor m/s -> km/h\n" \
            "Outro comando-Encerrar programa\n"

while True:
    msg = input(instrucao + "Insira o comando: ").lower()

    if msg == '1':
        print("\nConversor km/h -> m/s")
        velocidade = float(input("Velocidade = "))
        ms = round(velocidade / 3.6, 2)
        print(f"\n{velocidade} km/h é igual a {ms} m/s.\n")
    elif msg == '2':
        print("\nConversor m/s -> km/h")
        velocidade = float(input("Velocidade = "))
        kmh = round(velocidade * 3.6, 2)
        print(f"\n{velocidade} m/s é igual a {kmh} km/h.\n")
    else:
        print("Encerrando...")
        break

# Exercício 46: Gerar um número aleatório e pedir pro usuário acertar. Encerrar quando o usuário acertar.
num = random.randint(1, 1001)
chute = None

while chute != num:
    chute = int(input("Digite um número de 1 a 1000. "))
    diferenca = (num - chute).__abs__()

    if 1 <= diferenca <= 25:
        print("Tá quente!")
    elif 26 <= diferenca <= 50:
        print("Você está perto.")
    elif 51 <= diferenca <= 75:
        print("Você está ficando longe...")
    elif 76 <= diferenca <= 100:
        print("Tá frio!")
    elif diferenca > 100:
        print("PQP, o Sol tá mais perto!")

print("Acertou!")

# Exercício 47: Apresentar um menu de operações para o usuário.
mensagem = "Operações disponíveis:\n" \
           "1-Adição\n" \
           "2-Subtração\n" \
           "3-Multiplicação\n" \
           "4-Divisão\n" \
           "Selecione a operação: "

while True:
    opcao = input(mensagem)

    if opcao == '1':
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
        operacao = num1 + num2
        print(f"A soma de {num1} e {num2} é {operacao}.")
    elif opcao == '2':
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
        operacao = num1 - num2
        print(f"A diferença de {num1} e {num2} é {operacao}.")
    elif opcao == '3':
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
        operacao = num1 * num2
        print(f"O produto de {num1} e {num2} é {operacao}.")
    elif opcao == '4':
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
        operacao = num1 / num2
        print(f"A razão entre {num1} e {num2} é {operacao}.")
    elif opcao == '5':
        print("Encerrando programa...")
        break
    else:
        print("Comando inválido!")

# Exercício 48: Somar os valores pares da sequência de Fibonacci cuja soma não ultrapasse 4.000.000
i = 1

novo = 0
fibonnaci = 0
anterior = 0
soma_pares = 0

while novo <= 4_000_000:

    print((i, fibonnaci))

    if fibonnaci == 0:
        fibonnaci += 1
    else:
        novo = fibonnaci + anterior
        anterior = fibonnaci
        fibonnaci = novo

    if novo % 2 == 0:
        soma_pares += novo

    i += 1

print(f"A soma dos números de Fibonacci pares abaixo de 4.000.000 é {soma_pares}.")

# Exercício 49: Comparar duas aplicações financeiras e descobrir quanto tempo leva para que uma passe a outra.
salario_Joao = 1000
salario_Carlos = salario_Joao * 3

aplicacao_Carlos = 0
aplicacao_Joao = 0

mes = 0

while aplicacao_Joao <= aplicacao_Carlos:
    if mes == 0:
        aplicacao_Carlos = salario_Carlos * 1.02
        aplicacao_Joao = salario_Joao * 1.05
    else:
        aplicacao_Joao *= 1.05
        aplicacao_Carlos *= 1.02
    mes += 1
    print((mes, aplicacao_Carlos, aplicacao_Joao))

print(f"Serão necessários {mes} meses para que a aplicação de João se iguale ou supere a de Carlos.")

# Exercício 50: Comparar a altura de duas pessoas e descobrir o tempo necessário pra uma passar a outra.
altura_Chico = 1.50
altura_Ze = 1.10
anos = 0

while altura_Chico >= altura_Ze:
    altura_Chico += .02
    altura_Ze += .03
    anos += 1

print(f"Levará {anos} anos para que Zé seja mais alto que Chico.")

# Exercício 51: Calcular salário do funcionário, sabendo que o aumento dobra a cada ano.
salario = 2000
ano = 1995
aumento = .015

while ano <= 2000:
    ano += 1
    salario *= (1 + aumento)
    aumento *= 2

print(f"Em {ano}, o salário é de R$ {salario},00")

# Exercício 52: Receber o valor de saque do usuário e entregar o menor número possível de notas.
saque = int(input("Digite o valor a ser sacado: "))
soma_notas = 0
mensagem = "Serão entregues ao usuário:\n"

notas100, notas50, notas20, notas10, notas5, notas2, notas1 = 0, 0, 0, 0, 0, 0, 0

while saque >= 100:
    saque -= 100
    notas100 += 1

if notas100 > 0:
    mensagem += f"{notas100} notas de R$ 100,00\n"

while saque >= 50:
    saque -= 50
    notas50 += 1

if notas50 > 0:
    mensagem += f"{notas50} notas de R$ 50,00\n"

while saque >= 20:
    saque -= 20
    notas20 += 1

if notas20 > 0:
    mensagem += f"{notas20} notas de R$ 20,00\n"

while saque >= 10:
    saque -= 10
    notas10 += 1

if notas10 > 0:
    mensagem += f"{notas10} notas de R$ 10,00\n"

while saque >= 5:
    saque -= 5
    notas5 += 1

if notas5 > 0:
    mensagem += f"{notas5} notas de R$ 5,00\n"

while saque >= 2:
    saque -= 2
    notas2 += 1

if notas2 > 0:
    mensagem += f"{notas2} notas de R$ 2,00\n"

while saque >= 1:
    saque -= 1
    notas1 += 1

if notas1 > 0:
    mensagem += f"{notas1} notas de R$ 1,00"

print(mensagem)

# Exercício 53: Ler um inteiro e imprimir o Triânguloe de Floyd
num = int(input("Digite um inteiro: ")).__abs__()
i, n = 1, 0

while i <= num:
    j = 1
    while j <= i:
        n += 1
        print(n, end=' ')
        j += 1
    print()
    i += 1

# Exercício 54: Receber um inteiro maior que 1 e dizer se o número é primo o não.
while True:
    num = int(input("Digite um número: ")).__abs__()

    if num == 1:
        print("Encerrando...")
        break
    else:
        divisores = 0
        for c in range(1, num + 1):
            if num % c == 0:
                divisores += 1

        if divisores == 2:
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")

# Exercício 55: Receber um inteiro N e imprimir a soma dos N primeiros números primos.
termos = int(input("Digite um número: ")).__abs__()
ciclos = 0
soma = 0
numero = 2

while ciclos < termos:
    divisores = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            divisores += 1

    if divisores == 2:
        soma += numero
        ciclos += 1

    numero += 1

print(f"A soma dos {termos} primeiros números primos é {soma}.")

# Exercício 56: Calcular a soma de todos os números primos abaixo de 2.000.000
numeros_primos = 0
for cont in range(0, 2_000_000):
    divisores = 0
    for div in range(1, cont + 1):
        print(cont, div)
        if cont % div == 0:
            divisores += 1

    if divisores == 2:
        numeros_primos += 1

print(f"Abaixo de 2.000.000 existem {numeros_primos} números primos.")

# Exercício 57: Reber dois valores A e B e imprimir quantos números primos existem nesse intervalo.
a = int(input("Digite o primeiro número: ")).__abs__()
b = int(input("Digite o segundo número: ")).__abs__()
primos = 0

for c in range(a + 1, b):
    divisores = 0
    for d in range(1, c + 1):
        if c % d == 0:
            divisores += 1

    if divisores == 2:
        primos += 1

print(f"Entre {a} e {b} existem {primos} números primos.")

# Exercício 58: Somar os números primos entre A e B.
a = int(input("Digite o primeiro número: ")).__abs__()
b = int(input("Digite o segundo número: ")).__abs__()
soma = 0

for c in range(a + 1, b):
    divisores = 0
    for d in range(1, c + 1):
        if c % d == 0:
            divisores += 1

    if divisores == 2:
        soma += c

print(f"A soma dos números primos entre {a} e {b} é {soma}.")

# Exercício 59: Ler o número de habitantes, código de consumidor, e consumo mensal. Imprimir maior, menor e média.
habitantes = int(input("Número de habitantes da cidade: "))
media_consumo = 0
consumo_cod1, consumo_cod2, consumo_cod3 = 0, 0, 0
maior_consumo = 0
menor_consumo = 1_000_000

for h in range(0, habitantes):
    consumo = int(input("Consumo em kwh: "))
    codigo = input("Código do consumidor: ")

    if consumo > maior_consumo:
        maior_consumo = consumo
    if consumo < menor_consumo:
        menor_consumo = consumo

    if codigo == '1':
        consumo_cod1 += consumo
    elif codigo == '2':
        consumo_cod2 += consumo
    else:
        consumo_cod3 += consumo


media = (consumo_cod1 + consumo_cod2 + consumo_cod3) / habitantes

print(f"O maior consumo foi de {maior_consumo} kwh.\n"
      f"O menor consumo foi de {menor_consumo} kwh.\n"
      f"A média do consumo foi de {media_consumo} kwh.\n"
      f"Os consumidores residenciais tiveram ao todo, um consumo de {consumo_cod1} kwh.\n"
      f"Os consumidores comerciais tiveram ao todo, um consumo de {consumo_cod2} kwh.\n"
      f"Os consumidores industriais tiveram ao todo, um consumo de {consumo_cod3} kwh.\n")

# Exercício 60: Ler vários números e imprimir uma série de resultados de operações.
soma = 0
numeros = 0
media = 0
maior_numero = 0
menor_numero = 1_000_000
media_pares = 0

while True:
    num = int(input("Digite um número. 0 encerra o programa e exibe os resultados.\n"))

    if num == 0:
        print("Encerrando...")
        break

    soma += num
    numeros += 1

    if num > maior_numero:
        maior_numero = num

    if num < menor_numero:
        menor_numero = num

    if num % 2 == 0:
        media_pares += num

media = soma / numeros
media_pares /= numeros

print(f"A soma dos números é {soma}.\n"
      f"Foram digitados {numeros} números.\n"
      f"A média é de {media}.\n"
      f"O maior número foi digitado foi {maior_numero}.\n"
      f"O menor número foi digitado foi {menor_numero}.\n"
      f"A média dos números pares foi {media_pares}.")

# Exercício 61: Encontrar o maior palíndromo resultante do produto de dois números de três dígitos.
maior_palindromo = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        numero = x * y
        string = str(numero)
        print(x, y, numero)

        if len(string) == 5:
            if string[0] == string[4] and string[1] == string[3]:
                if numero > maior_palindromo:
                    maior_palindromo = numero
                    m = x
                    n = y
        elif len(string) == 6:
            if string[0] == string[5] and string[1] == string[4] and string[2] == string[3]:
                if numero > maior_palindromo:
                    maior_palindromo = numero
                    m = x
                    n = y

print(f"O maior palíndromo resultante do produto de dois números de três dígitos é {maior_palindromo},"
      f"produto de {m} e {n}.")

# Exercício 62: Contar o número de letras necessárias para escrever, de forma literal, os números de 1 a .1000.
total = ""

for i in range(1, 1001):
    num = num2words(i, lang='pt-BR')
    total += num.replace(' ', '')

# A função replace(a, b) substitui caracteres iguais ao primeiro parâmetro por carcateres iguais ao segundo.

print(f"Escritos de forma literal, os números de 1 a 1.000 têm {len(total)} caracteres.")