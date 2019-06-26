# coding: windows-1252
from datetime import datetime

# Data atual
print(datetime.now())

# Data atual formatada
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Data atual com diretivas de tempo
print(datetime.now().strftime('Hoje é %A do mês %B, da %U semana do ano de %Y'))

# convertendo uma string para datetime
str_to_dt = datetime.strptime('10/05/2019', '%d/%m/%Y')
print(str_to_dt)

# Diferença entre datas
data_inicial = datetime.strptime('10/05/2019 12:35:48', '%d/%m/%Y %H:%M:%S')
data_final = datetime.strptime('15/05/2019 21:51:14', '%d/%m/%Y %H:%M:%S')

diferenca = data_final - data_inicial

# A diferença entre duas datas gera um timedelta
print(type(diferenca))

print('Diferença de {} dias entre as datas'.format(diferenca.days))
print('Diferença de {} segundos entre as horas'.format(diferenca.seconds))
print('Diferença de {} minutos entre as horas'.format(diferenca.seconds / 60))
print('Diferença de {} horas entre as horas'.format(diferenca.seconds / 60 / 60))