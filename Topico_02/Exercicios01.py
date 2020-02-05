"""
A função round(), propriedade de números flutuantes (float) foi utilizada para
arredondar os valores para duas casas decimais.
Lembrar de usar essa função para arredondar valores AO ATRIBUÍ-LOS às variáveis
ou antes de imprimir o valor.

sintaxe:
valor_arredondado = round(valor_float, número_de_casas_a_exibir)

__abs__() é utilizado para obter o valor absoluto de um número. Isso significa
que mesmo que um número seja negativo, ele se tornará positivo após a chamada
dessa função.

P.S.: Números complexos não aceitam round()
"""

# Exercício 1: Ler um número inteiro e imprimir.
num = int(input("Inserir número: "))
print(num)

# Exercício 2: Ler um número real e imprimir.
num = float(input("Inserir número: "))
print(num)


# Exercício 3: Ler 3 números inteiros e imprimir a soma.
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))
res = num1 + num2 + num3
print(res)

# Exercício 4: Ler um número real e retornar o quadrado desse número.
num = float(input("Inserir número: "))
print(num ** 2)

# Exercício 5: Ler um número real e retornar a quinta parte desse número.
num = float(input("Inserir número: "))
print(num / 5)

# Exercício 6: Inserir um valor em Celsius e retornar o valor em Farenheit.
tempCelcius = float(input("Inserir temperatura em Celsius: "))
tempFarenheit = tempCelcius * (9 / 5) + 32
print(str(tempFarenheit) + "°F")

# Exercício 7: Inserir um valor em Farenheit e retornar o valor em Celsius.
tempFarenheit = float(input("Inserir temperatura em Farenheit: "))
tempCelcius = (tempFarenheit - 32) * 5 / 9
print(str(tempCelcius) + "°C")

# Exercício 8: Inserir um valor em Kelvin e retornar o valor em Celsius.
tempKelvin = float(input("Inserir temperatura em Kelvin: "))
tempCelcius = round(tempKelvin - 273.15, 2)
print(str(tempCelcius) + "°C")

# Exercício 9 : Inserir um valor em Celsius e retornar o valor em Kelvin.
tempCelcius = float(input("Inserir temperatura em Celsius: "))
tempKelvin = round(tempCelcius + 273.15, 2)
print(str(tempKelvin) + "K")

# Exercício 10: Converter velocidade de km/h para m/s
velKmh = float(input("Inserir velocidade em km/h: "))
velMs = round(velKmh / 3.6, 2)
print(str(velMs) + " m/s")

# Exercício 11: Converter velocidade de m/s para km/h
velMs = float(input("Inserir velocidade m/s: "))
velKmh = round(velMs * 3.6, 2)
print(str(velKmh) + " km/h")

# Exercício 12: Conversão de milhas para quilômetros.
distMil = float(input("Distância em milhas: "))
distKm = round(distMil * 1.61, 2)
print(str(distKm) + " km")

# Exercício 13: Conversão de quilômetros para milhas.
distKm = float(input("Distância em quilômetros: "))
distMil = round(distKm / 1.61, 2)
print(str(distMil) + " milhas")

# Exercício 14: Conversão de graus para radianos.
deg = float(input("Ângulo em graus: "))
rad = round(deg * 3.14 / 180, 2)
print(str(rad) + " radianos")

# Exercício 15: Conversão de radianos para graus.
rad = float(input("Ângulo em radianos: "))
deg = round(rad * 180 / 3.14, 2)
print(str(deg) + " graus")

# Exercício 16: Conversão de polegadas em centímetros.
pol = float(input("Tamanho em polegadas: "))
cm = round(pol * 2.54, 2)
print(str(cm) + " cm")

# Exercício 17: Conversão de centímetros em polegadas.
cm = float(input("Tamanho em centímetros: "))
pol = round(cm / 2.54, 2)
print(str(pol) + " pol")

# Exercício 18: Conversão de metros cúbicos em litros.
m3 = float(input("Volume em m³: "))
lts = round(m3 * 1_000, 2)
print(str(lts) + " l")

# Exercício 19: Conversão de litros em metros cúbicos.
lts = float(input("Volume em litros: "))
m3 = round(lts / 1_000, 2)
print(str(m3) + " m³")

# Exercício 20: Conversão de quilos em libras.
kg = float(input("Massa em quilogramas: "))
lb = round(kg / 0.45, 2)
print(str(lb) + " lb")

# Exercício 21: Conversão de libras em quilos.
lb = float(input("Massa em libras: "))
kg = round(lb * 0.45, 2)
print(str(kg) + " kg")

