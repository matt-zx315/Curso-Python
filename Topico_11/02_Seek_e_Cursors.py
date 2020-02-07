"""
Seek e cursors

 - seek() -> utilizada para mover o cursor pelo arquivo.
 Recebe como parâmetro um valor numérico que indica a posição
 na qual o cursor será colocado.

 Caso o valor seja maior que o tamanho da string, o texto não será impresso.
 A função, no entanto, não retorna erro.

 - readline() -> Lê o arquivo linha a linha.
 - readlines()

 A função read() ainda permite limiter o número de caracteres lidos,
 parando o cursor.
"""

arquivo = open("texto.txt")
leitura = arquivo.read()
print(leitura)

# Usando seek() para movimentar o cursor
# arquivo.seek(2600)
# leitura = arquivo.read()
# print(leitura)

arquivo.seek(0)
print(arquivo.readline())

arquivo.seek(0)

for linha in leitura.split("\n"):
    print(arquivo.readline())

print(leitura.split(" "))

arquivo.seek(0)
print(arquivo.readlines())  # Separa o texto em uma lista, com cada linha sendo um elemento.

arquivo.seek(0)  # Sempre usar seek() após executar uma leitura de arquivo.
linhas = arquivo.readlines()

print(len(linhas))

arquivo.seek(0)
print(arquivo.read(50))  # Lê apenas os 50 primeiros caracteres.

arquivo.close()
