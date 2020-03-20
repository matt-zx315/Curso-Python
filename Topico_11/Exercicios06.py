import binascii
import colored
import os
from random import randint
"""
Exercício 1: Criar um programa que:
item a: permita criar e abrir um arquivo:
item b: permita a gravação de caracteres nesse arquivo, encerrando a gravação ao digitar '0'.
item c: fechar o arquivo
Em seguida, ler o arquivo caractere por caractere.
"""

with open("Arquivos_Exercicios/arq.txt", 'w') as arq:
    while True:
        texto = input("Digite o texto:\n")

        if texto != '0':
            arq.write(texto + "\n")
        else:
            break

arq = open("Arquivos_Exercicios/arq.txt")
arq.seek(0)
print(arq.read())
arq.close()

# Exercício 2: Contar o número de linhas de um arquivo de texto.
with open("Arquivos_Exercicios/arq.txt") as arq:
    linhas = arq.readlines()
    print(len(linhas))

# Exercício 3: Ler um arquivo de texto e contar as vogais.
with open("Arquivos_Exercicios/arq.txt") as arq:
    texto = arq.read()
    vogais = 0

    for letra in texto.lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1

    print(f"Há {vogais} vogais no texto.")

# Exercício 4: Contar as vogais e consoantes de um arquivo de texto.
with open("Arquivos_Exercicios/arq.txt", 'r') as arq:
    texto = arq.read()
    vogais, consoantes = 0, 0

    for letra in texto.lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1
        else:
            consoantes += 1

    print(f"Há {vogais} vogais e {consoantes} consoantes no texto.")

# Exercício 5: Receber um arquivo de texto e um caractere. Retornar quantas vezes o caractere ocorre no texto.
arquivo = "Arquivos_Exercicios/arq.txt"
caractere = 'z'


def conta_caractere(_arquivo, _caractere):
    _cont = 0

    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read()
        for _letra in _texto:
            if _letra.lower() == _caractere.lower():
                _cont += 1
    return _cont


cont = conta_caractere(arquivo, caractere)
print(f"O caractere {caractere} se repete {cont} vezes.")

# Exercício 6: Receber um arquivo de texto e retornar quantas vezes cada letra do alfabeto aparece.
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
            'v', 'w', 'x', 'y', 'z']
arquivo = "Arquivos_Exercicios/arq.txt"


def conta_alfabeto(_arquivo):
    _alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read()

        for _letra in _alfabeto:
            _cont = 0

            for _caractere in _texto.lower():
                if _letra == _caractere:
                    _cont += 1

            print(f"A letra {_letra} aparece {_cont} vezes no texto {_arq.name}")


conta_alfabeto(arquivo)

# Exercício 7: Receber um arquivo de texto e criar um novo com as vogais substituídas por *:
arquivo = "Arquivos_Exercicios/arq.txt"
novo_caractere = '*'


def troca_vogais(_arquivo, _caractere):
    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read()
        _vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        _novo = ''

        for _letra in _texto:
            if _letra in _vogais:
                _novo += _caractere
            else:
                _novo += _letra

    with open("Arquivos_Exercicios/novo.txt", 'w') as _arq:
        _arq.write(_novo)


troca_vogais(arquivo, novo_caractere)

"""
Exercício 8: receber um arquivo e criar um novo.
As letras minúsculas devem ser convertidas para maiúsculas
e gravadas em um novo arquivo. Esse arquivo deve ser nomeado
pelo usuário via teclado.
"""
arquivo = "frutas.txt"

with open(arquivo, 'r') as arq:
    texto = arq.read()
    nome_arquivo = input("Digite o nome do novo arquivo:\n") + '.txt'

    with open(os.path.join("Arquivos_Exercicios", nome_arquivo), 'w') as novo:
        novo.write(texto.upper())

# Exercício 9: Receber dois arquivos de usuário e criar um terceiro com o conteúdo dos outros dois.
arquivo1 = "Arquivos_Exercicios/FRUTAS.txt"
arquivo2 = "Arquivos_Exercicios/arq.txt"


def combina_arquivos(_arquivo1, _arquivo2):
    _texto = ''
    with open(_arquivo1, 'r') as _arq1:
        _texto += _arq1.read()
    with open(_arquivo2, 'r') as _arq2:
        _texto += _arq2.read()
    with open("Arquivos_Exercicios/Combina.txt", 'w') as _arq3:
        _arq3.write(_texto)


combina_arquivos(arquivo1, arquivo2)

"""
Exercício 10: Receber um nome de arquivo de entrada e outro de saída.
O arquivo de entrada deve ter, por linha, o nome de uma cidade e sua população.
O arquivo de saída deve apresentar a cidade mais populosa e seu número de habitantes.
"""
cidades = [("São Paulo", 12_106_920), ("Moscou", 12_380_664), ("Tóquio", 9_071_577), ("Nova Iorque", 8_405_837),
           ("Xangai", 17_836_133), ("Londres", 8_308_369), ("Cairo", 8_922_949)]

