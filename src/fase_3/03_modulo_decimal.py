# coding: windows-1252
from decimal import Decimal, getcontext, FloatOperation

# O módulo decimal possui o type 'Decimal', não-primitivo, utilizado para cálculos
print('Representação decimal do float 0.15: {}'.format(Decimal(0.15)))
print('Representação decimal da str 0.15: {}'.format(Decimal('0.15')))

if Decimal(0.15) + Decimal(0.15) == Decimal('0.15') + Decimal('0.15'):
    print('Igual!')
else:
    print('Diferente')

# Definindo a precisão para comparação de igualdade de decimais
getcontext().prec = 2

if Decimal(0.15) + Decimal(0.15) == Decimal('0.15') + Decimal('0.15'):
    print('Igual!')
else:
    print('Diferente')

# Impedindo operações decimais com certos tipos de dados com traps
c = getcontext()

c.traps[FloatOperation] = True

print(Decimal('0.10') < 1.15)