# coding: windows-1252

# Declaração de funções com 'def' - Escopo da função definidido vida identação
def soma(num1, num2):
    return num1 + num2

print('Soma: {}'.format(soma(5, 3)))

# Declaração de funções com valores default de parâmetros
def soma(num1, num2=10):
    # Caso não seja passado 'num2', o mesmo assume o valor 10
    return num1 + num2

print('Soma Default: {}'.format(soma(5)))

# Alteração de valores default com parâmetros nomeados
print('Soma Parâmetros Nomeados: {}'.format(soma(5, num2=4)))

# Funções com números arbitrários de argumenos

# Packing - Passagem de parâmetros através de dicionários que contém a representação dos parâmetros da função
def soma(num1, num2):
    return num1 + num2

valores = {'num1': 60, 'num2': 20}

print('Soma Packing: {}'.format(soma(**valores)))

# Unpacking com *args - Passagem de quantidades arbitrárias de parâmetros para uma função, identificados pelo indice
def soma(*args):
    valor_somado = 0
    
    for v in args:
        valor_somado = valor_somado + v

    return valor_somado

print('Soma arbitrária pelo índice: {}'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9)))

# Unpacking com **kwargs - Passagem de quantidades arbitrárias de parâmetros para uma função, identificados pelo nome
def unpack(**kwargs):
    for k, v in kwargs.items():
        print('Identificação:{} - Valor:{}'.format(k, v))

unpack(nome='Bruno', idade=30, cidade='Sorocaba')