"""
math é uma biblioteca de operações matematicas como sqrt() e log() (raíz quadrada e logaritmo, respectivamente).
sintaxes:
- sqrt(número)
- log(numero, base)

random é utilizada para gerar valores aleatórios dentro de um intervalo.
sintaxes:
-random.randint(menor_valor, maior_valor)

"""
import math
import random


# Exercício 1: Receber dois números e imprimir o maior.
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

# Exercício 2: Receber um número. Se o número for positivo, calcular a raíz quadrada. Se não, dizer que é inválido.
num = float(input("Inserir número: "))

if num >= 0:
    print(num ** (1 / int(2)))
else:
    print("Número inválido.")

# Exercício 3: Ler um número real. Imprimir raíz quadrada se for positivo e o quadrado do número se for negativo.
num = float(input("Inserir número: "))

if num >= 0:
    print(num ** (1 / int(2)))
else:
    print(num ** 2)

# Exercício 4: Mostrar a raíz quadrada e o quadrado de um número se este for positivo.
num = float(input("Inserir número: "))
if num >= 0:
    print(num ** (1 / int(2)))
    print(num ** 2)

# Exercício 5: Verificar se o número recebido é par ou impar.
num = float(input("Inserir número: "))

if num % 2 == 0:
    print(f"{num} é número par.")
else:
    print(f"{num} é número ímpar.")

# Exercício 6: Receber dois números e imprimir o maior, bem como a diferença entre eles.
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if num1 > num2:
    print(num1)
    print(num1 - num2)
else:
    print(num2)
    print(num2 - num1)

# Exercício 7: Receber dois números e mostrar o maior. Dizer também quando são iguais.
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if num1 > num2:
    print(num1)
elif num1 == num2:
    print("Números iguais.")
else:
    print(num2)

# Exercício 8: Receber duas notas válidas (0 a 10) e calcular a média. Se for inválida, avisar o usuário e encerrar.
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

if (nota1 <= 10 and nota1 >= 0) and (nota2 <= 10 and nota1 >= 0):
    media = (nota1 + nota2) / 2
    print(media)
else:
    print("Nota(s) inválida(s).")

# Exercício 9: Determinar se um empréstimo será concedido ou não. A prestação deve ser no máximo, 20% do salário.
salario = float(input("Salário: "))
prestacao = float(input("Valor da prestação: "))

if prestacao / salario > 0.2:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")

# Exercício 10: Receber altura e sexo do usuário e retornar o peso ideal.
sexo = input("Sexo (SÓ EXISTE MASCULINO E FEMININO!!!): ").lower()
altura = float(input("Sua altura: "))

if sexo == "masculino" or sexo == 'm':
    peso = 72.7 * altura - 58
elif sexo == "feminino" or sexo == 'f':
    peso = 62.1 * altura - 44.7

print(peso)

# Exercício 11: Ler um número maior que zero e retornar a soma de seus algarismos.
# OBS.: Para evitar o uso de funções e estruturas não vistas até agora, é recomendado limitar o número de algarismos.
numero = int(input("Inserir número de até 4 dígitos: "))

m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10
# Obtemos o módulo da divisão por 10 para obtermos o valor de cada casa do número.

if 0 < numero <= 9999:
    soma = m + c + d + u
    print(f"A soma dos algarismos de {numero} é {soma}.")
else:
    print("Número inválido.")

# Exercício 12: Ler um número inteiro. Se for positivo, calcular o logaritmo. Se não, avisar que o número é inválido.
num = int(input("Inserir número: "))

if num <= 0:
    print("Número inválido.")
else:
    log_num = math.log(num, 10)
    print(log_num)

# Exercício 13: Média ponderada de 3 provas (pesos: 1, 1, 2). Para aprovar, a média deve ser superior a 60.
nota1 = float(input("Nota da prova 1 (0 a 100): "))
nota2 = float(input("Nota da prova 2 (0 a 100): "))
nota3 = float(input("Nota da prova 3 (0 a 100): "))

if 0 <= nota1 and nota2 and nota3 <= 100:
    media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4
else:
    print("NOTA(S) INVÁLIDA(S)!")