# Exercício 22: Conversão de jardas em metros.
yd = float(input("Distância em jardas: "))
m = round(yd * 0.91, 2)
print(str(m) + " m")

# Exercício 23: Conversão de metros em jardas.
m = float(input("Distância em jardas: "))
yd = round(m / 0.91, 2)
print(str(yd) + " yd")

# Exercício 24: Conversão de m² para acres.
m2 = float(input("Área em m²: "))
ac = round(m2 * 0.000_247)
print(str(ac) + " ac")

# Exercício 25: Conversão de acres para m².
ac = float(input("Área em acres: "))
m2 = round(ac * 4048.58, 2)
print(str(m2) + " m²")

# Exercício 26: Conversão de m² para hectares.
m2 = float(input("Área em m²: "))
hm2 = round(m2 * 0.000_1)
print(str(hm2) + " hm²")

# Exercício 27: Conversão de hectares para m².
hm2 = float(input("Área em hm²: "))
m2 = round(hm2 * 10_000, 2)
print(str(m2) + " m²")

# Exercício 28: Ler três valores e imprimir a soma do quadrado deles.
num1 = float(input("Valor 1: "))
num2 = float(input("Valor 2: "))
num3 = float(input("Valor 3: "))
print(round(num1 ** 2 + num2 ** 2 + num3 ** 2, 2))

# Exercício 29: Ler 4 notas e imprimir a média aritimética delas.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(round(media, 2))

# Exercício 30: Conversão de real em dólar.
real = float(input("Valor em reais: "))
dolar = round(real / 4.00, 2)
print(str(dolar) + " US$")

# Exercício 31: Ler um inteiro e imprimir os números anterior e posterior.
num = int(input("Digitar inteiro: "))
print(str(num) + " está entre " + str(num - 1) + " e " + str(num + 1) + ".")

# Exercício 32: Ler um inteiro e somar o sucessor do triplo com o antecessor do dobro.
num = int(input("Inserir inteiro: "))
soma = (3 * num + 1 + 2 * num - 1)
print(soma)

# Exercício 33: Recebe o lado do quadrado e imprime a área.
lado = float(input("Lado do quadrado: "))
print(round(lado ** 2, 4))

# Exercício 34: Área do círculo.
raio = float(input("Valor do raio: "))
area = (raio ** 2) * 3.141592
print(area)

# Exercício 35: Teorema de Pitágoras.
cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))
hipotenusa = round((cateto1 ** 2 + cateto2 ** 2) ** (1 / int(2)), 2)
print(hipotenusa)

# Exercício 36: Volume do cilindro.]
raio = float(input("Raio da base: "))
altura = float(input("Altura do cilindro: "))
volume = 3.141_592 * raio ** 2 * altura
print(volume)

# Exercício 37: Imprimir valor com desconto de 12%.
valor = float(input("Preço do produto: "))
preco = round(valor * (1 - 0.12), 2)
print(str(preco) + " R$")

# Exercício 38: Imprimir salário com aumento de 25%.
valor = float(input("Salário: "))
salario = round(valor * (1 + 0.25), 2)
print(str(salario) + " R$")

# Exercício 39: Dividir um prêmio entre três pessoas nas seguintes proporções: 46%, 32% e 22%
premio1 = round(780_000.00 * 0.46, 2)
premio2 = round(780_000.00 * 0.32, 2)
premio3 = round(780_000.00 * 0.22, 2)
texto = f"Primeiro prêmio: {premio1} R$\nSegundo prêmio: {premio2} R$\nTerceiro prêmio: {premio3} R$"
print(texto)

# Exercício 40: Calcular salário de um trabalhador, recebendo o número de dias trabalhados menos 8% para o IR.
dias = int(input("Número de dias trabalhados: "))
salario = round(dias * 30 * 0.92, 2)
print(str(salario) + " R$")

# Exercício 41: Inserir o valor da hora trabalhada, o número de dias trabalhados e um acréscimo de 10%.
valor = float(input("Valor da hora trabalhada: "))
horas = float(input("Número de horas trabalhadas: "))
salario = round(valor * horas * 1.1, 2)
print(str(salario) + " R$")

# Exercício 42: Inserir o valor do salário com gratificação de 5% e 7% de imposto.
salario = float(input("Salário: "))
print(str(round(salario * 1.05 * 0.93, 2)) + " R$")

