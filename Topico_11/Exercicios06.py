import binascii
import os
from random import randint
# """
# Exercício 1: Criar um programa que:
# item a: permita criar e abrir um arquivo:
# item b: permita a gravação de caracteres nesse arquivo, encerrando a gravação ao digitar '0'.
# item c: fechar o arquivo
# Em seguida, ler o arquivo caractere por caractere.
# """
#
# with open("Arquivos_Exercicios/arq.txt", 'w') as arq:
#     while True:
#         texto = input("Digite o texto:\n")
#
#         if texto != '0':
#             arq.write(texto + "\n")
#         else:
#             break
#
# arq = open("Arquivos_Exercicios/arq.txt")
# arq.seek(0)
# print(arq.read())
# arq.close()
#
# # Exercício 2: Contar o número de linhas de um arquivo de texto.
# with open("Arquivos_Exercicios/arq.txt") as arq:
#     linhas = arq.readlines()
#     print(len(linhas))
#
# # Exercício 3: Ler um arquivo de texto e contar as vogais.
# with open("Arquivos_Exercicios/arq.txt") as arq:
#     texto = arq.read()
#     vogais = 0
#
#     for letra in texto.lower():
#         if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#             vogais += 1
#
#     print(f"Há {vogais} vogais no texto.")
#
# # Exercício 4: Contar as vogais e consoantes de um arquivo de texto.
# with open("Arquivos_Exercicios/arq.txt", 'r') as arq:
#     texto = arq.read()
#     vogais, consoantes = 0, 0
#
#     for letra in texto.lower():
#         if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#             vogais += 1
#         else:
#             consoantes += 1
#
#     print(f"Há {vogais} vogais e {consoantes} consoantes no texto.")
#
# # Exercício 5: Receber um arquivo de texto e um caractere. Retornar quantas vezes o caractere ocorre no texto.
# arquivo = "Arquivos_Exercicios/arq.txt"
# caractere = 'z'
#
#
# def conta_caractere(_arquivo, _caractere):
#     _cont = 0
#
#     with open(_arquivo, 'r') as _arq:
#         _texto = _arq.read()
#         for _letra in _texto:
#             if _letra.lower() == _caractere.lower():
#                 _cont += 1
#     return _cont
#
#
# cont = conta_caractere(arquivo, caractere)
# print(f"O caractere {caractere} se repete {cont} vezes.")
#
# # Exercício 6: Receber um arquivo de texto e retornar quantas vezes cada letra do alfabeto aparece.
# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
#             'v', 'w', 'x', 'y', 'z']
# arquivo = "Arquivos_Exercicios/arq.txt"
#
#
# def conta_alfabeto(_arquivo):
#     _alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                  'u', 'v', 'w', 'x', 'y', 'z']
#
#     with open(_arquivo, 'r') as _arq:
#         _texto = _arq.read()
#
#         for _letra in _alfabeto:
#             _cont = 0
#
#             for _caractere in _texto.lower():
#                 if _letra == _caractere:
#                     _cont += 1
#
#             print(f"A letra {_letra} aparece {_cont} vezes no texto {_arq.name}")
#
#
# conta_alfabeto(arquivo)
#
# # Exercício 7: Receber um arquivo de texto e criar um novo com as vogais substituídas por *:
# arquivo = "Arquivos_Exercicios/arq.txt"
# novo_caractere = '*'
#
#
# def troca_vogais(_arquivo, _caractere):
#     with open(_arquivo, 'r') as _arq:
#         _texto = _arq.read()
#         _vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         _novo = ''
#
#         for _letra in _texto:
#             if _letra in _vogais:
#                 _novo += _caractere
#             else:
#                 _novo += _letra
#
#     with open("Arquivos_Exercicios/novo.txt", 'w') as _arq:
#         _arq.write(_novo)
#
#
# troca_vogais(arquivo, novo_caractere)
#
# """
# Exercício 8: receber um arquivo e criar um novo.
# As letras minúsculas devem ser convertidas para maiúsculas
# e gravadas em um novo arquivo. Esse arquivo deve ser nomeado
# pelo usuário via teclado.
# """
# arquivo = "frutas.txt"
#
# with open(arquivo, 'r') as arq:
#     texto = arq.read()
#     nome_arquivo = input("Digite o nome do novo arquivo:\n") + '.txt'
#
#     with open(os.path.join("Arquivos_Exercicios", nome_arquivo), 'w') as novo:
#         novo.write(texto.upper())
#
# # Exercício 9: Receber dois arquivos de usuário e criar um terceiro com o conteúdo dos outros dois.
# arquivo1 = "Arquivos_Exercicios/FRUTAS.txt"
# arquivo2 = "Arquivos_Exercicios/arq.txt"
#
#
# def combina_arquivos(_arquivo1, _arquivo2):
#     _texto = ''
#     with open(_arquivo1, 'r') as _arq1:
#         _texto += _arq1.read()
#     with open(_arquivo2, 'r') as _arq2:
#         _texto += _arq2.read()
#     with open("Arquivos_Exercicios/Combina.txt", 'w') as _arq3:
#         _arq3.write(_texto)
#
#
# combina_arquivos(arquivo1, arquivo2)
#
# """
# Exercício 10: Receber um nome de arquivo de entrada e outro de saída.
# O arquivo de entrada deve ter, por linha, o nome de uma cidade e sua população.
# O arquivo de saída deve apresentar a cidade mais populosa e seu número de habitantes.
# """
# cidades = [("São Paulo", 12_106_920), ("Moscou", 12_380_664), ("Tóquio", 9_071_577), ("Nova Iorque", 8_405_837),
#            ("Xangai", 17_836_133), ("Londres", 8_308_369), ("Cairo", 8_922_949)]
#
# with open("Arquivos_Exercicios/Cidades.txt", 'w') as arq:
#     for cidade in cidades:
#         arq.write(f"Cidade: {cidade[0]}, População: {cidade[1]}\n")
#
# arquivo1 = "Arquivos_Exercicios/Cidades.txt"
# arquivo2 = "Arquivos_Exercicios/Maior população.txt"
#
#
# def compara_valores(_arquivo1, _arquivo2=None):
#     _pops = []  # Valores de população
#     _maior_indice = None  # Posição na lista do maior valor
#
#     # Abrindo o arquivo:
#     with open(_arquivo1, 'r') as _arq:
#         for _linha in _arq.readlines():  # Lendo cada linha
#             _rev = reversed(_linha)  # Facilita a leitura dos números
#             _char = ''
#
#             for _c in _rev:
#                 if _c != ' ':  # Para de varrer o iterável ao encontrar o primeiro espaço em branco.
#                     _char += _c  # Cria uma lista de caracteres, os quais são os algarismos dos valores procurados.
#                 else:
#                     _char = list(reversed(_char))  # Traz os algarismos de volta à ordem original.
#                     _char.pop()  # Remove o caractere \n
#                     _pop = ''  # Os algarismos serão armazenados como um string único aqui.
#
#                     for _n in _char:
#                         _pop += _n  # Armazenando algarismos na string.
#
#                     _pop = int(_pop)  # Convertendo o texto para inteiro.
#                     _pops.append(_pop)  # Carregando os valores de população na lista
#                     _maior_indice = _pops.index(max(_pops))  # Encontrando o índice do maior valor.
#                     print(_maior_indice)
#                     break
#
#     with open(_arquivo2, 'w') as _arq2:
#         with open(_arquivo1, 'r') as _arq1:
#             _arq2.write(_arq1.readlines()[_maior_indice])
#
#
# compara_valores(arquivo1, arquivo2)
#
# # Exercício 11: Receber o nome do arquio e uma palavra. Retornar o número de vezes que a palavra aparece no arquivo.
# arquivo = "Arquivos_Exercicios/Texto.txt"
# palavra = "fighter"
#
#
# def encontra_palavra(_arquivo, _palavra):
#     with open(_arquivo, 'r') as _arq:
#         _texto = _arq.read().split(" ")
#         return _texto.count(_palavra.lower())
#
#
# print(f"A palavra \"{palavra}\" foi encontrada no arquivo {arquivo} {encontra_palavra(arquivo, palavra)} vezes.")
#
# """
# Exercício 12: Abrir um arquivo, contar e escrever o número de caracteres, linhas e palavras.
# Escrever também quantas vezes cada letra ocorre, exceto letras com acento.
# """
# arquivo = "Arquivos_Exercicios/Texto.txt"
# letras, linhas, palavras = 0, 0, 0
# mensagem1, mensagem2, texto = '', '', ''
#
# with open(arquivo, 'r+') as arq:
#     texto = '\n' + arq.read()
#
#     alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                 'v', 'w', 'x', 'y', 'z']
#
#     for letra in texto:
#         if letra != ' ' or letra != '\n':
#             letras += 1
#
#     linhas = len(texto.split('\n'))
#
#     palavras = len(texto.split(' '))
#
#     mensagem1 = f"O texto {arq.name} tem {letras} letras, {linhas} linhas e {palavras} palavras."
#     print(mensagem1)
#
#     for letra in alfabeto:
#         cont = 0
#
#         for char in texto:
#             if char == letra:
#                 cont += 1
#
#         mensagem = f"A letra {letra} aparece {cont} vezes no texto {arq.name}"
#         print(mensagem)
#         mensagem2 += mensagem + '\n'
#
#     texto += '\n' + mensagem1 + '\n' + mensagem2
#
# with open(arquivo, 'w') as arq:
#     arq.write(texto)
#
# """
# Exercício 13: Criar um programa que o usuário possa registrar nomes e números de telefone.
# O programa deve encerrar caso o usuário entre com 0 como número de telefone.
# """
# with open("Arquivos_Exercicios/Registros.txt", 'w') as regs:
#     while True:
#         nome = input("Digite o nome:\n")
#         telefone = input("Digite o número de telefone (Digite 0 para encerrar):\n")
#
#         if telefone != '0':
#             registro = "nome: " + nome + "\ttelefone: " + telefone + '\n'
#             regs.write(registro)
#         else:
#             break
#
# """
# Exercício 14: Ler um arquivo com datas de nascimento e, a partir da data atual,
# calcular as idades no registro e escrever esse valor em outro arquivo.
# """
# data_atual = [24, 2, 2020]
# nascimentos = None
#
# with open("Arquivos_Exercicios/Nascimentos.txt") as nasc:
#     texto = nasc.read()
#     nascimentos = texto.split('\n')
#
#
# def calcula_idade(_nascimentos, _data_atual):
#     _idades = []
#     for nascimento in nascimentos:
#         _data = nascimento.split('/')
#         _dia = int(_data[0])
#         _mes = int(_data[1])
#         _ano = int(_data[2])
#
#         _dias = _data_atual[0] - _dia
#         _meses = _data_atual[1] - _mes
#         _anos = _data_atual[2] - _ano
#
#         if _dias < 0:
#             _dias += 30
#             _meses -= 1
#
#         if _meses < 0:
#             _meses += 12
#             _anos -= 1
#
#         _idade = f"{_anos} anos, {_meses} meses e {_dias} dias.\n"
#         _idades.append(_idade)
#
#     return _idades
#
#
# with open("Arquivos_Exercicios/Idades.txt", 'w') as idades:
#     for idade in calcula_idade(nascimentos, data_atual):
#         idades.write(idade)
#
# """
# Exercício 15: Receber o ano atual e dois nomes de arquivos. Um desses arquivos deve ter
# nomes (no máximo 40 caracteres) e anos de nascimento. O outro arquivo deverá
# ser gerado na saída do programa, apresentando a idade da pessoa e se:
#  - ela é menor de idade (idade < 18)
#  - ela está entrando na maioridade (idade = 18)
#  - ela é maior de idade (idade > 18)
# """
# ano_atual = 2020
# arquivo = "Arquivos_Exercicios/Pessoas.txt"
#
#
# def carrega_dados(_arquivo):
#     with open(_arquivo, 'r') as _arq:
#         _dados = _arq.read().split('\n')
#
#         return _dados
#
#
# def calcula_idades(_atual, _dados):
#     _idades = []
#     _anos = [_dado for _dado in _dados if _dados.index(_dado) % 5 == 3]
#
#     for _ano in _anos:
#         _idades.append(_atual - int(_ano))
#
#     return _idades
#
#
# def encontra_nomes(_arquivo):
#     with open(_arquivo, 'r') as _arq:
#         _dados = _arq.read().split('\n')
#         _nomes = [_dado for _dado in _dados if _dados.index(_dado) % 5 == 1]
#
#         return _nomes
#
#
# def gera_arquivo(_ano_atual, _arquivo_entrada, _nome_saida):
#     _dados = carrega_dados(_arquivo_entrada)
#     _idades = calcula_idades(_ano_atual, _dados)
#     _nomes = encontra_nomes(_arquivo_entrada)
#
#     with open(_nome_saida, 'w') as _arq:
#         for _i in range(len(_nomes)):
#             _arq.write(f"Nome: {_nomes[_i]}\tIdade: {_idades[_i]}.\n")
#
#
# gera_arquivo(ano_atual, arquivo, "Arquivos_Exercicios/Nomes e Idades")
#
# # Exercício 16: Receber um vetor de 10 valores, converter para binário e gravar os resultados num arquivo.
# vetor = []
#
# while len(vetor) < 10:
#     rnd = randint(0, 20)
#     vetor.append(rnd)
#
# with open("Arquivos_Exercicios/Dec2Bin.txt", 'w') as arq:
#     resto = 0
#
#     for decimal in vetor:
#         binario = ''
#         aux = decimal
#
#         while aux > 1:
#             resto = aux % 2
#             aux //= 2
#             binario += str(resto)
#
#         binario += str(aux)
#         binario = binario[::-1] + '\n'
#         texto = f"{decimal} = {binario}"
#         arq.write(texto)
#
# """
# Exercício 17: Ler um arquivo que contenha as dimensões de uma matriz, o número de posições a serem anuladas
# e quais serão as posições anuladas. Essas posições devem receber o valor 0 e as restantes, 1.
# """
# arquivo = "Arquivos_Exercicios/Dimensões.txt"
#
#
# def le_arquivo(_arquivo):
#     with open(_arquivo) as _arq:
#         _dados = _arq.read().split('\n')
#
#         return _dados
#
#
# def gera_matriz(_dados):
#     _matriz = []
#     _dimensoes = _dados[1].split(' ')
#     _linhas = int(_dimensoes[0])
#     _colunas = int(_dimensoes[1])
#
#     for _i in range(_linhas):
#         _matriz.append([])
#
#         for _j in range(_colunas):
#             _matriz[_i].append(1)
#
#     return _matriz
#
#
# def anula_posicoes(_dados, _matriz):
#     for i in range(3):
#         _dados.pop(0)
#
#     for _d in _dados:
#         _dado = _d.split(' ')
#
#         _linha = int(_dado[0])
#         _coluna = int(_dado[1])
#
#         _matriz[_linha][_coluna] = 0
#
#     return matriz
#
#
# def grava_matriz(_matriz):
#     _linha = []
#     with open("Arquivos_Exercicios/Matriz.txt", 'w') as _arq:
#         for _linha in _matriz:
#             for _numero in _linha:
#                 _numero = str(_numero) + ' '
#                 _arq.write(_numero)
#             _arq.write('\n')
#
#
# dados = le_arquivo(arquivo)
# matriz = gera_matriz(dados)
# matriz = anula_posicoes(dados, matriz)
# grava_matriz(matriz)
#
# # Exercício 18: Ler uma arquivo que contenha uma lista de produtos e seus preços e calcular o valor da compra.
# arquivo = "Arquivos_Exercicios/Compras.txt"
#
#
# def captura_dados(_arquivo):
#     with open(_arquivo, 'r') as _arq:
#         _dados = _arq.read().split('\n')
#
#         return _dados
#
#
# def calcula_valor(_dados):
#     _temp = [float(_dado) * 100 for _dado in _dados if _dados.index(_dado) % 5 == 3]  # * 100 é para arredondar
#
#     return sum(_temp) / 100
#
#
# dados = captura_dados(arquivo)
# print(calcula_valor(dados))
#
# """
# Exercício 19: Receber de um usuário um arquivo contendo nomes de alunos e suas notas.
# Cada linha deve ter nome e nota, e o programa deve encontrar e imprimir a maior delas.
# """
# arquivo = "Arquivos_Exercicios/Notas.txt"
#
#
# def captura_dados(_arquivo):
#     with open(_arquivo, 'r') as _arq:
#         _dados = _arq.read().split('\n')
#
#         return _dados
#
#
# def le_notas(_dados):
#     _notas = []
#     for _dado in _dados:
#         _nota = ''
#
#         for _char in _dado[::-1]:
#             if _char != ' ':
#                 _nota += _char
#             else:
#                 _notas.append(float(_nota[::-1]))
#                 break
#
#     return _notas
#
#
# def encontra_maior(_arquivo, _notas):
#     _maior_nota = max(_notas)
#     _indice_nota = _notas.index(_maior_nota)
#
#     with open(_arquivo, 'r') as _arq:
#         _dados = _arq.read().split('\n')
#
#         return _dados[_indice_nota]
#
#
# dados = captura_dados(arquivo)
# notas = le_notas(dados)
# print(encontra_maior(arquivo, notas))
#
# """
# Exercício 20: Receber um número que representa o total de alunos duma disciplina.
# Armazenar em dois vetores os nomes desses alunos e suas notas finais.
# Os nomes dos alunos devem ter, no máximo, 40 caracteres. Caso não cheguem a 40,
# completar com espaços em branco. Escrever num arquivo os nomes e notas desses alunos.
# """
# numero_alunos = 5
#
#
# def registra_nomes(_numero_alunos):
#     _nomes = []
#
#     for _i in range(_numero_alunos):
#         _nome = input("Nome do aluno:\n")
#
#         if len(_nome) < 40:
#             _nome += ' ' * (40 - len(_nome))
#         elif len(_nome) > 40:
#             _nome += '\b' * (len(_nome) - 40)
#
#         print(_nome)
#
#         _nomes.append(_nome)
#
#     return _nomes
#
#
# def registra_notas(_numero_alunos):
#     _notas = []
#
#     for _i in range(_numero_alunos):
#         _nota = float(input("Nota do aluno:\n"))
#         _notas.append(_nota)
#
#     return _notas
#
#
# def escreve_arquivo(_nomes, _notas, _numero_alunos):
#     with open("Arquivos_Exercicios/Notas Finais.txt", 'w') as _arq:
#
#         for _aluno in range(numero_alunos):
#             _finais = f"Nome: {_nomes[_aluno]} Nota: {_notas[_aluno]}\n"
#             _arq.write(_finais)
#
#
# # nomes = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
# #          "Aline Souza Pires", "Caio de Andrade e Lima Silva"]
# # notas = [2.0, 6.4, 9.1, 8.7, 10.0]  # Listas usadas para teste de gravação.
#
# nomes = registra_nomes(numero_alunos)
# notas = registra_notas(numero_alunos)
# escreve_arquivo(nomes, notas, numero_alunos)
#
# """
# Exerrcício 21: Rceber o número de alunos de uma disciplina, digitar seus nomes
# (40 caracteres max) e suas notas. Salvar os dados num arquivo binário e imprimir
# o aluno com a maior nota.
# """
# numero_alunos = 5
#
#
# def registra_nomes(_numero_alunos):
#     _nomes = []
#
#     for _i in range(_numero_alunos):
#         _nome = input("Nome do aluno:\n")
#
#         if len(_nome) < 40:
#             _nome += ' ' * (40 - len(_nome))
#         elif len(_nome) > 40:
#             _nome += '\b' * (len(_nome) - 40)
#
#         print(_nome)
#
#         _nomes.append(_nome)
#
#     return _nomes
#
#
# def registra_notas(_numero_alunos):
#     _notas = []
#
#     for _i in range(_numero_alunos):
#         _nota = float(input("Nota do aluno:\n"))
#         _notas.append(_nota)
#
#     return _notas
#
#
# def escreve_arquivo(_nomes, _notas, _numero_alunos):
#     with open("Arquivos_Exercicios/Notas_Binário.bin", 'wb') as _arq:
#
#         for _aluno in range(numero_alunos):
#             _finais = f"Nome: {_nomes[_aluno]} Nota: {_notas[_aluno]}\n"
#             _arq.write(_finais.encode('utf-8'))
#
#     return _arq.name
#
#
# def encontra_maior(_arquivo, _notas):
#     _maior_nota = max(_notas)
#     _indice_nota = _notas.index(_maior_nota)
#
#     with open(_arquivo, 'rb') as _arq:
#         _dados = _arq.read().decode('utf-8').split('\n')
#
#         return _dados[_indice_nota]
#
#
# nomes = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
#          "Aline Souza Pires", "Caio de Andrade e Lima Silva"]
# notas = [2.0, 6.4, 9.1, 8.7, 10.0]  # Listas usadas para teste de gravação.
#
# arquivo = escreve_arquivo(nomes, notas, numero_alunos)
# print(encontra_maior(arquivo, notas))
#
"""
Exercício 22: Receber dois nomes de arquivos.
Um dos nomes é de um arquivo contendo o nome de um aluno e suas três notas.
O outro é um arquivo de saída com as notas em ordem crescente.
"""
arquivo = "Arquivos_Exercicios/Nota_Aluno.txt"


def captura_dados(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        return _dados


def ordena_notas(_dados):
    _notas = [_nota for _nota in _dados if (_dados.index(_nota) % 5 != 0 and _dados.index(_nota) % 5 != 4)]
    _notas.sort()

    with open("Arquivos_Exercicios/Notas_Ordenadas.txt", 'w') as _arq:
        _texto = f'{_dados[0]}:\n'
        for _nota in _notas:
            _texto += f"{_nota}\n"


dados = captura_dados(arquivo)
ordena_notas(dados)
