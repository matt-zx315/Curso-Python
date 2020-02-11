"""
Sistema de arquivos e navegação

Para fazer uso do sistema de arquivos do sistema operacional,
é preciso importar o módulo os (Operating System - Sistema Operacional).

 - os.getcwd() -> Retorna o diretório onde está o programa em execução.
 - os.chdir(caminho) -> Muda de diretório.
 - os.path.isabs(caminho) -> Verifica se o caminho é absoluto ou não. Retorna True ou False.
 - os.name -> Retorna o tipo do sistema operacional.
 - os.uname() -> Retorna o tipo do sistema com mais detalhes.
 - os.chdir() -> Muda o diretório. Retorna um FileNotFoundError se o diretório não existir.
 - os.path.join(caminho, caminhos) -> Cria um caminho para um diretório, este existindo ou não.
 - os.listdir(caminho) -> Mostra todo o conteúdo do diretório recebeido em forma de lista.
 - os.scandir(caminho) -> Retorna um objeto tipo ScandirIterator com elementos do tipo DirEntry.
"""
import os
import sys

print(os.getcwd())

os.chdir('..')  # Se o diretório atual for a raíz do SO, então chdir() não fará nada.
print(os.getcwd())

print(os.path.isabs("/home"))
print(os.path.isabs("/Python"))

"""
IMPORTANTE: a barra (/) sozinha faz com que o retorno seja True, mesmo que o diretório não exista.
USUÁRIOS WINDOWS: para verificar diretórios em Windows, utilizar "C:\\Users\\<nome do usuário>."
O uso de \\ é necessário para que o Python entenda que o caminho com a barra inverida, já que esta,
em strings, é um caractere de escape.
O ideal é não usar Windows para desenvolver em Python, mas como a maioria das aplicações são feitas
para rodar no Windows, é necessário saber isso.
"""

print(os.name)  # Retorna posix para Linux/Mac e mt para Windows
print(os.uname())  # No Windows, utilizar sys.platform (Necessário importar o módulo sys)
print(sys.platform)

caminho = os.path.join(os.getcwd(), '..')
os.chdir(caminho)
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), 'Curso Python', 'Topico_10'))  # Aceita 3 ou mais argumentos.
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), '../Topico_11'))  # Acessando uma pasta irmã.
print(os.getcwd())

print(os.listdir(os.getcwd()))  # Vendo o conteúdo do diretório atual.
print(os.listdir(os.path.join(os.getcwd(), '..')))  # Vendo o conteúdo de um diretório acima.

print(os.getcwd())

# Para usar scandir(), é recomendável criar uma variável:
scan1 = os.scandir()

print(type(scan1))

diretorio = list(scan1)
print(type(diretorio[0]))

for item in diretorio:
    print(item.name)  # Objetos do tipo DirEntry possuem um atributo chamado name, ou seja, o nome do arquivo.

scan2 = os.scandir(os.path.join(os.getcwd(), '..'))
# Ao passar um caminho como argumento de scandir(), o valor path dos objetos passará a ser o caminho do argumento.

diretorio2 = list(scan2)

for item in diretorio2:
    print(item)

# Sobre os objetos do tipo DirEntry:
print(dir(diretorio[0]))  # Retornam diversos detalhes sobre um arquivo, diretório ou link simbólico.
print(diretorio[0].inode())  # Número de identificação do objeto na árvore de diretório.
print(diretorio[0].is_dir())  # Verifica se o objeto é um diretório.
print(diretorio[0].is_file())  # Verifica se o objeto é um arquivo.
print(diretorio[0].is_symlink())  # Verifica se o objeto é um link simbólico.
print(diretorio[0].name)  # Retorna o nome do objeto e sua extensão.
print(diretorio[0].path)  # Retorna o caminho até o objeto a partir do diretório atual.
print(diretorio[0].stat())  # Exibe informações sobre o objeto, inclusive seu tamanho em bytes.

# Quando utilzar a função scandir(), é necessário fechá-la após seu uso, assim como quando um arquivo é aberto.
scan1.close()
scan2.close()