# Exercício 43: A partir de um valor inserido, exibir o valor com 10% de desconto, parcelas em 3x e comissão de 5%
valor = float(input("Preço do produto: "))
desconto = round(valor * 0.95, 2)
parcelas = round(valor / 3, 2)
comissaoVista = round(desconto * 0.05, 2)
comissaoPrazo = round(valor * 0.05, 2)
precos = f"À vista, o valor será de R$ {valor}  \n" \
         f"Parcelado, custará 3x de R$ {parcelas} \n" \
         f"O vendedor terá uma comissão de R$ {comissaoVista} no preço à vista." \
         f"O vendedor terá uma comissão de R$ {comissaoPrazo} no preço a prazo."
print(precos)

# Exercício 44: Inserir altura do degrau de uma escada e a altura a ser atingida. Imprimir o número de degraus.
alturaDegrau = float(input("Altura do degrau: "))
alturaAtingida = float(input("Altura a ser atingida: "))
numeroDegraus = round(alturaAtingida / alturaDegrau)
print("Serão necessários " + str(numeroDegraus) + " degraus.")

# Exercício 45: Converter letra maiúscula em minúscula.
letra = input("Insira a letra: ")
print(letra.upper())

# Exercício 46: Inverter dígitos de um número inteiro positivo.
num = str(int(input("Insira o número inteiro: ")).__abs__())
print(num[:: -1])

# Exercício 47: Ler um inteiro positivo de 4 dígitos (1000 a 9999) e imprimir um dígito por linha.
num = str(int(input("Insira o número inteiro de 4 dígitos: ")).__abs__())
print(num[0])
print(num[1])
print(num[2])
print(num[3])

# Exercício 48: Converter um número inteiro em horas minutos e segundos.
tempo = int(input("Inserir valor em segundos: "))
segundos = tempo % 60
minutos = tempo // 60 % 60
horas = tempo // 3600
print(f"{horas} h : {minutos} min : {segundos} s")

# Exercício 49: Ler o horário inicial e o tempo de duração de uma atividade. Imprimir o horário de término.
hora_inicio = int(input("Hora de início: "))
minuto_inicio = int(input("Minuto de início: "))
segundo_inicio = int(input("Segundo de início: "))
horas_duracao = int(input("Horas de duração: "))
minutos_duracao = int(input("Minutos de duração: "))
segundos_duracao = int(input("Segundos de duração: "))
horario_final = (hora_inicio + horas_duracao) * 3_600 + (minuto_inicio + minutos_duracao) * 60 + (segundo_inicio +
                                                                                                  segundos_duracao)
segundo_final = horario_final % 60
minuto_final = horario_final // 60 % 60
hora_final = horario_final // 3_600
print(f"{hora_final} h : {minuto_final} min : {segundo_final} s")

# Exercício 50: Calcular o ano de nascimento do usuário a partir da idade e do ano atual.
idade = int(input("Sua idade: "))
ano_atual = int(input("Ano atual: "))

ano_nascimento = ano_atual - idade
print(str(f"Você nasceu em {ano_nascimento}."))

# Exercício 51: Inserir valores de coordenada x e y de um ponto e retornar a distância deste ponto à origem (0, 0).
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))

distancia = round((x ** 2 + y ** 2) ** (1 / int(2)), 4)
print(distancia)

# Exercício 52: Dividir um prêmio entre três pessoas proporcionalmente ao investimento de cada um.
jogador_1 = float(input("Investimento do jogador 1: "))
jogador_2 = float(input("Investimento do jogador 2: "))
jogador_3 = float(input("Investimento do jogador 3: "))
premio = float(input("Prêmio do sorteio: "))

total_investido = jogador_1 + jogador_2 + jogador_3

premio_1 = round(premio * jogador_1 / total_investido, 2)
premio_2 = round(premio * jogador_2 / total_investido, 2)
premio_3 = round(premio * jogador_3 / total_investido, 2)

mensagem = f"Dos R$ {premio} de prêmio:\n" \
           f"O jogador 1 receberá R$ {premio_1}\n" \
           f"O jogador 2 receberá R$ {premio_2}\n" \
           f"O jogador 3 receberá R$ {premio_3}\n"

print(mensagem)

# Exercício 53: Ler comprimento e largura de um terreno e preço de tela por metro. Imprimir o custo para cercar.
largura = float(input("Largura do terreno: "))
comprimento = float(input("Comprimento do terreno: "))
preco = float(input("Preço da tela por metro: "))

custo = round(2 * (largura + comprimento) * preco, 2)
print(f"O custo para cercar o terreno será de R$ {custo}")