with open("Arquivos_Exercicios/Cidades.txt", 'w') as arq:
    for cidade in cidades:
        arq.write(f"Cidade: {cidade[0]}, População: {cidade[1]}\n")

arquivo1 = "Arquivos_Exercicios/Cidades.txt"
arquivo2 = "Arquivos_Exercicios/Maior população.txt"


def compara_valores(_arquivo1, _arquivo2=None):
    _pops = []  # Valores de população
    _maior_indice = None  # Posição na lista do maior valor

    # Abrindo o arquivo:
    with open(_arquivo1, 'r') as _arq:
        for _linha in _arq.readlines():  # Lendo cada linha
            _rev = reversed(_linha)  # Facilita a leitura dos números
            _char = ''

            for _c in _rev:
                if _c != ' ':  # Para de varrer o iterável ao encontrar o primeiro espaço em branco.
                    _char += _c  # Cria uma lista de caracteres, os quais são os algarismos dos valores procurados.
                else:
                    _char = list(reversed(_char))  # Traz os algarismos de volta à ordem original.
                    _char.pop()  # Remove o caractere \n
                    _pop = ''  # Os algarismos serão armazenados como um string único aqui.

                    for _n in _char:
                        _pop += _n  # Armazenando algarismos na string.

                    _pop = int(_pop)  # Convertendo o texto para inteiro.
                    _pops.append(_pop)  # Carregando os valores de população na lista
                    _maior_indice = _pops.index(max(_pops))  # Encontrando o índice do maior valor.
                    print(_maior_indice)
                    break

    with open(_arquivo2, 'w') as _arq2:
        with open(_arquivo1, 'r') as _arq1:
            _arq2.write(_arq1.readlines()[_maior_indice])


compara_valores(arquivo1, arquivo2)

# Exercício 11: Receber o nome do arquio e uma palavra. Retornar o número de vezes que a palavra aparece no arquivo.
arquivo = "Arquivos_Exercicios/Texto.txt"
palavra = "fighter"


def encontra_palavra(_arquivo, _palavra):
    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read().split(" ")
        return _texto.count(_palavra.lower())


print(f"A palavra \"{palavra}\" foi encontrada no arquivo {arquivo} {encontra_palavra(arquivo, palavra)} vezes.")

"""
Exercício 12: Abrir um arquivo, contar e escrever o número de caracteres, linhas e palavras.
Escrever também quantas vezes cada letra ocorre, exceto letras com acento.
"""
arquivo = "Arquivos_Exercicios/Texto.txt"
letras, linhas, palavras = 0, 0, 0
mensagem1, mensagem2, texto = '', '', ''

with open(arquivo, 'r+') as arq:
    texto = '\n' + arq.read()

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for letra in texto:
        if letra != ' ' or letra != '\n':
            letras += 1

    linhas = len(texto.split('\n'))

    palavras = len(texto.split(' '))

    mensagem1 = f"O texto {arq.name} tem {letras} letras, {linhas} linhas e {palavras} palavras."
    print(mensagem1)

    for letra in alfabeto:
        cont = 0

        for char in texto:
            if char == letra:
                cont += 1

        mensagem = f"A letra {letra} aparece {cont} vezes no texto {arq.name}"
        print(mensagem)
        mensagem2 += mensagem + '\n'

    texto += '\n' + mensagem1 + '\n' + mensagem2

with open(arquivo, 'w') as arq:
    arq.write(texto)

"""
Exercício 13: Criar um programa que o usuário possa registrar nomes e números de telefone.
O programa deve encerrar caso o usuário entre com 0 como número de telefone.
"""
with open("Arquivos_Exercicios/Registros.txt", 'w') as regs:
    while True:
        nome = input("Digite o nome:\n")
        telefone = input("Digite o número de telefone (Digite 0 para encerrar):\n")

        if telefone != '0':
            registro = "nome: " + nome + "\ttelefone: " + telefone + '\n'
            regs.write(registro)
        else:
            break

"""
Exercício 14: Ler um arquivo com datas de nascimento e, a partir da data atual,
calcular as idades no registro e escrever esse valor em outro arquivo.
"""
data_atual = [24, 2, 2020]
nascimentos = None

with open("Arquivos_Exercicios/Nascimentos.txt") as nasc:
    texto = nasc.read()
    nascimentos = texto.split('\n')


