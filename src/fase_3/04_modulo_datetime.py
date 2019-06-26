# coding: windows-1252
from datetime import datetime

# Data atual
print(datetime.now())

# Data atual formatada
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Data atual com diretivas de tempo
print(datetime.now().strftime('Hoje � %A do m�s %B, da %U semana do ano de %Y'))

# convertendo uma string para datetime
str_to_dt = datetime.strptime('10/05/2019', '%d/%m/%Y')
print(str_to_dt)

# Diferen�a entre datas
data_inicial = datetime.strptime('10/05/2019 12:35:48', '%d/%m/%Y %H:%M:%S')
data_final = datetime.strptime('15/05/2019 21:51:14', '%d/%m/%Y %H:%M:%S')

diferenca = data_final - data_inicial

# A diferen�a entre duas datas gera um timedelta
print(type(diferenca))

print('Diferen�a de {} dias entre as datas'.format(diferenca.days))
print('Diferen�a de {} segundos entre as horas'.format(diferenca.seconds))
print('Diferen�a de {} minutos entre as horas'.format(diferenca.seconds / 60))
print('Diferen�a de {} horas entre as horas'.format(diferenca.seconds / 60 / 60))