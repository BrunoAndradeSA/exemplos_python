# coding: windows-1252

# Resultado da operação entre números do tipo 'int' e 'int'
print('################################################################################')
adicao = int(10) + int(5)
print('Adição:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = int(10) - int(5)
print('Subtração:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = int(10) * int(5)
print('Multiplicação:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = int(10) / int(5)
print('Divisão:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))

# Resultado da operação entre números do tipo 'float' e 'int'
print('################################################################################')
adicao = float(10) + int(5)
print('Adição:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = float(10) - int(5)
print('Subtração:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = float(10) * int(5)
print('Multiplicação:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = float(10) / int(5)
print('Divisão:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))

# Resultado da operação entre números do tipo 'float' e 'complex'
print('################################################################################')
adicao = float(10) + complex(5, 1)
print('Adição:'+ str(adicao) + ' - Tipo:' + str(type(adicao)))

subtracao = float(10) - complex(5, 1)
print('Subtração:'+ str(subtracao) + ' - Tipo:' + str(type(subtracao)))

multiplicacao = float(10) * complex(5, 1)
print('Multiplicação:'+ str(multiplicacao) + ' - Tipo:' + str(type(multiplicacao)))

divisao = float(10) / complex(5, 1)
print('Divisão:'+ str(divisao) + ' - Tipo:' + str(type(divisao)))
print('################################################################################')