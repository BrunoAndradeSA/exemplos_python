# coding: windows-1252

# Classificação de um número de 0 a 10
numero = int(input('Digite um número de 0 a 10:'))

if numero <= 10 and numero > 7:
    print('Alto')
    print('Isto faz parte do bloco if')
elif numero <= 6 and numero > 4:
    print('Médio')
    print('Isto faz parte do bloco elif')
else:
    print('Baixo')
    print('Isto faz parte do bloco else')