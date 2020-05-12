"""
Manipulando data e hora

datetime -> Módulo built-in para trabalhar com data e hora.
"""
import datetime

print(dir(datetime))
print(datetime.MAXYEAR)  # O maior ano que o módulo reconhece
print(datetime.MINYEAR)  # O menor ano que o módulo reconhece

print(dir(datetime.datetime))
print(datetime.datetime.now())  # Retorna a data e hora atual (2020-05-08 12:44:54.316342)
# Retorna uma tupla com os valores (year, month, day, hour, minute, seconds, microseconds)
print(repr(datetime.datetime.now()))

# Ajustando data e hora:
inicio = datetime.datetime.now()
print(inicio)

# Alterando horário para um valor arbitrário
inicio = inicio.replace(hour=15, minute=27, second=46)
print(inicio)

horario = datetime.datetime.now()
horario = horario.replace(minute=horario.minute + 5)
print(horario)

print(type(horario))  # <class 'datetime.datetime'>

# # Transformando dados de entrada em uma data:
# data = input("Informe sua data de nascimento (dd/mm/aaaa): ")
# print(data)
# print(type(data))
#
# data = data.split('/')
# print(data)
#
# data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
# print(data)
# print(type(data))

# Acessando os valores individuais de ano, mês, dia, hora, minuto, segundo e microssegundo
print(horario.year)
print(horario.month)
print(horario.day)
print(horario.hour)
print(horario.minute)
print(horario.second)
print(horario.microsecond)