def calcula_idade(_nascimentos, _data_atual):
    _idades = []
    for nascimento in nascimentos:
        _data = nascimento.split('/')
        _dia = int(_data[0])
        _mes = int(_data[1])
        _ano = int(_data[2])

        _dias = _data_atual[0] - _dia
        _meses = _data_atual[1] - _mes
        _anos = _data_atual[2] - _ano

        if _dias < 0:
            _dias += 30
            _meses -= 1

        if _meses < 0:
            _meses += 12
            _anos -= 1

        _idade = f"{_anos} anos, {_meses} meses e {_dias} dias.\n"
        _idades.append(_idade)

    return _idades


with open("Arquivos_Exercicios/Idades.txt", 'w') as idades:
    for idade in calcula_idade(nascimentos, data_atual):
        idades.write(idade)

"""
Exercício 15: Receber o ano atual e dois nomes de arquivos. Um desses arquivos deve ter
nomes (no máximo 40 caracteres) e anos de nascimento. O outro arquivo deverá
ser gerado na saída do programa, apresentando a idade da pessoa e se:
 - ela é menor de idade (idade < 18)
 - ela está entrando na maioridade (idade = 18)
 - ela é maior de idade (idade > 18)
"""
ano_atual = 2020
arquivo = "Arquivos_Exercicios/Pessoas.txt"


