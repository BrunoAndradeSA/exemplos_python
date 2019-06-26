# coding: windows-1252

# M�todo set() � utilizado para conjuntos que n�o permitem elementos duplicadas, n�o assegura ordem e nem �ndice entre os elementos

# Intersec��o de conjuntos
print(set([1, 2, 3, 4, 5]) & set([2, 4]))

# Uni�o de conjuntos
print(set([1, 2, 3, 4, 5]) | set([6, 7]))

# X n�o cont�m Y
print(set([1, 2, 3, 4, 5]).isdisjoint(set([6, 7])))
print(set([1, 2, 3, 4, 5]).isdisjoint(set([4, 7])))

# Diferen�a
print(set([1, 2, 3, 4]) - set([1, 3, 4]))

# Todos elementos de Y est�o em X
print(set([1, 2, 3, 6, 7, 4]) >= set([1, 2, 3]))
