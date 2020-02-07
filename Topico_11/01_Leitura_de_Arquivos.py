"""
Leitura de arquivos

Para ler um arquivo, utilizamos a função integrada open()

 - open() -> Forma simples: passar apenas um argumento de entrada (arquivo ou caminho do arquivo a ser lido).
 Retorna um objeto do tipo _io.IOWrapper.
 Essa funçao abre um arquivo para leitura. Esse arquivo deve existir,
 caso contrário, a função retorna o erro FileNotFoundError.

 Ao imprimir um arquivo aberto com a função open:

 <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
         tipo           nome          modo      codificação

 - tipo: tipo de objeto gerado pela função.
 - nome: nome do arquivo aberto.
 - modo: para quê o arquivo foi aberto. 'r' significa leitura (do inglês, "read").
 - codificação: a codificação utilizada para escrever o arquivo.

 - read() -> Lê o conteúdo do arquivo aberto.
 Retorna um objeto do tipo string (str).
 
 Caso o arquivo já tenha sido lido anteriormente, a função não exibirá nada.
 Isso acontece por causa de um recurso do Python chamado cursor, o qual funciona da mesma forma
 que o cursor quando se está escrevendo um arquivo. Toda vez que um arquivo é aberto, o cursor
 é posicionado no final do mesmo. Portanto, abrir o mesmo arquivo uma segunda vez não terá efeito algum,
 já que o cursor lerá apenas quilo que estiver na sua frente. Se o cursor está no fim do arquivo,
 então não haverá nada mais para ser lido. 

OBS.: Ao abrir um arquivo com a função open(), é criada uma conexão do arquivo
com o disco do computador e o programa. Essa conexão é chamada de streaming.
Ao encerrar os trabalhos com arquivos, usar a função close() para
fechar essa conexão.

Passos para trabalhar com arquivos:

 1 - Abrir o arquivo
 2 - Trabalhar o arquivo (leitura/escrita)
 3 - Fechar o arquivo

Por que encerrar?

 - Quando um arquivo é aberto por um programa, é criado um mecanismo chamado lock.
 Esse mecanismo impede que outros programas acessem o arquivo aberto.
 - Tentar acessar um arquivo fechado retorna um ValueError.
 - Para verificar se um arquivo está aberto ou fechado, utiliza-se arquivo.closed.
 - A verificação serve para evitar que esse erro ocorra. Dessa forma,
 caso o arquivo esteja fechado, será necessário reabrí-lo, evitando assim o erro
 e, consequentemente, a interrupção do programa.

"""

arquivo = open("texto.txt")
leitura = arquivo.read()

print(arquivo)
print(type(arquivo))
print(leitura)
print(type(leitura))
print(len(leitura))  # Contando o número de caracteres.

leitura = leitura.split('\n')
print(len(leitura))  # Contando o número de linhas.

print(arquivo.closed)  # Verifica se o arquivo está fechado.

arquivo.close()

print(arquivo.closed)
