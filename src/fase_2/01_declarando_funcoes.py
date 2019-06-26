# coding: windows-1252

# Declara��o de fun��es com 'def' - Escopo da fun��o definidido vida identa��o
def soma(num1, num2):
    return num1 + num2

print('Soma: {}'.format(soma(5, 3)))

# Declara��o de fun��es com valores default de par�metros
def soma(num1, num2=10):
    # Caso n�o seja passado 'num2', o mesmo assume o valor 10
    return num1 + num2

print('Soma Default: {}'.format(soma(5)))

# Altera��o de valores default com par�metros nomeados
print('Soma Par�metros Nomeados: {}'.format(soma(5, num2=4)))

# Fun��es com n�meros arbitr�rios de argumenos

# Packing - Passagem de par�metros atrav�s de dicion�rios que cont�m a representa��o dos par�metros da fun��o
def soma(num1, num2):
    return num1 + num2

valores = {'num1': 60, 'num2': 20}

print('Soma Packing: {}'.format(soma(**valores)))

# Unpacking com *args - Passagem de quantidades arbitr�rias de par�metros para uma fun��o, identificados pelo indice
def soma(*args):
    valor_somado = 0
    
    for v in args:
        valor_somado = valor_somado + v

    return valor_somado

print('Soma arbitr�ria pelo �ndice: {}'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9)))

# Unpacking com **kwargs - Passagem de quantidades arbitr�rias de par�metros para uma fun��o, identificados pelo nome
def unpack(**kwargs):
    for k, v in kwargs.items():
        print('Identifica��o:{} - Valor:{}'.format(k, v))

unpack(nome='Bruno', idade=30, cidade='Sorocaba')