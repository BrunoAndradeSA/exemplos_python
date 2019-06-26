# coding: windows-1252

# Tuplas = 'tuples'

tupla = (1, 2, 3, 4, 5, 'Seis', 'Sete')
print(tupla)

# 'Slice' de tuplas
print(tupla[2])
print(tupla[2:4])

# tuplas são IMUTÁVEIS
# tupla[2] = 9
# print(tupla)

# Contando ocorrências de itens da tupla [Retorna 0 se não encontrar] - count()
print(tupla.count(2))

# Retornar o índice de determinado elemento da tupla [Caso ERRO caso não localize o item]- index()
print(tupla.index(3))

# Iterando sobre tuplas
print('Iteração:')
for elemento in tupla:
    print(elemento)