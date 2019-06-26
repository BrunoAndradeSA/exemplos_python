# coding: windows-1252
from decimal import Decimal, getcontext, FloatOperation

# O m�dulo decimal possui o type 'Decimal', n�o-primitivo, utilizado para c�lculos
print('Representa��o decimal do float 0.15: {}'.format(Decimal(0.15)))
print('Representa��o decimal da str 0.15: {}'.format(Decimal('0.15')))

if Decimal(0.15) + Decimal(0.15) == Decimal('0.15') + Decimal('0.15'):
    print('Igual!')
else:
    print('Diferente')

# Definindo a precis�o para compara��o de igualdade de decimais
getcontext().prec = 2

if Decimal(0.15) + Decimal(0.15) == Decimal('0.15') + Decimal('0.15'):
    print('Igual!')
else:
    print('Diferente')

# Impedindo opera��es decimais com certos tipos de dados com traps
c = getcontext()

c.traps[FloatOperation] = True

print(Decimal('0.10') < 1.15)