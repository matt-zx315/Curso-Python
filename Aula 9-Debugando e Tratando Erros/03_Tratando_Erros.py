"""
Try/Except/Else/Finally

O bloco try/except é utilizado para tratar erros que podem acontecer no código.
Ele previneque o programa pare de funcionar e o usuário receba mensagens de erro.

sintaxe geral:

try:
    <problema ou execução problemática>
except:
    <o que fazer se der problema>

OBS.: Tratar erros genéricos não é a melhor maneira. O ideal é sempre tratar de forma específica.

try:
    <problema ou execução problemática>
except TipoDoErro:
    <o que fazer se der problema>

A desvantagem é que, caso haja outro tipo de erro,
ele não será tratado, e a execução do código será interrompida.

O tipo de exceção pode ser nomeado:

try:
    <problema ou execução problemática>
except TipoDoErro as err:
    <o que fazer se der problema>

err é um nome convencionado a se usar em Python para o erro retornado.

É possível, ainda, colocar diversos blocos except em sequência, cada um tratando um tipo de erro.
Outra solução seria um bloco except "semi-genérico":

try:
    <problema ou execução problemática>
except (TipoDoErro1, TipoDoErro2, ... TipoDoErroN) as err:
    return f"Ocorreu o seguinte erro: {err}"

#########################################
## DICA de quando e onde tratar código:##
##                                     ##
## TODA ENTRADA DEVE SER TRATADA       ##
##                                     ##
## A função do usuário é DESTRUIR      ##
## o seu sistema!                      ##
#########################################

else, em um bloco de tratamento de erros, é utilizado para executar as instruções
caso não ocorram erros.

finally executa sempre, seja após o else (não houve exceção) ou except (houve exceção).
Sua função é fechar ou desalocar recursos (por exemplo: encerrar conexão com banco de dados,
fechar um arquivo aberto para leitura ou escrita etc.).
Evitar utilizar essa palavra fora dos casos citados acima, uma vez que sua execução ocorre
logo após o tratamento de exceções, estas ocorrendo ou não. Nesses casos, não utilizar else.
"""

# Exemplo 1 - Tratando um erro genérico:
try:
    nepu()  # O programa tenta executar a função nepu()
except:
    print("DEU RUIM!")  # Se falhar, a alternativa é exibir uma mensagem e continuar a execução do programa.

# Exemplo 2 - Outro erro genérico:
try:
    len(5)
except:
    print("Não sou nenhum especialista mas... Acho que tem algo errado aqui.")

# Exemplo 3 - Tratando um erro específico:
try:
    nepu()
except NameError:
    print("ISSO NON ECZISTE!")

# Nomeando o tipo de erro:
try:
    len(5)
except TypeError as err:
    print(f"A aplicação retornou o erro: {err}")

# Efetuando mais de um tratamento de exceção:
try:
    # len(5)
    # nepu()
    print("lista"[9])
except NameError as err_a:
    print(f"A aplicação retornou o erro do tipo NameError: {err_a}")
except TypeError as err_b:
    print(f"A aplicação retornou o erro do tipo TypeError: {err_b}")
except:
    print("Deu um erro diferente")


def pega_valor(_dicionario, _chave):
    try:
        return _dicionario[_chave]
    except KeyError:
        return None
    except TypeError:
        return None


dicionario = {'a': 1}

print(pega_valor(dicionario, 'b'))
print(pega_valor(lambda x: x[0], 'a'))

# Usando else:


def recebe_numero():
    # Sem um bloco Try/Except, o usuário poderia passar um valor inapropriado, como uma letra, por exemplo.
    try:
        num = int(input("Digite um número: "))
    except ValueError:  # Saber o tipo de erro que pode ocorrer requer experiência. Pra isso existem os testes.
        print("Digite apenas valores INTEIROS!!!")
    else:
        print(f"Você digitou: {num}")


# recebe_numero()

# Usando finally:


def recebe_real():
    try:
        _real = float(input("Digite um número real: "))
    except ValueError:
        print("Eu disse NÚMERO REAL!!!")
    else:
        print(f"Você digitou: {_real}")
    finally:
        print("Executando o finally")


# recebe_real()
# recebe_real()
# recebe_real()
# recebe_real()

# Usando o tratamento de exceções:


def divisao(_a, _b):
    try:
        return float(_a) / float(_b)
    except ValueError:
        return "Valor(es) incorreto(s)!"
    except ZeroDivisionError:
        return "Divisão por zero não existe!"


a = input("Digite um número real: ")
b = input("Digite um número real: ")

print(divisao(a, b))