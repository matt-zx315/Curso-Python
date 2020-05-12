"""
Escrevendo em arquivos CSV

reader() = leitor -> Cria um objeto que permite a leitura de arquivos .csv
writer() = escritor -> Cria um objeto que permite a escrita em arquivos .csv
"""
from csv import writer, DictWriter

# with open("CSV/livros.csv", 'w') as livros:
#     escritor_csv = writer(livros)
#     livro = None
#     escritor_csv.writerow(['Título', 'Volume', 'Autor'])  # Cabeçalho
#
#     while livro != 'sair':
#         livro = input("Título do livro: ")
#         if livro != 'sair':
#             volume = int(input("Volume do livro: "))
#             autor = input("Autor do livro: ")
#             escritor_csv.writerow([livro, volume, autor])

with open("CSV/livros.csv", 'w') as livros:
    cabecalho = ['Título', 'Volume', 'Autor']
    escritor_csv = DictWriter(livros, fieldnames=cabecalho)
    escritor_csv.writeheader()
    livro = None

    # OBS.: As chavesdo dicionário devem ser as mesmas do cabeçalho!
    while livro != 'sair':
        livro = input("Título do livro: ")
        if livro != 'sair':
            volume = int(input("Volume do livro: "))
            autor = input("Autor do livro: ")
            escritor_csv.writerow({'Título': livro, 'Volume': volume, 'Autor': autor})
