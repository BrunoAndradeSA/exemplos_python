# coding: windows-1252

# Tuplas = 'tuples'

tupla = (1, 2, 3, 4, 5, 'Seis', 'Sete')
print(tupla)

# 'Slice' de tuplas
print(tupla[2])
print(tupla[2:4])

# tuplas s�o IMUT�VEIS
# tupla[2] = 9
# print(tupla)

# Contando ocorr�ncias de itens da tupla [Retorna 0 se n�o encontrar] - count()
print(tupla.count(2))

# Retornar o �ndice de determinado elemento da tupla [Caso ERRO caso n�o localize o item]- index()
print(tupla.index(3))

# Iterando sobre tuplas
print('Itera��o:')
for elemento in tupla:
    print(elemento)