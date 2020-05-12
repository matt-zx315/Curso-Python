"""
Métodos de data e hora

"""
import datetime
import functools
import timeit
from textblob import TextBlob

agora = datetime.datetime.now()  # Permite especificar um timezone (horário local)
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  # Não é possível especificar timezone
print(hoje)
print(type(hoje))
print(repr(hoje))

# Agendando um procedimento com datetime.datetime.combine()
tempo = datetime.timedelta(days=1)
# datetime.time() -> Ajusta os valores de hora, minuto, segundo e microssegundo para 0.
procedimento = datetime.datetime.combine((agora + tempo), datetime.time())
print(procedimento)
print(type(procedimento))
print(repr(procedimento))

"""
# Encontrar dia da semana

O método weekday() possui uma tabela de dias da semana em forma de números:

0 - Segunda-feira (Monday)
1 - Terça-feira (Tuesday)
2 - Quarta-feira (Wednesday)
3 - Quinta-feira (Thursday)
4 - Sexta-feira (Friday)
5 - Sábado (Satuday)
6 - Domingo (Sunday)
"""

print(procedimento.weekday())

# aniversario = input("Informe sua data de nascimento (dd/mm/aaaa): ")
# aniversario = aniversario.split('/')
# print(aniversario)
# aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))
#
# if aniversario.weekday() == 0:
#     print("Você nasceu numa segunda-feira.")
# elif aniversario.weekday() == 1:
#     print("Você nasceu numa terça-feira.")
# elif aniversario.weekday() == 2:
#     print("Você nasceu numa quarta-feira.")
# elif aniversario.weekday() == 3:
#     print("Você nasceu numa quarta-feira.")
# elif aniversario.weekday() == 4:
#     print("Você nasceu numa sexta-feira.")
# elif aniversario.weekday() == 5:
#     print("Você nasceu num sábado.")
# elif aniversario.weekday() == 6:
#     print("Você nasceu num domingo.")

# Formatando datas/horas strftime() -> (String Format Time)
print(hoje)
"""
%d retorna o dia; %D retorna data no formato mm/dd/aa
%m retorna o mês; %M retorna os minutos
%y retorna o ano com dois dígitos; %Y retorna o ano com quatro dígitos
%h retorna o nome do mês abreviado; %H retorna a hora
%S retorna o segundo
%f retorna o microssegundo
%b retorna o nome do mês abreviado de acordo com o idioma do sistema; %B retorna o nome completo do mês
"""
hoje1 = hoje.strftime('%d/%m/%y - %H:%M:%S.%f')
hoje2 = hoje.strftime('%d de %h de %Y, %H:%M')
print(hoje1)
print(hoje2)


def converte_data(_data):
    _data = _data.split('/')
    _data = datetime.datetime(int(_data[2]), int(_data[1]), int(_data[0]))
    return _data


def formatar_data(_data):
    _nova_data = converte_data(_data)

    if _nova_data.month == 1:
        return f"{_nova_data.day} de Janeiro de {_nova_data.year}"
    elif _nova_data.month == 2:
        return f"{_nova_data.day} de Fevereiro de {_nova_data.year}"
    elif _nova_data.month == 3:
        return f"{_nova_data.day} de Março de {_nova_data.year}"
    elif _nova_data.month == 4:
        return f"{_nova_data.day} de Abril de {_nova_data.year}"
    elif _nova_data.month == 5:
        return f"{_nova_data.day} de Maio de {_nova_data.year}"
    elif _nova_data.month == 6:
        return f"{_nova_data.day} de Junho de {_nova_data.year}"
    elif _nova_data.month == 7:
        return f"{_nova_data.day} de Julho de {_nova_data.year}"
    elif _nova_data.month == 8:
        return f"{_nova_data.day} de Agosto de {_nova_data.year}"
    elif _nova_data.month == 9:
        return f"{_nova_data.day} de Setembro de {_nova_data.year}"
    elif _nova_data.month == 10:
        return f"{_nova_data.day} de Outubro de {_nova_data.year}"
    elif _nova_data.month == 11:
        return f"{_nova_data.day} de Novembro de {_nova_data.year}"
    elif _nova_data.month == 12:
        return f"{_nova_data.day} de Dezembro de {_nova_data.year}"


print(formatar_data('5/6/1987'))

# Usando textblob (pip install textblob) para traduzir o nome do mês


def textblob_data(_data):
    _nova_data = converte_data(_data)
    _mes = _nova_data.strftime("%B")
    # Se a string estiver entre aspas simples, usar aspas duplas para o valor de to e vice-versa.
    return f"{_nova_data.day} de {TextBlob(_mes).translate(to='pt-br')} de {_nova_data.year}."


print(textblob_data('5/6/1987'))  # OBS.: Textblob só funciona se estiver conectado à internet.

# Usando strptime() para passar uma string e converter em data
data = datetime.datetime.strptime('10/04/1986', '%d/%m/%Y')  # Usa a formatação de strftime()
print(data)

# Trabalhando somente com as horas:
almoco = datetime.time(12, 30, 0)
print(almoco)

# Marcando tempo de execução com timeit:
"""
Método timeit():
 - recebe 2 parâmetros: uma operação em forma de string e o número de vezes que deve executar a operação;
 - retorna o tempo que levou para executar a operação.
"""
tempo1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # Generator
print(tempo1)

tempo2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)  # List comprehension
print(tempo2)

tempo3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)  # Map
print(tempo3)


def teste(_n):
    _soma = 0

    for num in range(_n * 200):
        _soma = _soma + num ** num + 4

    return _soma


# functools.partial() recebe o nome da função e o parâmetro
tempo4 = timeit.timeit(functools.partial(teste, 5), number=10000)
print(tempo4)
