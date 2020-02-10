"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional,
o software precisa ter permissão:

    - de leitura: para ler o arquivo;
    - de escrita: para escrever dados no arquivo.

OBS.: Para testar essa permissão, é possível usar o comando cat <arquivo>
para verificar se o usuário tem permissão de leitura para o arquivo
em questão ou não. Esse comando somente funciona em sistemas Linux ou Mac.

StringIO é utilizado para ler e escrever arquivos em memória.
Isso significa que o arquivo não será gravado em disco,
mas sim armazenado temporariamente na memória, sendo removvido
após o fechamento do programa.

Podemos criar um arquivo em memória já com uma string inserida
ou mesmo vazio para a inserção de texto.
"""
from io import StringIO

mensagem = "Apenas uma string comum."

# Criando arquivo em memória
arquivo = StringIO(mensagem)

print(arquivo.read())