if media_ponderada >= 60:
    print(f"Aluno aprovado com média {media_ponderada}.")
else:
    print(f"Aluno reprovado com média {media_ponderada}.")

# Exercício 14: Média ponderada de 3 notas (pesos: 2, 3, 5). Critérios: 0 - 2,9 (reprovado), 3 - 4,9 (recuperação).
print("Inserir notas de 0 a 10.\n")
nota_lab = float(input("Nota da atividade de laboratório: "))
nota_aval = float(input("Nota da avaliação semestral: "))
nota_exame = float(input("Nota do exame final: "))

if 0 <= nota_lab and nota_aval and nota_exame <= 10:
    media_ponderada = (nota_lab * 2 + nota_aval * 3 + nota_exame * 5) / 10
else:
    print('NOTA(S) INVÁLIDA(S)!')

if 0 <= media_ponderada <= 2.9:
    print(f"Aluno reprovado com média {media_ponderada}.")
elif 3.0 <= media_ponderada <= 4.9:
    print(f"Aluno de recuperação com média {media_ponderada}.")
else:
    print(f"Aluno aprovado com média {media_ponderada}.")

# Exercício 15: Ler um inteiro de 1 a 7 e retornar o dia da semana equivalente.
dia = int(input("Digite um inteiro de 1 a 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("NÚMERO INVÁLIDO!")

# Exercício 16: Ler um inteiro de 1 a 12 e retornar o mês equivalente.
mes = int(input("Digite um inteiro de 1 a 12: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("NÚMERO INVÁLIDO!")

# Exercício 17: Calcular a área do trapézio. Os valores devem ser TODOS positivos.
base_menor = float(input("Valor da base menor: "))
base_maior = float(input("Valor da base maior: "))
altura = float(input("Valor da altura: "))

if (base_menor or base_maior or altura) <= 0 or (base_menor > base_maior):
    print("VALOR(ES) INVÁLIDO(S)!")
else:
    area = (base_maior + base_menor) * altura / 2
    print(f"A área do trapézio é {area}.")

# Exercício 18: Apresentar um menu com 4 operações matemáticas. O usuário seleciona uma e o programa a realiza.
mensagem = "Selecione a operação que deseja realizar:" \
            "" \
            "+ (adição)" \
            "- (subtração)" \
            "* (multiplicação)" \
            "/ (divisão)" \
            "" \
            "Opção: " \

opcao = input(mensagem)

if opcao == '+':
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
    operacao = num1 + num2
    print(f"A soma de {num1} e {num2} é {operacao}.")
elif opcao == '-':
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
    operacao = num1 - num2
    print(f"A diferneça de {num1} e {num2} é {operacao}.")
elif opcao == '*':
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
    operacao = num1 * num2
    print(f"O produto de {num1} e {num2} é {operacao}.")
elif opcao == '/':
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
    if num2 != 0:
        operacao = num1 / num2
        print(f"A soma de {num1} e {num2} é {operacao}.")
    else:
        print("NÃO SE DIVIDE POR ZERO, ANIMAAAAL!")
else:
    print("Operação inválida/inexistente.")

# Exercício 19: Verificar se um número é divísivel por 3 ou 5, mas não pelos dois simultaneamente.
num = float(input("Digite um número: "))

if num % 15 == 0:
    print(f"{num} é inválido.")
elif num % 3 == 0 and num % 5 != 0:
    print(f"{num} é divisível por 3.")
elif num % 3 != 0 and num % 5 == 0:
    print(f"{num} é divisível por 5.")
else:
    print(f"{num} não é divisível nem por 3 nem por 5.")

# Exercício 20: Receber 3 segmentos e definir se é um triângulo ou não e se é equilátero, isóceles ou escaleno.
seg_A = float(input("Valor do segmento A: "))
seg_B = float(input("Valor do segmento B: "))
seg_C = float(input("Valor do segmento C: "))

if not (seg_A < seg_B + seg_B and seg_B < seg_A + seg_C and seg_C < seg_A + seg_B):
    print("ABC não é um triângulo.")
else:
    if seg_A == seg_B and seg_B == seg_C:
        print("ABC é um triângulo equilátero.")
    elif seg_A == seg_B and seg_B != seg_C:
        print("ABC é um triângulo isóceles.")
    else:
        print("ABC é um triângulo escaleno.")

# Exercício 21: Apresentar um menu de operações. A subtração é do maior pelo menor e não pode haver divisão por zero.
mensagem = "Selecione uma das operações abaixo:\n" \
           "\n" \
           "1-Adição\n" \
           "2-Subtração (Maior pelo menor)\n" \
           "3-Multiplicação\n" \
           "4-Divisão (O denominador não pode ser zero)\n" \
           "\n" \
           "Opção: "

opcao = input(mensagem)

operacao = None

if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    print("OPERAÇÃO INVÁLIDA/INEXISTENTE!")
else:
    num1 = float(input("Insira o primeiro valor: "))
    num2 = float(input("Insira o segundo valor: "))

    if opcao == '1':
        operacao = num1 + num2
    elif opcao == '2':
        if num1 > num2:
            operacao = num1 - num2
        else:
            print("Subtração apenas do maior pelo menor.")
    elif opcao == '3':
        operacao = num1 * num2
    elif opcao == '4':
        if num2 != 0:
            operacao = num1 / num2
        else:
            print("NÃO EXISTE DIVISÃO POR ZERO!")
    print(f"Resultado da operação: {operacao}.")

# Exercício 22: Ler a idade e o tempo de contribuíção de um trabalhador e retornar se esse pode ou não se aposentar.
idade = int(input("Idade (em anos): "))
tempo = int(input("Tempo de contribuíção (em anos): "))

if idade >= 65 or tempo >= 30 or (idade >= 50 and tempo >= 25):
    print("Trabalhador pode se aposentar.")
else:
    print("Trabalahdor ainda não pode se aposentar.")

# Exercício 23: Determinar se um ano é bissexto (divisível por 4, 400 e não por 100)
ano = int(input("Digite o ano: "))

if ano % 100 == 0 and ano % 400 == 0:
    print(f"{ano} é ano bissexto.")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é ano bissexto.")
else:
    print(f"{ano} não é ano bissexto.")

# Exercício 24: Calcular o imposto sobre o valor de um produto de acordo com o estado.
valor = float(input("Inserir valor do produto: "))
estado = input("Estado de destino do produto (apenas a sigla): ").upper()

preco_final = None

if estado == "MG":
    preco_final = round(valor * 1.07, 2)
elif estado == "MS":
    preco_final = round(valor * 1.08, 2)
elif estado == "RJ":
    preco_final = round(valor * 1.15)
elif estado == "SP":
    preco_final = round(valor * 1.12, 2)
else:
    print("Estado não atendido.")

print(f"O preço do produto é R$ {preco_final}.")

# Exercício 25: Resolver equação de segundo grau. Avisar no caso do coeficiente 'a' ser igual a 0.
a = int(input("Insira o coeficiente de segundo grau: "))
b = int(input("Insira o coeficiente de primeiro grau: "))
c = int(input("Insira o coeficiente independente: "))

mensagem = ""
equacao = f"({a})x² + ({b})x + ({c}) = 0"

if a == 0:
    mensagem = f"A equação {equacao} tem coeficiente 'a' igual a 0. Não é equação de segundo grau."
    print(mensagem)
else:
    mensagem = f"\n  Equação: " + equacao
    print(mensagem)

    x1, x2 = 0, 0

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        print(f"\n  Delta > 0. Equação {equacao} tem duas raízes reais.")

        x1 = round((-b + math.sqrt(delta)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(delta)) / (2 * a), 2)

        print(f"As raízes de {equacao} são: {x1} e {x2}.")

    elif delta == 0:
        print(f"\n  Delta > 0. Equação {equacao} tem uma raíz real.\n")

        x1 = round(-b / (2 * a), 2)

        print(f"A raíz de {equacao} é {x1}.")

    else:
        print(equacao + " não possui raízes reais.")

# Exercício 26: Ler o rendimento de um carro e retornar mensagens de acordo com o valor.
rendimento = float(input("Rendimento do carro (em km/l): "))

if rendimento < 8:
    print("Venda o carro!")
elif 8 <= rendimento <= 14:
    print("Econômico.")
else:
    print("Super econômico!")

# Exercício 27: Classificar um atleta de acordo com sua idade.
idade = int(input("Digite a idade: "))

if 5 <= idade <= 7:
    categoria = "Infantil A."
    mensagem = "Atleta pertencente à categoria " + categoria
elif 8 <= idade <= 10:
    categoria = "Infantil B."
    mensagem = "Atleta pertencente à categoria " + categoria
elif 11 <= idade <= 13:
    categoria = "Juvenil A."
    mensagem = "Atleta pertencente à categoria " + categoria
elif 14 <= idade <= 17:
    categoria = "Juvenil B."
    mensagem = "Atleta pertencente à categoria " + categoria
elif idade >= 18:
    categoria = "Sênior."
    mensagem = "Atleta pertencente à categoria " + categoria
else:
    mensagem = "Não é possível categorizar."

print(mensagem)

# Exercício 28: Receber 3 valores inteiros positivos e calcular as médias geométrica, ponderada, harmônica e aritimética
print("Digite três números inteiros.")
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Terceiro valor: "))

mensagem = "Selecionar a operação:" + "\n\n" \
            "a) Média Geométrica" + "\n" \
            "b) Média Ponderada" + "\n" \
            "c) Média Harmônica" + "\n" \
            "d) Média Aritimética" + "\n\n" \
            "Opção: "

operacao = input(mensagem).lower()
media = 0

if operacao == 'a':
    operacao = "geométrica"
    media = round((x * y * z) ** 1 / int(3), 2)
    mensagem = f"A média {operacao} de {x}, {y}, e {z} é {media}."
elif operacao == 'b':
    operacao = "ponderada"
    media = round((1 * x + 2 * y + 3 * z) / 6, 2)
    mensagem = f"A média {operacao} de {x}, {y}, e {z} é {media}."
elif operacao == 'c':
    operacao = "harmônica"
    media = round((1 / ((1 / x) + (1 / y) + (1 / z))), 2)
    mensagem = f"A média {operacao} de {x}, {y}, e {z} é {media}."
elif operacao == 'd':
    operacao = "aritimética"
    media = round((x + y + z) / 3, 2)
    mensagem = f"A média {operacao} de {x}, {y}, e {z} é {media}."
else:
    mensagem = "Comando inválido."

print(mensagem)

# Exercício 29: Fazer cinco perguntas de soma de números aleatórios de 1 a 99 e contar o número de acertos.
# 1
a = random.randint(1, 99)
b = random.randint(1, 99)

soma = a + b
acertos = 0

resposta = int(input(f"A soma de {a} e {b} é: "))

if resposta == soma:
    print("ACERTOU!")
    acertos += 1
else:
    print("ERROU!")

# 2
a = random.randint(1, 99)
b = random.randint(1, 99)

soma = a + b

resposta = int(input(f"A soma de {a} e {b} é: "))

if resposta == soma:
    print("ACERTOU!")
    acertos += 1
else:
    print("ERROU!")

# 3
a = random.randint(1, 99)
b = random.randint(1, 99)

soma = a + b

resposta = int(input(f"A soma de {a} e {b} é: "))

if resposta == soma:
    print("ACERTOU!")
    acertos += 1
else:
    print("ERROU!")

# 4
a = random.randint(1, 99)
b = random.randint(1, 99)

soma = a + b

resposta = int(input(f"A soma de {a} e {b} é: "))

if resposta == soma:
    print("ACERTOU!")
    acertos += 1
else:
    print("ERROU!")

# 5
a = random.randint(1, 99)
b = random.randint(1, 99)

soma = a + b

resposta = int(input(f"A soma de {a} e {b} é: "))

if resposta == soma:
    print("ACERTOU!")
    acertos += 1
else:
    print("ERROU!")

print(f"Você acertou {acertos} questões.")

# Exercício 30: Receber 3 números e mostrar em ordem crescente.
num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Terceiro valor: "))

if num1 <= num2 <= num3:
    print(f"A ordem dos números é: {num1}, {num2}, {num3}.")
elif num1 <= num3 <= num2:
    print(f"A ordem dos números é: {num1}, {num3}, {num2}.")
elif num2 <= num1 <= num3:
    print(f"A ordem dos números é: {num2}, {num1}, {num3}.")
elif num2 <= num3 <= num1:
    print(f"A ordem dos números é: {num2}, {num3}, {num1}.")
elif num3 <= num1 <= num2:
    print(f"A ordem dos números é: {num3}, {num1}, {num2}.")
elif num3 <= num2 <= num1:
    print(f"A ordem dos números é: {num3}, {num2}, {num1}.")

# Exercício 31: Mostrar a classificação de uma pessoa de acordo com seu peso e altura.
peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

classificacao = ''

if peso <= 60:
    if altura < 1.2:
        classificacao = 'A'
    elif 1.2 <= altura <= 1.7:
        classificacao = 'B'
    else:
        classificacao = 'C'
elif 60 < peso <= 90:
    if altura < 1.2:
        classificacao = 'D'
    elif 1.2 <= altura <= 1.7:
        classificacao = 'E'
    else:
        classificacao = 'F'
else:
    if altura < 1.2:
        classificacao = 'G'
    elif 1.2 <= altura <= 1.7:
        classificacao = 'H'
    else:
        classificacao = 'I'

print("Classificação: " + classificacao)

# Exercício 32: Selecionar uma opção de um menu de lanchonete e digitar a quantidade.
preco0 = 1.20
preco1 = 1.30
preco2 = 1.50
preco3 = 1.20
preco4 = 1.70
preco5 = 2.20
preco6 = 1.00

mensagem = "Selecione seu pedido e a quantidade:\n" \
           "Pedido\t\t\t\tCódigo\t\tPreço\n\n" \
           f"Cachorro quente\t\t100\t\t\tR$ {preco0}\n" \
           f"Bauru simples  \t\t101\t\t\tR$ {preco1}\n" \
           f"Bauru com ovo  \t\t102\t\t\tR$ {preco2}\n" \
           f"Hamburguer     \t\t103\t\t\tR$ {preco3}\n" \
           f"Cheeseburguer  \t\t104\t\t\tR$ {preco4}\n" \
           f"Suco           \t\t105\t\t\tR$ {preco5}\n" \
           f"Refrigerante   \t\t106\t\t\tR$ {preco6}\n" \
           "\n" \
           "Digite o código de seu pedido: "

codigo = input(mensagem)

if codigo == "100":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco0 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "101":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco1 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "102":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco2 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "103":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco3 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "104":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco4 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "105":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco5 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
elif codigo == "106":
    quantidade = int(input("Digite a quantidade: "))
    preco = preco6 * quantidade
    mensagem = f"O preço do seu pedido é de R$ {preco}."
else:
    mensagem = "Código inválido."

print(mensagem)

# Exercício 33: Calcular o novo preço de um produto e classificar esse preço.
preco_antigo = float(input("Preço antigo do produto: "))
preco_novo = 0
classificacao = ""

if preco_antigo < 0:
    print("Preço inválido.")
elif preco_antigo <= 50:
    preco_novo = round(preco_antigo * 1.05, 2)
elif 50 < preco_antigo <= 100:
    preco_novo = round(preco_antigo * 1.1, 2)
else:
    preco_novo = round(preco_antigo * 1.15, 2)

if 0 < preco_novo <= 80:
    classificacao = "Barato."
    print(f"A R$ {preco_novo}, o produto pode ser considerado " + classificacao)
elif 80 < preco_novo <= 120:
    classificacao = "Normal."
    print(f"A R$ {preco_novo}, o produto pode ser considerado " + classificacao)
elif 120 < preco_novo <= 200:
    classificacao = "Caro."
    print(f"A R$ {preco_novo}, o produto pode ser considerado " + classificacao)
else:
    classificacao = "Muito Caro."
    print(f"A R$ {preco_novo}, o produto pode ser considerado " + classificacao)

# Exercício 34: Ler as notas e as faltas de um aluno, atribuindo-lhe um conceito de A até F.
nota = float(input("Insira a nota do aluno: "))
faltas = int(input("Insira o número de faltas do aluno: "))

if nota < 0 or nota > 10 or faltas < 0:
    print("Valor(es) inválido(s)!\nApenas valores de 0 a 10 para notas e maiores que 0 para faltas.")
else:
    conceito = ''

    if 9 <= nota <= 10:
        if faltas <= 20:
            conceito = 'A'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
        else:
            conceito = 'B'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
    elif 7.5 <= nota < 9:
        if faltas <= 20:
            conceito = 'B'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
        else:
            conceito = 'C'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
    elif 5 <= nota < 7.5:
        if faltas <= 20:
            conceito = 'C'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
        else:
            conceito = 'D'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
    elif 4 <= nota < 5:
        if faltas <= 20:
            conceito = 'D'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
        else:
            conceito = 'E'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
    elif 0 <= nota < 4:
        if faltas <= 20:
            conceito = 'E'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")
        else:
            conceito = 'F'
            print(f"Com nota {nota} e {faltas} falta(s), foi atribuído ao aluno conceito {conceito}.")

# Exercício 35: Receber uma data e verificar se é válida (se o ano é bissexto e se o dia existe no mês).
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

ano_bissexto = False

if dia < 0 or mes < 0 or mes > 12:
    print("Data inválida!")
else:
    data = f"{dia}/{mes}/{ano}"
    print(f"Data inserida: {data}.")

    if ano % 100 == 0 and ano % 400 == 0:
        ano_bissexto = True
    elif ano % 4 == 0 and ano % 100 != 0:
        ano_bissexto = True
    else:
        ano_bissexto = False

    if mes == 1:
        if dia > 31:
            print(f"Não existe dia {dia} em Janeiro!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 2:
        if (ano_bissexto and dia <= 29) or (not ano_bissexto and dia <= 28):
            print(f"{data} é uma data válida.")
        elif not ano_bissexto and dia == 29:
            print(f"Não existe dia {dia} de Fevereiro em ano não-bissexto!")
        else:
            print(f"Não existe dia {dia} em Fevereiro.")
    elif mes == 3:
        if dia > 31:
            print(f"Não existe dia {dia} em Março!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 4:
        if dia > 30:
            print(f"Não existe dia {dia} em Abril!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 5:
        if dia > 31:
            print(f"Não existe dia {dia} em Maio!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 6:
        if dia > 30:
            print(f"Não existe dia {dia} em Junho!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 7:
        if dia > 31:
            print(f"Não existe dia {dia} em Julho!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 8:
        if dia > 30:
            print(f"Não existe dia {dia} em Agosto!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 9:
        if dia > 30:
            print(f"Não existe dia {dia} em Setembro!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 10:
        if dia > 31:
            print(f"Não existe dia {dia} em Outubro!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 11:
        if dia > 30:
            print(f"Não existe dia {dia} em Novembro!")
        else:
            print(f"{data} é uma data válida.")
    elif mes == 12:
        if dia > 31:
            print(f"Não existe dia {dia} em Dezembro!")
        else:
            print(f"{data} é uma data válida.")

# Exercício 36: Calcular a comissão paga ai um vendedor.
vendas = float(input("Venda mensal em reais: "))

if vendas >= 100_000:
    comissao = round(vendas * 0.16 + 700, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
elif 80_000 <= vendas < 100_000:
    comissao = round(vendas * 0.14 + 650, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
elif 60_000 <= vendas < 80_000:
    comissao = round(vendas * 0.14 + 600, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
elif 40_000 <= vendas < 60_000:
    comissao = round(vendas * 0.14 + 550, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
elif 20_000 <= vendas < 40_000:
    comissao = round(vendas * 0.14 + 500, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
elif 0 <= vendas < 20_000:
    comissao = round(vendas * 0.14 + 400, 2)
    print(f"O valor da comissão do vendedor será de R$ {comissao}.")
else:
    print("DEMITE ESSE SUJEITO!!!")

# Exercício 37: Criar um sistema de parque de estacionamento. Receber hora, minuto e segundo. Arredondar tempo pra cima.
hora_inicial = int(input("Hora de chegada: ")).__abs__()
minuto_inicial = int(input("Minuto de chegada: ")).__abs__()
segundo_inicial = int(input("Segundo de chegada: ")).__abs__()
hora_final = int(input("Hora de saída: ")).__abs__()
minuto_final = int(input("Minuto de saída: ")).__abs__()
segundo_final = int(input("Segundo de saída: ")).__abs__()

if segundo_final < 0 or segundo_final > 59 or segundo_inicial < 0 or segundo_inicial > 59:
    print("VALOR(ES) DE HORA, MINUTO E/OU SEGUNDO INVÁLIDO(S)!!!")

elif minuto_final < 0 or minuto_final > 59 or minuto_inicial < 0 or minuto_inicial > 59:
    print("VALOR(ES) DE HORA, MINUTO E/OU SEGUNDO INVÁLIDO(S)!!!")

elif hora_final < 0 or hora_final > 23 or hora_inicial < 0 or hora_inicial > 23:
    print("VALOR(ES) DE HORA, MINUTO E/OU SEGUNDO INVÁLIDO(S)!!!")
else:
    preco = 0

    if segundo_final - segundo_inicial < 0:
        minuto_final -= 1
        segundos_totais = segundo_final + 60 - segundo_inicial
    else:
        segundos_totais = segundo_final - segundo_inicial

    if minuto_final - minuto_inicial < 0:
        hora_final -= 1
        minutos_totais = minuto_final + 60 - minuto_inicial
    else:
        minutos_totais = minuto_final - minuto_inicial

    if hora_final - hora_inicial < 0:
        horas_totais = hora_final + 24 - hora_inicial
    else:
        horas_totais = hora_final - hora_inicial

    if segundos_totais > 0:
        minutos_totais += 1
    if minutos_totais > 0:
        horas_totais += 1

    if horas_totais <= 2:
        preco += horas_totais * 1
    elif 2 < horas_totais <= 4:
        preco += horas_totais * 1.4
    else:
        preco = horas_totais * 2

    print(f"O valor do estacionamento foi de R$ {preco}.")

# Exercício 38: Receber uma data, a partir do ano de 2008, e verificar se esta é válida.
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

ano_bissexto = False

if dia < 0 or mes < 0 or mes > 12:
    print("Data inválida!")
else:
    data = f"{dia}/{mes}/{ano}"
    print(f"Data inserida: {data}.")

    if ano >= 2008:
        if ano % 100 == 0 and ano % 400 == 0:
            ano_bissexto = True
        elif ano % 4 == 0 and ano % 100 != 0:
            ano_bissexto = True
        else:
            ano_bissexto = False

        if mes == 1:
            if dia > 31:
                print(f"Não existe dia {dia} em Janeiro!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 2:
            if (ano_bissexto and dia <= 29) or (not ano_bissexto and dia <= 28):
                print(f"{data} é uma data válida.")
            elif not ano_bissexto and dia == 29:
                print(f"Não existe dia {dia} de Fevereiro em ano não-bissexto!")
            else:
                print(f"Não existe dia {dia} em Fevereiro.")
        elif mes == 3:
            if dia > 31:
                print(f"Não existe dia {dia} em Março!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 4:
            if dia > 30:
                print(f"Não existe dia {dia} em Abril!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 5:
            if dia > 31:
                print(f"Não existe dia {dia} em Maio!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 6:
            if dia > 30:
                print(f"Não existe dia {dia} em Junho!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 7:
            if dia > 31:
                print(f"Não existe dia {dia} em Julho!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 8:
            if dia > 30:
                print(f"Não existe dia {dia} em Agosto!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 9:
            if dia > 30:
                print(f"Não existe dia {dia} em Setembro!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 10:
            if dia > 31:
                print(f"Não existe dia {dia} em Outubro!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 11:
            if dia > 30:
                print(f"Não existe dia {dia} em Novembro!")
            else:
                print(f"{data} é uma data válida.")
        elif mes == 12:
            if dia > 31:
                print(f"Não existe dia {dia} em Dezembro!")
            else:
                print(f"{data} é uma data válida.")
    else:
        print("Data inválida. Favor inserir uma data a partir de 2008.")

# Exercício 39: Calcular o aumento de salário de acordo com o tempo de serviço, bem como um bônus.
salario = float(input("Salário: ")).__abs__()
tempo = int(input("Tempo de serviço em anos: ")).__abs__()
bonus = 0

if salario <= 500:
    if tempo < 1:
        bonus = 0
        mensagem = "Funcionário não terá direito a bônus."
    elif 1 <= tempo <= 3:
        bonus = round(100.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 4 <= tempo <= 6:
        bonus = round(200.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 7 <= tempo <= 10:
        bonus = round(300.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    else:
        bonus = round(500.0, 1)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."

    salario = salario * 1.25 + bonus
    print(mensagem + f" O novo salário será de R$ {salario}0.")

elif 500 < salario <= 1000:
    if tempo < 1:
        bonus = 0
        mensagem = "Funcionário não terá direito a bônus."
    elif 1 <= tempo <= 3:
        bonus = round(100.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 4 <= tempo <= 6:
        bonus = round(200.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 7 <= tempo <= 10:
        bonus = round(300.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    else:
        bonus = round(500.0, 1)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."

    salario = salario * 1.2 + bonus
    print(mensagem + f" O novo salário será de R$ {salario}0.")

elif 1000 < salario <= 1500:
    if tempo < 1:
        bonus = 0
        mensagem = "Funcionário não terá direito a bônus."
    elif 1 <= tempo <= 3:
        bonus = round(100.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 4 <= tempo <= 6:
        bonus = round(200.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 7 <= tempo <= 10:
        bonus = round(300.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    else:
        bonus = round(500.0, 1)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."

    salario = salario * 1.15 + bonus
    print(mensagem + f" O novo salário será de R$ {salario}0.")

elif 1500 < salario <= 2000:
    if tempo < 1:
        bonus = 0
        mensagem = "Funcionário não terá direito a bônus."
    elif 1 <= tempo <= 3:
        bonus = round(100.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 4 <= tempo <= 6:
        bonus = round(200.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 7 <= tempo <= 10:
        bonus = round(300.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    else:
        bonus = round(500.0, 1)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."

    salario = salario * 1.1 + bonus
    print(mensagem + f" O novo salário será de R$ {salario}0.")

elif salario > 2000:
    if tempo < 1:
        bonus = 0
        mensagem = "Funcionário não terá direito a bônus."
    elif 1 <= tempo <= 3:
        bonus = round(100.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 4 <= tempo <= 6:
        bonus = round(200.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    elif 7 <= tempo <= 10:
        bonus = round(300.0)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."
    else:
        bonus = round(500.0, 1)
        mensagem = f"Funcionário terá direito a R$ {bonus}0 de bônus."

    salario = salario + bonus
    print(mensagem + f" O novo salário será de R$ {salario}0.")

# Exercício 40: Calcular o preço de um carro com base em seu valor inicial, porcentagem do distribuídor e dos impostos.
valor_base = float(input("Valor base do veículo (em reais): "))

if valor_base <= 12_000:
    preco = round(valor_base * (1 + 0.05), 2)
    print(f"O preço final do carro é de R$ {preco}0.")
elif 12_000 < valor_base <= 25_000:
    preco = round(valor_base * (1 + 0.1 + 0.15), 2)
    print(f"O preço final do carro é de R$ {preco}0.")
else:
    preco = round(valor_base * (1 + 0.15 + 0.20), 2)
    print(f"O preço final do carro é de R$ {preco}0.")

# Exercício 41: Calcular o IMC de uma pessoa e retornar sua classificação.
altura = float(input("Sua altura: ")).__abs__()
peso = float(input("Seu peso: ")).__abs__()

imc = round(peso / (altura ** 2), 1)

if imc < 18.5:
    print(f"Seu IMC é de {imc}. Você está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print(f"Seu IMC é de {imc}. Você está saudável.")
elif 25 <= imc <= 29.9:
    print(f"Seu IMC é de {imc}. Você está acima do peso.")
elif 30 <= imc <= 34.9:
    print(f"Seu IMC é de {imc}. Você tem obesidade de grau I.")
elif 35 <= imc <= 39.9:
    print(f"Seu IMC é de {imc}. Você tem obesidade de grau II (severa).")
else:
    print(f"Seu IMC é de {imc}. Você tem obesidade de grau III (mórbida).")