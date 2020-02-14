"""
Sistema de arquivos - Manipulação

1º passo: Verificar se o arquivo ou diretório existe (os.path.exists(caminho))
2º passo: Caso o arquivo não exista, ele deve ser criado.

OBS.: Nos sistemas MAC, é possível que ocorra um erro do tipo PermissionError.
Isso acontece porque, nesses sistemas, o programa precisa de permissões administrativas,
sendo que o programa não é executado com essas permissões.
Nos sitemas Windows e Linux esse erro não ocorre com tanta frequência. No entanto,
ainda é possível ter esse erro caso o programa não tenha permissão
para criar arquivos ou diretórios em determinado local.

Há também o erro FileExists caso o programa tente criar um arquivo com nome já existente.
A mesma coisa pode ocorrer com a criação de diretórios.

É importante lembrar, também, que o novo arquivo/diretório será criado no diretório em que o programa
está executando no momento. Para criar um arquivo ou diretório em um diretório diferente, será necessário
passar o seu caminho, relativo ou absoluto.

Sobre os comandos de deleção: Arquivos apagados pelo software não não para a lixeira.
eles são excluídos PERMANENTEMENTE.
OBS.: Se o programa tentar apagar um arquivo em uso no Windows, haverá um erro.
A função os.remove() também retorna erro do tipo FileNotFoundError caso o arquivo não exista.
Ainda sobre a remoção de arquivos, caso o argumento passado seja um diretório, e não um arquivo,
a função retorna um erro do tipo IsADirectoryError

Apagar diretórios é possível utilizando a função os.rmdir(). No entanto, é preciso que o diretório
passado esteja vazio. Caso contrário, retorna um OSError. Também é possível ter um FileNotFoundError
no caso do diretório não existir.
"""
import os
from send2trash import send2trash  # Biblioteca utilizada para enviar arquivos para a lixeira, permitindo restaurá-los.
# OBS.: Caso o pacote não instale, utilizar sudo apt-get install lsb-core para resolver o problema (Linux).
import tempfile

# # Descobrindo se o arquivo existe:
# print(os.path.exists("arquivo.txt"))
# print(os.path.exists("frutas.txt"))
#
# # Descobrindo se o diretório existe pelo caminho relativo. O caminho absoluto é aquele que vem desde a raíz do sistema.
# print(os.path.exists("../Topico_25"))
# print(os.path.exists("../Topico_10"))
# print(os.path.exists("../Topico_10/pacote"))

# Criando o arquivo - forma 1:
# open("teste.txt", 'w').close()  # Cria e fecha o arquivo. Outra opção é passar o argumento 'a' ao invés de 'w'.
#
# # Criando o arquivo - forma 2:
# with open("outro.txt", 'a') as arquivo:  # Tanto faz utilziar 'a' ou 'w'.
#     pass  # Palavra chave utilizada para encerrar um bloco de código caso não haja nada nele.
#
# # Criando o arquivo - forma 3:
# os.mknod('arquivo.txt')
#
# # Criando um diretório:
# os.mkdir("Pasta")

"""
Para criar vários diretórios um dentro do outro com nkdir(),
é preciso criar um por vez.

os.mkdir("Pasta")
os.mkdir("Pasta/Subpasta1")
os.mkdir("Pasta/Subpasta2")
os.mkdir("Pasta/Subpasta1/Pacote")
etc.
"""

# # Criando uma árvore de diretórios (sim, é possível criar diretórios irmãos dessa forma O.O):
# os.makedirs("Pasta/Subpasta1/Pacote/../../Subpasta2")
#
# # O parâmetro exist_ok=True ignora a criação do(s) diretório(s) caso este(s) já exista(m).
# os.makedirs("Pasta/Subpasta1/Pacote/../../Subpasta2", exist_ok=True)
#
# # Renomeando diretórios:
# os.rename("Pasta/Subpasta2", "Pasta/Diretório1")  # Retorna um OSError se o diretório não estiver vazio.
#
# # Renomeando arquivos:
# os.mknod("Arquivo.txt")
# os.rename("Arquivo.txt", "Renomeado.txt")
#
# # Apagando arquivos:
# os.remove("Renomeado.txt")
#
# # Apagando diretórios (um por vez):
# os.rmdir("Pasta/Subpasta2")
#
# # Apagando uma árvore de arquivos:
# for dado in os.scandir("Pasta/Subpasta1"):
#     if dado.is_file():
#         os.remove(dado.path)
#     elif dado.is_dir():
#         os.rmdir(dado.path)  # Funcionará apenas se o(s) diretório(s) estiver(em) vazio(s).

# # Removendo uma árvore de diretórios:
# os.removedirs("Pasta/Subpasta1/Pacote")

"""
Se algum dos diretórios não estiver vazio, o processo para, precisando ser executado novamente.
Diretórios vazios dentro de outros diretórios serão apagados, mas o processo pode parar e será
necessário executar o código novamente. *SUGESTÃO:* Usar loop while(os.scandir(caminho) > 0).
"""

# # DICA: Para gerar múltiplos arquivos numa pasta no Linux, usar o comando touch arquivo{1..1000}.txt
# send2trash("Pasta")  # Exclui arquivos de acordo com o caminho. Remove diretórios com e sem arquivos.
# # OBS.: Se o arquivo não existir, retorna um OSError.

# # Trabalhando com arquivos e diretórios temporários:
# with tempfile.TemporaryDirectory() as tmp:
#     print(f"Diretório temporário criado em {tmp}.")
#
#     with open(os.path.join(tmp, 'arquivo.txt'), 'w') as arq:
#         arq.write("Nepu\n")
#     input()  # Só serve para manter os arquivos temporários ativos dentro do bloco with.

"""
OBS.: O código acima pode não funcionar em sistemas Windows
pelo fato de trabalharem de forma diferente com arquivos temporários.
"""

# with tempfile.TemporaryFile() as tmpf:  # Arquivos temporários são escritos apenas em binários.
#     tmpf.write(b"Nepu")  # Convertendo string para binário. Retorna TypeError se não for usado o b''.
#     tmpf.seek(0)
#     print(tmpf.read())

arquivo = tempfile.NamedTemporaryFile()  # Gera um arquivo temporário com um nome.
arquivo.write(b'Nepu')

print(arquivo.name)
print(arquivo.read())

input()
arquivo.close()