def carrega_dados(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        return _dados


def calcula_idades(_atual, _dados):
    _idades = []
    _anos = [_dado for _dado in _dados if _dados.index(_dado) % 5 == 3]

    for _ano in _anos:
        _idades.append(_atual - int(_ano))

    return _idades


def encontra_nomes(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')
        _nomes = [_dado for _dado in _dados if _dados.index(_dado) % 5 == 1]

        return _nomes


def gera_arquivo(_ano_atual, _arquivo_entrada, _nome_saida):
    _dados = carrega_dados(_arquivo_entrada)
    _idades = calcula_idades(_ano_atual, _dados)
    _nomes = encontra_nomes(_arquivo_entrada)

    with open(_nome_saida, 'w') as _arq:
        for _i in range(len(_nomes)):
            _arq.write(f"Nome: {_nomes[_i]}\tIdade: {_idades[_i]}.\n")


gera_arquivo(ano_atual, arquivo, "Arquivos_Exercicios/Nomes e Idades")

# Exercício 16: Receber um vetor de 10 valores, converter para binário e gravar os resultados num arquivo.
vetor = []

while len(vetor) < 10:
    rnd = randint(0, 20)
    vetor.append(rnd)

with open("Arquivos_Exercicios/Dec2Bin.txt", 'w') as arq:
    resto = 0

    for decimal in vetor:
        binario = ''
        aux = decimal

        while aux > 1:
            resto = aux % 2
            aux //= 2
            binario += str(resto)

        binario += str(aux)
        binario = binario[::-1] + '\n'
        texto = f"{decimal} = {binario}"
        arq.write(texto)

"""
Exercício 17: Ler um arquivo que contenha as dimensões de uma matriz, o número de posições a serem anuladas
e quais serão as posições anuladas. Essas posições devem receber o valor 0 e as restantes, 1.
"""
arquivo = "Arquivos_Exercicios/Dimensões.txt"


def le_arquivo(_arquivo):
    with open(_arquivo) as _arq:
        _dados = _arq.read().split('\n')

        return _dados


def gera_matriz(_dados):
    _matriz = []
    _dimensoes = _dados[1].split(' ')
    _linhas = int(_dimensoes[0])
    _colunas = int(_dimensoes[1])

    for _i in range(_linhas):
        _matriz.append([])

        for _j in range(_colunas):
            _matriz[_i].append(1)

    return _matriz


def anula_posicoes(_dados, _matriz):
    for i in range(3):
        _dados.pop(0)

    for _d in _dados:
        _dado = _d.split(' ')

        _linha = int(_dado[0])
        _coluna = int(_dado[1])

        _matriz[_linha][_coluna] = 0

    return matriz


def grava_matriz(_matriz):
    _linha = []
    with open("Arquivos_Exercicios/Matriz.txt", 'w') as _arq:
        for _linha in _matriz:
            for _numero in _linha:
                _numero = str(_numero) + ' '
                _arq.write(_numero)
            _arq.write('\n')


dados = le_arquivo(arquivo)
matriz = gera_matriz(dados)
matriz = anula_posicoes(dados, matriz)
grava_matriz(matriz)

# Exercício 18: Ler uma arquivo que contenha uma lista de produtos e seus preços e calcular o valor da compra.
arquivo = "Arquivos_Exercicios/Compras.txt"


def captura_dados(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        return _dados


def calcula_valor(_dados):
    _temp = [float(_dado) * 100 for _dado in _dados if _dados.index(_dado) % 5 == 3]  # * 100 é para arredondar

    return sum(_temp) / 100


dados = captura_dados(arquivo)
print(calcula_valor(dados))

"""
Exercício 19: Receber de um usuário um arquivo contendo nomes de alunos e suas notas.
Cada linha deve ter nome e nota, e o programa deve encontrar e imprimir a maior delas.
"""
arquivo = "Arquivos_Exercicios/Notas.txt"


def captura_dados(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        return _dados


def le_notas(_dados):
    _notas = []
    for _dado in _dados:
        _nota = ''

        for _char in _dado[::-1]:
            if _char != ' ':
                _nota += _char
            else:
                _notas.append(float(_nota[::-1]))
                break

    return _notas


def encontra_maior(_arquivo, _notas):
    _maior_nota = max(_notas)
    _indice_nota = _notas.index(_maior_nota)

    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        return _dados[_indice_nota]


dados = captura_dados(arquivo)
notas = le_notas(dados)
print(encontra_maior(arquivo, notas))

"""
Exercício 20: Receber um número que representa o total de alunos duma disciplina.
Armazenar em dois vetores os nomes desses alunos e suas notas finais.
Os nomes dos alunos devem ter, no máximo, 40 caracteres. Caso não cheguem a 40,
completar com espaços em branco. Escrever num arquivo os nomes e notas desses alunos.
"""
numero_alunos = 5


def registra_nomes(_numero_alunos):
    _nomes = []

    for _i in range(_numero_alunos):
        _nome = input("Nome do aluno:\n")

        if len(_nome) < 40:
            _nome += ' ' * (40 - len(_nome))
        elif len(_nome) > 40:
            _nome += '\b' * (len(_nome) - 40)

        print(_nome)

        _nomes.append(_nome)

    return _nomes


def registra_notas(_numero_alunos):
    _notas = []

    for _i in range(_numero_alunos):
        _nota = float(input("Nota do aluno:\n"))
        _notas.append(_nota)

    return _notas


def escreve_arquivo(_nomes, _notas, _numero_alunos):
    with open("Arquivos_Exercicios/Notas Finais.txt", 'w') as _arq:

        for _aluno in range(numero_alunos):
            _finais = f"Nome: {_nomes[_aluno]} Nota: {_notas[_aluno]}\n"
            _arq.write(_finais)


# nomes = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
#          "Aline Souza Pires", "Caio de Andrade e Lima Silva"]
# notas = [2.0, 6.4, 9.1, 8.7, 10.0]  # Listas usadas para teste de gravação.

nomes = registra_nomes(numero_alunos)
notas = registra_notas(numero_alunos)
escreve_arquivo(nomes, notas, numero_alunos)

"""
Exerrcício 21: Rceber o número de alunos de uma disciplina, digitar seus nomes
(40 caracteres max) e suas notas. Salvar os dados num arquivo binário e imprimir
o aluno com a maior nota.
"""
numero_alunos = 5


def registra_nomes(_numero_alunos):
    _nomes = []

    for _i in range(_numero_alunos):
        _nome = input("Nome do aluno:\n")

        if len(_nome) < 40:
            _nome += ' ' * (40 - len(_nome))
        elif len(_nome) > 40:
            _nome += '\b' * (len(_nome) - 40)

        print(_nome)

        _nomes.append(_nome)

    return _nomes


def registra_notas(_numero_alunos):
    _notas = []

    for _i in range(_numero_alunos):
        _nota = float(input("Nota do aluno:\n"))
        _notas.append(_nota)

    return _notas


def escreve_arquivo(_nomes, _notas, _numero_alunos):
    with open("Arquivos_Exercicios/Notas_Binário.bin", 'wb') as _arq:

        for _aluno in range(numero_alunos):
            _finais = f"Nome: {_nomes[_aluno]} Nota: {_notas[_aluno]}\n"
            _arq.write(_finais.encode('utf-8'))

    return _arq.name


def encontra_maior(_arquivo, _notas):
    _maior_nota = max(_notas)
    _indice_nota = _notas.index(_maior_nota)

    with open(_arquivo, 'rb') as _arq:
        _dados = _arq.read().decode('utf-8').split('\n')

        return _dados[_indice_nota]


nomes = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
         "Aline Souza Pires", "Caio de Andrade e Lima Silva"]
notas = [2.0, 6.4, 9.1, 8.7, 10.0]  # Listas usadas para teste de gravação.

arquivo = escreve_arquivo(nomes, notas, numero_alunos)
print(encontra_maior(arquivo, notas))

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

"""
Ler a profissão e o tempo de serviço em anos de cada um dos
5 funcionários de uma empresa e armazenar os dados num arquivo
'emp.txt', sendo cada linha reservada para os dados de cada funcionário
"""
funcionarios = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
                "Aline Souza Pires", "Caio de Andrade e Lima Silva"]


def le_entrada(_funcionario):
    _texto = input("Funcionário: " + _funcionario + "\nProfissão: ")
    _dado = '\tProfissão ' + _texto
    _texto = input("Tempo de serviço: ")
    _dado += '\tTempo de serviço: ' + _texto

    return _dado


def registra_fucnionarios(_funcionarios):
    with open("Arquivos_Exercicios/emp.txt", 'w') as _emp:
        for _funcionario in _funcionarios:
            _registro = "Funcionário: " + _funcionario + le_entrada(_funcionario) + '\n'
            _emp.write(_registro)


registra_fucnionarios(funcionarios)

"""
Exercício 24: Implementar um sistema de despensa doméstica.
Cada produto deve ter um código numérico, descrição e quantidade.
Devem haver opções para entrada e retirada de produtos, bem como
um relatório geral e lista de itens não disponíveis. Armazenar em binário.
"""
erro = colored.fg(196)
existente = colored.fg(46)
alerta = colored.fg(226)


def cadastra_produtos(_produtos):
    _codigo_produto = int(input("Digite o código do produto:\n"))

    if _codigo_produto in _produtos.keys():
        print(colored.stylize("Produto já cadastrado!", existente))
        return _produtos

    _descricao = input("Descrição do produto:\n")
    _produtos[_codigo_produto] = {"descrição": _descricao, "quantidade": 0}
    print(_produtos)

    return _produtos


def entrada_produto(_produtos):
    _codigo_produto = int(input("Digite o código do produto:\n"))

    if _codigo_produto not in _produtos.keys():
        print(colored.stylize("PRODUTO NÃO ENCONTRADO!", erro))
        return _produtos

    _quantidade = int(input("Digite o número de unidades recebidas:\n"))
    _produtos[_codigo_produto]['quantidade'] += _quantidade

    return _produtos


def saida_produto(_produtos):
    _codigo_produto = int(input("Digite o código do produto:\n"))

    if _codigo_produto not in _produtos.keys():
        print(colored.stylize("PRODUTO NÃO ENCONTRADO!", erro))
        return _produtos

    _quantidade = int(input("Digite o número de unidades a retirar:\n"))

    if _produtos[_codigo_produto]['quantidade'] - _quantidade > 0:
        _produtos[_codigo_produto]['quantidade'] -= _quantidade
        return _produtos

    print(colored.stylize("QUANTIDADE INDISPONÍVEL!", erro))
    return _produtos


def gera_relatorio(_produtos):
    _relatorio = ''

    with open("Arquivos_Exercicios/relatório.bin", 'wb') as _prd:
        for _chave, _valor in _produtos.items():
            _relatorio += f"Código: {_chave}: {_valor}\n"

        _prd.write(_relatorio.encode('utf-8'))


def lista_indisponivel(_produtos):
    _indisponiveis = ''

    with open("Arquivos_Exercicios/Indisponíveis.bin", 'wb') as _ind:
        for _chave in _produtos:
            if _produtos[_chave]['quantidade'] == 0:
                _indisponiveis += f'{_chave}: {_produtos[_chave]}\n'

        _ind.write(_indisponiveis.encode('utf-8'))


def executar():
    produtos = {}

    while True:
        _mensagem = "Bem vindo ao sistema de gestão de produtos.\n" \
                    "Digite um dos comandos abaixo para começar:\n" \
                    "1-Cadastrar um novo produto.\n" \
                    "2-Dar entrada em um produto cadastrado.\n" \
                    "3-Retirar um produto cadastrado (se houver em quantidade suficiente).\n" \
                    "4-Gerar um relatório geral.\n" \
                    "5-Exibir a lista de produtos indisponíveis.\n" \
                    "0-sair.\n"

        _comando = int(input(_mensagem))

        if _comando == 1:
            produtos = cadastra_produtos(produtos)
        elif _comando == 2:
            produtos = entrada_produto(produtos)
        elif _comando == 3:
            produtos = saida_produto(produtos)
        elif _comando == 4:
            gera_relatorio(produtos)
        elif _comando == 5:
            print(lista_indisponivel(produtos))
        elif _comando == 0:
            break
        else:
            print(colored.stylize("Comando inválido. Insira um dos comandos a seguir:\n", alerta))


executar()

"""
Exercício 25: Gerenciar uma lista de contatos. cada contato deve ter:
nome, telefone e aniversário (dia/mês). O programa deve permitir:

- inserir contato
- remover contato
- pesquisar por nome
- listar todos os contatos
- listar contatos que iniciem por uma determinada letra
- imprimir os aniversariantes do mês
"""
contatos = {}
arquivo = "Arquivos_Exercicios/Contatos.txt"
niver = 'aniversário'
fone = 'telefone'

erro = colored.fg(196)
alerta = colored.fg(226)


def carrega_dados(_arquivo):
    global contatos

    with open(_arquivo, 'r') as _contatos:
        _dados = _contatos.read().split('\n')

        _nomes = [_nome for _nome in _dados if _dados.index(_nome) % 4 == 0]
        _fones = [_fone for _fone in _dados if _dados.index(_fone) % 4 == 1]
        _nivers = [_niver for _niver in _dados if _dados.index(_niver) % 4 == 2]

        for _indice in range(len(_dados) // 4):
            contatos[_nomes[_indice]] = {'telefone': _fones[_indice], 'aniversário': _nivers[_indice]}


def salvar_dados(_arquivo):
    global contatos

    _nomes = list(contatos.keys())
    _fones, _nivers = [], []

    for _contato in contatos:
        _fones.append(contatos[_contato]['telefone'])
        _nivers.append(contatos[_contato]['aniversário'])

    with open(_arquivo, 'w') as _contatos:
        for _indice in range(len(_nomes)):
            _contatos.write(f"{_nomes[_indice]}\n")
            _contatos.write(f"{_fones[_indice]}\n")
            _contatos.write(f"{_nivers[_indice]}\n")
            _contatos.write("\n")


def insere_contato(_telefone, _aniversario, _arquivo):
    global contatos

    _nome = input("Nome do contato:\n")
    _fone = input("Telefone:\n")
    _niver = input("Data de nascimento (dia/mês):\n")
    contatos[_nome] = {_telefone: _fone, _aniversario: _niver}

    salvar_dados(_arquivo)


def remover_contato(_arquivo):
    global contatos, erro, alerta

    _nome = input("Nome do contato:\n")

    if _nome in contatos:
        del contatos[_nome]
        salvar_dados(_arquivo)
    else:
        print(colored.stylize("USUÁRIO NÃO ENCONTRADO!!!", erro))


def pesquisa_nome():
    global contatos, alerta

    _nome = input("Nome completo do contato:\n")

    if _nome in contatos.keys():
        print(f"{_nome}: {contatos[_nome]}")
    else:
        print(colored.stylize(f"{_nome} não encontrado. Digite o nome completo.", alerta))


def listar_contatos(_contatos):
    with open("Arquivos_Exercicios/Contatos.txt", 'r') as _conts:
        print(_conts.read())


def busca_letra():
    global contatos, alerta

    _letra = input("Digite a inicial:\n")

    if len(_letra) > 1:
        print(colored.stylize("Entrada maior que uma letra. Tente novamente.", alerta))
    else:
        for _nome in contatos.keys():
            if _nome[0] == _letra:
                print(f"{_nome}: {contatos[_nome]}\n")


def busca_aniversariantes():
    global contatos

    _indice = None

    _mes = input("Digite o mês da busca (os dois dígitos!):\n")

    for _contato in contatos.values():
        _data = _contato['aniversário']
        _niver = _data.split('/')[1]
        _indice = list(contatos.values()).index(_contato)

        if _mes == _niver:
            print(f"{list(contatos.keys())[_indice]}")


def executar():
    _mensagem = "\nDigite um comando:\n" \
                "1 - Inserir novo contato\n" \
                "2 - Remover um contato existente\n" \
                "3 - Pesquisar um contato\n" \
                "4 - Exibir a lista de contatos\n" \
                "5 - Buscar por letra inicial\n" \
                "6 - Encontrar os aniversariantes do mês\n" \
                "0 - Sair\n"

    carrega_dados(arquivo)

    while True:
        _opcao = int(input(_mensagem))

        if _opcao == 0:
            print('Encerrando...')
            break
        elif _opcao == 1:
            insere_contato('telefone', 'aniversário', arquivo)
        elif _opcao == 2:
            remover_contato(arquivo)
        elif _opcao == 3:
            pesquisa_nome()
        elif _opcao == 4:
            listar_contatos(contatos)
        elif _opcao == 5:
            busca_letra()
        elif _opcao == 6:
            busca_aniversariantes()
        else:
            print(colored.stylize("\nOpção inválida. Escolha uma das opções a seguir:\n", alerta))


executar()

"""
Exercício 26: Criar um programa para cadastro de alunos.
O programa deve:

 - armazenar matrícula, sobrenome (apenas um) e ano de nascimento
 - ao iniciar o programa, o usuário deve informar o número de alunos que serão armazenados
 - o usuário deve entrar com as informações dos alunos
 - as informações devem ser armazenadas em um arquivo
"""


def carrega_dados(_arquivo):
    _alunos = {}

    with open(_arquivo, 'r') as _arq:
        _dados = _arq.read().split('\n')

        _matriculas = [_matricula for _matricula in _dados if _dados.index(_matricula) % 8 == 0]
        _nomes = [_nome for _nome in _dados if _dados.index(_nome) % 8 == 1]
        _sobrenomes = [_sobrenomes for _sobrenomes in _dados if _dados.index(_sobrenomes) % 8 == 2]
        _anos = [int(_ano) for _ano in _dados if _dados.index(_ano) % 8 == 3]
        _turmas = [_turma for _turma in _dados if _dados.index(_turma) % 8 == 4]
        _notas = [float(_nota) for _nota in _dados if _dados.index(_nota) % 8 == 5]
        _aprovados = [True if _nota >= 6.0 else False for _nota in _notas]

        for _indice in range(int(len(_dados) / 8)):
            _alunos[_matriculas[_indice]] = {'nome': _nomes[_indice], 'sobrenome': _sobrenomes[_indice],
                                             'ano de nascimento': _anos[_indice], 'turma': _turmas[_indice],
                                             'nota': _notas[_indice], 'aprovado': _aprovados[_indice]}

    return _alunos


def salva_arquivo(_alunos, _arquivo):
    with open(_arquivo, 'w') as _arq:
        for _aluno in _alunos:
            _matricula = _aluno
            _nome = _alunos[_aluno]['nome']
            _sobrenome = _alunos[_aluno]['sobrenome']
            _ano_nascimento = _alunos[_aluno]['ano de nascimento']
            _turma = _alunos[_aluno]['turma']
            _nota = _alunos[_aluno]['nota']
            _aprovado = _alunos[_aluno]['aprovado']

            _texto = f"{_matricula}\n{_nome}\n{_sobrenome}\n{_ano_nascimento}\n{_turma}\n{_nota}\n{_aprovado}\n\n"
            _arq.write(_texto)


def registra_alunos(_numero_alunos, _matriculados):
    _alunos = _matriculados

    for _aluno in range(_numero_alunos):
        _matricula = (input("Digite o número de matrícula:\n"))
        _nome = input("Digite o nome:\n")
        _sobrenome = input("Digite o ÚLTIMO sobrenome:\n")
        _ano_nascimento = int(input("Digite o ano de nascimento:\n"))
        _turma = input("Digite a turma:\n")
        _nota = float(input("Digite a nota:\n"))
        _aprovado = None

        if _nota >= 6.0:
            _aprovado = True
        else:
            _aprovado = False

        _alunos[_matricula] = {'nome': _nome, 'sobrenome': _sobrenome, 'ano de nascimento': _ano_nascimento,
                               'turma': _turma, 'nota': _nota, 'aprovado': _aprovado}

    return _alunos


"""
Exercício 27: (aproveitando código do 26. NEM FODENDO refaço isso tudo!)
Incluir:

 - informações da turma
 - exibir alunos e médias
 - exibir alunos aprovados e reprovados
"""


def exibe_alunos(_alunos):
    for _aluno in _alunos:
        print(f"\n{_aluno}: {_alunos[_aluno]}")


def busca_aprovados(_alunos):
    for _aluno in _alunos:
        if _alunos[_aluno]['aprovado']:
            print(f"{_alunos[_aluno]['nome']}: aprovado.\n")


def busca_reprovados(_alunos):
    for _aluno in _alunos:
        if not _alunos[_aluno]['aprovado']:
            print(f"{_alunos[_aluno]['nome']}: reprovado.\n")


def executar():
    _arquivo = "Arquivos_Exercicios/Alunos.txt"
    _alunos = None

    with open(_arquivo, 'r') as _arq:
        if len(_arq.read()) != 0:
            _alunos = carrega_dados(_arquivo)

    _mensgem = '\nSelecione a operação:\n' \
               '1 - Registrar alunos\n' \
               '2 - Exibir lista de alunos\n' \
               '3 - Exibir lista de aprovados\n' \
               '4 - Exibir lista de reprovados\n' \
               '0 - Sair\n' \

    while True:
        _opcao = input(_mensgem)

        if _opcao == '0':
            salva_arquivo(_alunos, _arquivo)
            print("Encerrando...")
            break
        elif _opcao == '1':
            _numero_alunos = int(input("\nDigite o número de alunos que serão adicionados:\n"))
            _alunos = registra_alunos(_numero_alunos, _alunos)
            salva_arquivo(_alunos, _arquivo)
        elif _opcao == '2':
            exibe_alunos(_alunos)
        elif _opcao == '3':
            busca_aprovados(_alunos)
        elif _opcao == '4':
            busca_reprovados(_alunos)
        else:
            print("Opção inválida!")


executar()

"""
Exercício 28: Fazer um programa que recebe um arquivo
de entrada e um nome de arquivo de saída. Cada linha
deve ter 30 caracteres e o arquivo de saída deve ter
o texto do arquivo de entrada escrito de trás para frente.
"""
entrada = "Arquivos_Exercicios/Texto.txt"
saida = "Arquivos_Exercicios/Reverso.txt"


def carrega_arquivo(_arquivo):
    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read().split('\n')
        _texto = ''.join(_texto)

        return _texto


def separa_linhas(_texto):
    _linhas = []
    _linha = ''
    _cont = 0

    for _char in _texto:
        if len(_linha) <= 30:
            _linha += _char
        else:
            _linhas.append(_linha)
            _linha = _char

    _linhas = '\n'.join(_linhas)

    return _linhas


def escreve_inverso(_entrada, _saida):
    _texto = carrega_arquivo(_entrada)
    _linhas = separa_linhas(_texto)
    _linhas = _linhas[::-1]

    with open(_saida, 'w') as _s:
        _s.write(_linhas)


escreve_inverso(entrada, saida)

"""
Exercício 29: criar um programa que manipula um arquivo
contendo os campos de código do vendedor, nome do vendedor,
valor de venda e mês. Deve apresentar um menu com as opções:

 - Criar arquivo
 - Incluir registro de vendedor
 - Excluir registro de vendedor
 - Alterar valor de uma venda
 - Imprimir os registros
 - Excluir o arquivo
 - Finalizar

Os registros devem estar em ordem crescente de código de vendedor
e mês, não devendo haver repetição dos mesmos.
"""
# formato da chave -> (código, mês)


def cria_arquivo():
    _local_arquivo = "Arquivos_Exercicios/"
    _nome_arquivo = input("Digite o nome do arquivo a ser criado:\n")

    _arquivo = _local_arquivo + _nome_arquivo + '.txt'

    with open(_arquivo, 'r') as _arq:
        pass


def salva_arquivo(_registros):
    _local_arquivo = "Arquivos_Exercicios/"
    _nome_arquivo = input("Digite o nome do arquivo para salvar:\n")

    _arquivo = _local_arquivo + _nome_arquivo + '.txt'

    with open(_arquivo, 'a') as _arq:
        for _registro in _registros:
            _codigo = _registro[0]
            _mes = _registro[1]
            _nome = _registros[_registro]["nome"]
            _vendas = _registros[_registro]["vendas"]

            _texto = f"{_codigo}\n{_mes}\n{_nome}\n{_vendas}\n"

            _arq.write(_texto)


def inclui_registro():
    _registros = {}

    _codigo = input("Digite o código do vendedor:\n")
    _mes = input("Digite o mês das vendas:\n")

    _nome = input("Digite o nome do vendedor:\n")
    _vendas = float(input("Digite o valor das vendas:\n"))

    _registros[(_codigo, _mes)] = {"nome": _nome, "vendas": _vendas}

    salva_arquivo(_registros)

    return _registros


def exclui_registros(_registros):
    _codigo = input("Digite o código do vendedor:\n")
    _mes = input("Digite o mês das vendas:\n")

    del _registros[(_codigo, _mes)]

    salva_arquivo(_registros)


def altera_vendas(_registros):
    _codigo = input("Digite o código do vendedor:\n")
    _mes = input("Digite o mês das vendas:\n")

    _vendas = float(input("Digite o valor da venda:\n"))

    _registros[(_codigo, _mes)]["vendas"] = _vendas

    salva_arquivo(_registros)

    return _registros


def imprime_registros():
    _local_arquivo = "Arquivos_Exercicios/"
    _nome_arquivo = input("Digite o nome do arquivo a ser criado:\n")

    _arquivo = _local_arquivo + _nome_arquivo + '.txt'

    with open(_arquivo, 'r') as _arq:
        _texto = _arq.read()

        print(_texto)


def apaga_arquivo():
    _local_arquivo = "Arquivos_Exercicios/"
    _nome_arquivo = input("Digite o nome do arquivo a ser criado:\n")

    _arquivo = _local_arquivo + _nome_arquivo + '.txt'

    os.remove(_arquivo)


def executar():
    _registros = {}
    while True:
        _mensagem = "Escolha uma opção:\n" \
                    "0-Sair\n" \
                    "1-Criar um novo arquivo\n" \
                    "2-Inserir um novo registro\n" \
                    "3-Remover um registro existente\n" \
                    "4-Alterar um registro\n" \
                    "5-Imprimir registros de um arquivo\n" \
                    "6-Apagar um arquivo\n"

        _opcao = input(_mensagem)

        if _opcao == '0':
            print("Encerrando...")
            break
        elif _opcao == '1':
            cria_arquivo()
        elif _opcao == '2':
            inclui_registro()
        elif _opcao == '3':
            exclui_registros(_registros)
        elif _opcao == '4':
            altera_vendas(_registros)
        elif _opcao == '5':
            imprime_registros()
        elif _opcao == '6':
            apaga_arquivo()
        else:
            print("Opção inválida!")


executar()
