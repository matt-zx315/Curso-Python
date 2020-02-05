"""
Erros mais comuns em Python

Entendendo a saída de erros:

- Traceback: Saída de erros;
- File: Arquivo e caminho;
- line: linha onde se encontra o erro
- NameError: tipo de erro.

OBS.: No PyCharm e em outras IDEs, o Traceback mostra o local do arquivo que apresenta o erro.
No entanto, ao rodar o mesmo código no console Python, essa informação não é exibida.
Já no terminal, o nome do arquivo é exibdo, mas não o seu caminho.

------------------------------------------------------------------------------------------------------------------------

###################
1) SyntaxError: erro de sintaxe. O Python não reconhece o código escrito como parte da linguagem.
###################

------------------------------------------------------------------------------------------------------------------------
def funcao:
    print("Tá errado!")

  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 27
    def funcao:
              ^
SyntaxError: invalid syntax

Regra de sintaxe não respeitada.
------------------------------------------------------------------------------------------------------------------------
None = 1

File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 40
    None = 1
    ^
SyntaxError: can't assign to keyword

Atribuíção de valor a uma palavra reservada.
------------------------------------------------------------------------------------------------------------------------
return

File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 51
    return
    ^
SyntaxError: 'return' outside function

return foi usada fora de uma função.
------------------------------------------------------------------------------------------------------------------------

###################
2) NameError: Ocorre quando uma variável ou função não é definida.
###################

------------------------------------------------------------------------------------------------------------------------
printf("Nepu")  # Erro de quem veio de C pra Python (NameError)

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 7, in <module>
    printf("Nepu")  # Erro de quem veio de C pra Python (NameError)
NameError: name 'printf' is not defined

printf não é uma função definida no código.
------------------------------------------------------------------------------------------------------------------------
print(num)

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 66, in <module>
    print(num)
NameError: name 'num' is not defined

Variável num não declarada.
------------------------------------------------------------------------------------------------------------------------

###################
3) TypeError: Aplicação de uma função/operação/ação a um tipo errado
###################

------------------------------------------------------------------------------------------------------------------------
len(5)

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 115, in <module>
    len(5)
TypeError: object of type 'int' has no len()

Não existe len de inteiro.
------------------------------------------------------------------------------------------------------------------------
print("Nepu" + [])

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 121, in <module>
    print("Nepu" + [])
TypeError: can only concatenate str (not "list") to str

Não é possível concatenar uma string com uma lista.
------------------------------------------------------------------------------------------------------------------------

###################
4) Index Error: Tentativa de acesso a um elemento de dado indexado utilizando um índice inválido.
###################

------------------------------------------------------------------------------------------------------------------------
lista = [6]
print(lista[1])

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 83, in <module>
    print(lista[1])
IndexError: list index out of range

A lista só tem um elemento (índice 0), mas houve tentativa de acesso a um índice inválido.
------------------------------------------------------------------------------------------------------------------------
lista = "Nepu"
print(lista[0][5])

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 95, in <module>
    print(lista[0][5])
IndexError: string index out of range

Tentativa de acesso a um índice inexistente da string.
------------------------------------------------------------------------------------------------------------------------

###################
5) ValueError: retornado quando uma função built-in (integrada) recebe um argumento correto, mas com valor inapropriado.
###################

------------------------------------------------------------------------------------------------------------------------
print(int('Errou!'))

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 133, in <module>
    print(int('Errou!'))
ValueError: invalid literal for int() with base 10: 'Errou!'

int() espera receber uma string, mas não pode converter por causa da base 10,
aceitando apenas caonjuntos de caracteres de 0 a 9.
------------------------------------------------------------------------------------------------------------------------

###################
6) KeyError: ocorre ao tentar acessar um dicionário utilizando uma chave que não existe.
###################

------------------------------------------------------------------------------------------------------------------------
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
print(dicionario['j'])

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 150, in <module>
    print(dicionario['j'])
KeyError: 'j'

Chave inexistente.

OBS.: No caso de um default dict, não existe esse tipo de erro. Um valor padrão é gerado para a chave inexistente.
------------------------------------------------------------------------------------------------------------------------

###################
7) AttributeError: ocorre quando uma variável não tem um determinado atributo ou função.
###################

------------------------------------------------------------------------------------------------------------------------
tupla = (1, 2, 3)
tupla.sort()

Traceback (most recent call last):
  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 168, in <module>
    tupla.sort()
AttributeError: 'tuple' object has no attribute 'sort'

Tuplas não possuem o método sort().
------------------------------------------------------------------------------------------------------------------------

###################
8) IndentationError: erro de indentação. Retornado quando a indentação de 4 espaços não é respeitada.
###################

------------------------------------------------------------------------------------------------------------------------
def nova():
print("Nepu")

  File "C:/Documents/Curso Python/Topico_09/01_Erros_Comuns.py", line 184
    print("Nepu")
        ^
IndentationError: expected an indented block

Necessário indentar a linha.
------------------------------------------------------------------------------------------------------------------------

OBS.: Exceptions (excessões) e Errors (erros) são sinônimos em programação.
"""

