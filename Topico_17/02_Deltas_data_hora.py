"""
Trabalhando com deltas de data e hora

Delta: diferença entre uma data e outra
delta = data final - data inicial
"""
import datetime

# Diferença entre datas
hoje = datetime.datetime.now()
aniversario = datetime.datetime(2020, 8, 19, 0)

tempo = aniversario - hoje

print(tempo)
print(type(tempo))  # <class 'datetime.timedelta'>
print(tempo.days)

# Exemplo: calculando o delta em dias:
data_compra = datetime.datetime.now()
print(data_compra)

tempo_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_compra + tempo_boleto
print(vencimento_boleto)
print(type(vencimento_boleto))
