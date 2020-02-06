"""
Pacotes externos

Para instalar pacotes externos, é utilizado o gerenciador de pacotes PIP - Python Installer Package
Para conhecer os pacotes externos oficiais: https://pypi.org
Para atualizar o pip: pip install --upgrade pip

Sintaxe: pip install <nome do pacote> -> Instala o pacote.
Exemplo: pip install colored

Colored: permite a impressão de textos coloridos no terminal. Compatível apenas com Linux e Mac.
No Windows, não apresenta erro, mas na impressão o texto aparecerá com um código de cores.

Atualizando um pacote: pip install <pacote> --upgrade
Exemplo: pip install colored --upgrade
"""
from colored import *

print(dir(colored))

estilo = fg(57), bg(226)  # Criando um estilo para o texto.
texto = "Nepu"  # Texto a ser estilizado.

print(stylize(texto, estilo))  # stylize(texto, estilo) -> adiciona o estilo ao texto.
