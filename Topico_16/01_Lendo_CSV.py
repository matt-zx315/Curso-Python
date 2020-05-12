"""
Leitura de arquivos CSV

CSV -> Comma Separated Values (Valores Separados por Vírgula)

OBS.: A vírgula não é o único separador num CSV. Podem ser utilizados
ainda ponto e vírgula, espaço e outros. Ele precisa apenas ser difinido.

Em alguns arquivos,é possível que não haja um cabeçalho na primeira linha,
estando esse em outro arquivo, separado dos dados.
"""
from csv import reader, DictReader

# Não é a forma ideal de se trabalhar com arquivos .csv
with open("CSV/lutadores.csv") as lutadores:
    dados = lutadores.read()
    # print(type(dados))
    dados = dados.split(',')[2:]  # Ignorando o cabeçalho
    print(dados)

"""
A linguagem Python possui duas formas de trabalhar com arquivos csv:
    -reader -> permite a iteração sobre as linhas dos arquivos .csv como listas;
    -DictReader -> semelhante ao reader, porem organiza as listas como OrderedDicts.
"""
lista = []

with open("CSV/lutadores.csv") as lutadores:
    leitor_csv = reader(lutadores)
    next(leitor_csv)

    for linha in leitor_csv:
        # Cada linha é um arquivo
        print(f'{linha[0]} é natural de {linha[1]} e mede {linha[2]} cm.')

        # Armazenando valores para utilizá-los posteriormente
        lista.append(str(linha[0]))
        lista.append(str(linha[1]))
        lista.append(int(linha[2]))

print(lista)

with open("CSV/lutadores.csv") as lutadores:
    leitor_csv = DictReader(lutadores, delimiter=',')  # Informando qual o separador.

    for linha in leitor_csv:
        # Cada linha é um OrderedDict que tem como chaves os valores do cabeçalho.
        print(f'{linha["Nome"]} é natural de {linha["País"]} e mede {linha["Altura (em cm)"]} cm.')
