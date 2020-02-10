"""
Escrevendo em arquivos

 OBS.:
 - Ao abrir um arquivo para leitura, não será possível escrever no mesmo.
 - O contrário também é verdade: arquivos abertos para escrita não podem ser lidos.

Para escrever em arquivos:
 - O arquivo deve ser aberto no modo de escrita -> open('arquivo'.txt, 'w').
 - Para escrever no arquivo, utiliza-se a função write().

Ao escrever em um arquivo já existente utilizando o modo de escrita 'w',
toda vez que o programa executar, o arquivo original será sobrescrito,
ou seja, o conteúdo anterior será apagado e substituído pelo novo.
"""

with open("novo.txt", 'w') as arquivo:  # O argumento 'w' significa escrita. É o modo de abertura do arquivo.
    arquivo.write("Escrevendo uma linha no arquivo.\n")
    arquivo.write("Outra linha\n")
    arquivo.write("Assim que se escrevem múltiplas linhas.")
