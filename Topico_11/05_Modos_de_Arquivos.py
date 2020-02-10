"""
Modos de abertura de arquivos:

r -> leitura de arquivos;
w -> escrita em arquivos. Sobrescreve no caso do arquivo já existir;
x -> abre para escrita somente se o arquivo não existir. Caso o arquivo exista, retorna um FileExistsError.
a -> adiciona conteúdo NO FINAL do arquivo. Cria o arquivo caso não exista. Não é possível controlar o cursor.
+ -> modo de atualização. Leitura e escrita. Deve ser precedido sempre uma das letras acima.
"""
from colored import fg, stylize

try:
    with open("Novo.txt", 'x') as arquivo:
        arquivo.write("Nepu")
except FileExistsError as err:
    mensagem = "Arquivo já existe!"
    estilo = fg(196)
    print(stylize(mensagem, estilo))

with open("frutas.txt", 'a') as frutas:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ").lower()

        if fruta != 'sair':
            frutas.write(fruta + '\n')
        else:
            break
