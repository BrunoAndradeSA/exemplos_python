# coding: windows-1252

# Resultado da opera��o entre n�meros do tipo 'int' e 'int'
print('################################################################################')
adicao = int(10) + int(5)
print('Adi��o:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = int(10) - int(5)
print('Subtra��o:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = int(10) * int(5)
print('Multiplica��o:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = int(10) / int(5)
print('Divis�o:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))

# Resultado da opera��o entre n�meros do tipo 'float' e 'int'
print('################################################################################')
adicao = float(10) + int(5)
print('Adi��o:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = float(10) - int(5)
print('Subtra��o:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = float(10) * int(5)
print('Multiplica��o:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = float(10) / int(5)
print('Divis�o:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))

# Resultado da opera��o entre n�meros do tipo 'float' e 'complex'
print('################################################################################')
adicao = float(10) + complex(5, 1)
print('Adi��o:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = float(10) - complex(5, 1)
print('Subtra��o:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = float(10) * complex(5, 1)
print('Multiplica��o:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = float(10) / complex(5, 1)
print('Divis�o:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))
print('################################################################################')